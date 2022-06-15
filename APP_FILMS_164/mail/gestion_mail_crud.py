"""Gestion des "routes" FLASK et des données pour les mail.
Fichier : gestion_mail_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.mail.gestion_mail_wtf_forms import FormWTFAjoutermail
from APP_FILMS_164.mail.gestion_mail_wtf_forms import FormWTFDeletemail
from APP_FILMS_164.mail.gestion_mail_wtf_forms import FormWTFUpdatemail

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /mail_afficher
    
    Test : ex : http://127.0.0.1:5005/mail_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_mail_sel = 0 >> tous les mail.
                id_mail_sel = "n" affiche le mail dont l'id est "n"
"""


@app.route("/mail_afficher/<string:order_by>/<int:id_mail_sel>", methods=['GET', 'POST'])
def mail_afficher(order_by, id_mail_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_mail_sel == 0:
                    strsql_mail_afficher = """SELECT id_mail, 
                    mail_mail,
                     
                    personne_mail 
                    FROM t_mail ORDER BY id_mail ASC"""


                    mc_afficher.execute(strsql_mail_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_mail"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les villes d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du mail sélectionné avec un ville de variable
                    valeur_id_mail_selected_dictionnaire = {"value_id_mail_selected": id_mail_sel}
                    strsql_mail_afficher = """SELECT id_mail, mail_mail, personne_mail  FROM t_mail WHERE id_mail = %(value_id_mail_selected)s"""

                    mc_afficher.execute(strsql_mail_afficher, valeur_id_mail_selected_dictionnaire)
                else:
                    strsql_mail_afficher = """SELECT id_mail, mail_mail, personne_mail  FROM t_mail ORDER BY id_mail DESC"""

                    mc_afficher.execute(strsql_mail_afficher)

                data_mail = mc_afficher.fetchall()

                print("data_mail ", data_mail, " Type : ", type(data_mail))

                # Différencier les messages si la table est vide.
                if not data_mail and id_mail_sel == 0:
                    flash("""La table "t_mail" est vide. !!""", "warning")
                elif not data_mail and id_mail_sel > 0:
                    # Si l'utilisateur change l'id_mail dans l'URL et que le mail n'existe pas,
                    flash(f"Le mail demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_mail" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données mail affichés !!", "success")

        except Exception as Exception_mail_afficher:
            raise ExceptionmailAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{mail_afficher.__name__} ; "
                                          f"{Exception_mail_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("mail/mail_afficher.html", data=data_mail)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /mail_ajouter
    
    Test : ex : http://127.0.0.1:5005/mail_ajouter
    
    Paramètres : sans
    
    But : Ajouter un mail pour un mail
    
    Remarque :  Dans le champ "name_mail_html" du formulaire "mail/mail_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/mail_ajouter", methods=['GET', 'POST'])
def mail_ajouter_wtf():
    form = FormWTFAjoutermail()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                mail_mail_wtf = form.mail_mail_wtf.data
                personne_mail_wtf = form.personne_mail_wtf.data
                valeurs_insertion_dictionnaire = {"value_mail_mail": mail_mail_wtf,
                                                  "value_personne_mail" : personne_mail_wtf
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)



               #strsql_insert_mail = """INSERT INTO t_mail (id_mail,mail_mail,personne_mail) VALUES (NULL,%(value_mail_mail)s,%(value_batiment_mail)s,%(value_personne_mail)s)"""
                strsql_insert_mail = """INSERT INTO `t_mail` (`id_mail`, `mail_mail`, `personne_mail`) VALUES (NULL, %(value_mail_mail)s, %(value_personne_mail)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_mail, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('mail_afficher', order_by='DESC', id_mail_sel=0))

        except Exception as Exception_mail_ajouter_wtf:
            raise ExceptionmailAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{mail_ajouter_wtf.__name__} ; "
                                            f"{Exception_mail_ajouter_wtf}")

    return render_template("mail/mail_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /mail_update
    
    Test : ex cliquer sur le menu "mail" puis cliquer sur le bouton "EDIT" d'un "mail"
    
    Paramètres : sans
    
    But : Editer(update) un mail qui a été sélectionné dans le formulaire "mail_afficher.html"
    
    Remarque :  Dans le champ "mail_mail_update_wtf" du formulaire "mail/mail_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/mail_update", methods=['GET', 'POST'])
def mail_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_mail"
    id_mail_update = request.values['id_mail_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatemail()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "mail_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            mail_mail_update = form_update.mail_mail_update_wtf.data
          #  name_mail_update = name_mail_update.lower()
            personne_mail_update = form_update.personne_mail_update_wtf.data

            valeur_update_dictionnaire = {"value_id_mail": id_mail_update,
                                          "value_mail_mail": mail_mail_update,
                                          "value_personne_mail": personne_mail_update,
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_villemail = """UPDATE t_mail SET mail_mail = %(value_mail_mail)s, personne_mail = %(value_personne_mail)s WHERE id_mail = %(value_id_mail)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_villemail, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_mail_update"
            return redirect(url_for('mail_afficher', order_by="ASC", id_mail_sel=id_mail_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_mail" et "mail_mail" de la "t_mail"
            str_sql_id_mail = "SELECT id_mail, mail_mail,  personne_mail FROM t_mail " \
                               "WHERE id_mail = %(value_id_mail)s"
            valeur_select_dictionnaire = {"value_id_mail": id_mail_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_mail, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "ville mail" pour l'UPDATE
            data_mail_mail = mybd_conn.fetchone()
            print("data_mail_mail ", data_mail_mail, " type ", type(data_mail_mail), " mail ",
                  data_mail_mail["mail_mail"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "mail_update_wtf.html"
            form_update.mail_mail_update_wtf.data = data_mail_mail["mail_mail"]
            form_update.personne_mail_update_wtf.data = data_mail_mail["personne_mail"]

    except Exception as Exception_mail_update_wtf:
        raise ExceptionmailUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{mail_update_wtf.__name__} ; "
                                      f"{Exception_mail_update_wtf}")

    return render_template("mail/mail_update_wtf.html", form_update=form_update)



"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /mail_delete
    
    Test : ex. cliquer sur le menu "mail" puis cliquer sur le bouton "DELETE" d'un "mail"
    
    Paramètres : sans
    
    But : Effacer(delete) un mail qui a été sélectionné dans le formulaire "mail_afficher.html"
    
    Remarque :  Dans le champ "mail_mail_delete_wtf" du formulaire "mail/mail_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""

@app.route("/mail_delete", methods=['GET', 'POST'])
def mail_delete_wtf():

    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_mail"
    id_mail_delete = request.values['id_mail_btn_delete_html']

    # Objet formulaire pour effacer le mail sélectionné.
    form_delete = FormWTFDeletemail()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("mail_afficher", order_by="ASC", id_mail_sel=0))






            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_mail": id_mail_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_id_mail = """DELETE FROM t_mail WHERE id_mail = %(value_id_mail)s"""
                # Manière brutale d'effacer d'abord la "fk_mail", même si elle n'existe pas dans la "t_mail_film"
                # Ensuite on peut effacer le mail vu qu'il n'est plus "lié" (INNODB) dans la "t_mail_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_id_mail, valeur_delete_dictionnaire)
                flash(f"mail définitivement effacé !!", "success")
                print(f"mail définitivement effacé !!")

                # afficher les données
                return redirect(url_for('mail_afficher', order_by="ASC", id_mail_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_mail": id_mail_delete}
            print(id_mail_delete, type(id_mail_delete))

            # Requête qui affiche tous les films_mail qui ont le mail que l'utilisateur veut effacer

            with DBconnection() as mydb_conn:


                # Opération sur la BD pour récupérer "id_mail" et "mail_mail" de la "t_mail"
                str_sql_id_mail = "SELECT id_mail, mail_mail FROM t_mail WHERE id_mail = %(value_id_mail)s"

                mydb_conn.execute(str_sql_id_mail, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "ville mail" pour l'action DELETE
                data_mail_mail = mydb_conn.fetchone()
                print("data_mail_mail ", data_mail_mail, " type ", type(data_mail_mail), " mail ",
                      data_mail_mail["mail_mail"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "mail_delete_wtf.html"
            form_delete.mail_mail_delete_wtf.data = data_mail_mail["mail_mail"]

            # Le bouton pour l'action "DELETE" dans le form. "mail_delete_wtf.html" est caché.
            btn_submit_del = True

    except Exception as Exception_mail_delete_wtf:
        raise ExceptionmailDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{mail_delete_wtf.__name__} ; "
                                      f"{Exception_mail_delete_wtf}")

    return render_template("mail/mail_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)
