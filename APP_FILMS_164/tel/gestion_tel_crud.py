"""Gestion des "routes" FLASK et des données pour les tel.
Fichier : gestion_tel_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.tel.gestion_tel_wtf_forms import FormWTFAjoutertel
from APP_FILMS_164.tel.gestion_tel_wtf_forms import FormWTFDeletetel
from APP_FILMS_164.tel.gestion_tel_wtf_forms import FormWTFUpdatetel

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /tel_afficher
    
    Test : ex : http://127.0.0.1:5005/tel_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_tel_sel = 0 >> tous les tel.
                id_tel_sel = "n" affiche le tel dont l'id est "n"
"""


@app.route("/tel_afficher/<string:order_by>/<int:id_tel_sel>", methods=['GET', 'POST'])
def tel_afficher(order_by, id_tel_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_tel_sel == 0:
                    strsql_tel_afficher = """SELECT id_tel, 
                    numero_tel,
                    prenom_tel 
                    
                    FROM t_tel ORDER BY id_tel ASC"""


                    mc_afficher.execute(strsql_tel_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_tel"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les villes d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du tel sélectionné avec un ville de variable
                    valeur_id_tel_selected_dictionnaire = {"value_id_tel_selected": id_tel_sel}
                    strsql_tel_afficher = """SELECT id_tel, numero_tel,prenom_tel  FROM t_tel WHERE id_tel = %(value_id_tel_selected)s"""

                    mc_afficher.execute(strsql_tel_afficher, valeur_id_tel_selected_dictionnaire)
                else:
                    strsql_tel_afficher = """SELECT id_tel, numero_tel,prenom_tel  FROM t_tel ORDER BY id_tel DESC"""

                    mc_afficher.execute(strsql_tel_afficher)

                data_tel = mc_afficher.fetchall()

                print("data_tel ", data_tel, " Type : ", type(data_tel))

                # Différencier les messages si la table est vide.
                if not data_tel and id_tel_sel == 0:
                    flash("""La table "t_tel" est vide. !!""", "warning")
                elif not data_tel and id_tel_sel > 0:
                    # Si l'utilisateur change l'id_tel dans l'URL et que le tel n'existe pas,
                    flash(f"Le tel demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_tel" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données tel affichés !!", "success")

        except Exception as Exception_tel_afficher:
            raise ExceptiontelAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{tel_afficher.__name__} ; "
                                          f"{Exception_tel_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("tel/tel_afficher.html", data=data_tel)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /tel_ajouter
    
    Test : ex : http://127.0.0.1:5005/tel_ajouter
    
    Paramètres : sans
    
    But : Ajouter un tel pour un tel
    
    Remarque :  Dans le champ "name_tel_html" du formulaire "tel/tel_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/tel_ajouter", methods=['GET', 'POST'])
def tel_ajouter_wtf():
    form = FormWTFAjoutertel()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                numero_tel_wtf = form.numero_tel_wtf.data
                prenom_tel_wtf = form.prenom_tel_wtf.data

                valeurs_insertion_dictionnaire = {"value_numero_tel": numero_tel_wtf,
                                                  "value_prenom_tel" : prenom_tel_wtf

                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)



               #strsql_insert_tel = """INSERT INTO t_tel (id_tel,numero_tel,prenom_tel,personne_tel) VALUES (NULL,%(value_numero_tel)s,%(value_prenom_tel)s,%(value_personne_tel)s)"""
                strsql_insert_tel = """INSERT INTO `t_tel` (`id_tel`, `numero_tel`, `prenom_tel`) VALUES (NULL, %(value_numero_tel)s, %(value_prenom_tel)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_tel, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('tel_afficher', order_by='DESC', id_tel_sel=0))

        except Exception as Exception_tel_ajouter_wtf:
            raise ExceptiontelAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{tel_ajouter_wtf.__name__} ; "
                                            f"{Exception_tel_ajouter_wtf}")

    return render_template("tel/tel_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /tel_update
    
    Test : ex cliquer sur le menu "tel" puis cliquer sur le bouton "EDIT" d'un "tel"
    
    Paramètres : sans
    
    But : Editer(update) un tel qui a été sélectionné dans le formulaire "tel_afficher.html"
    
    Remarque :  Dans le champ "numero_tel_update_wtf" du formulaire "tel/tel_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/tel_update", methods=['GET', 'POST'])
def tel_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_tel"
    id_tel_update = request.values['id_tel_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatetel()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "tel_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            numero_tel_update = form_update.numero_tel_update_wtf.data
          #  name_tel_update = name_tel_update.lower()
            prenom_tel_update = form_update.prenom_tel_update_wtf.data

            valeur_update_dictionnaire = {"value_id_tel": id_tel_update,
                                          "value_numero_tel": numero_tel_update,
                                          "value_prenom_tel": prenom_tel_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_villetel = """UPDATE t_tel SET numero_tel = %(value_numero_tel)s, prenom_tel = %(value_prenom_tel)s WHERE id_tel = %(value_id_tel)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_villetel, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_tel_update"
            return redirect(url_for('tel_afficher', order_by="ASC", id_tel_sel=id_tel_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_tel" et "numero_tel" de la "t_tel"
            str_sql_id_tel = "SELECT id_tel, numero_tel, prenom_tel FROM t_tel " \
                               "WHERE id_tel = %(value_id_tel)s"
            valeur_select_dictionnaire = {"value_id_tel": id_tel_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_tel, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "ville tel" pour l'UPDATE
            data_numero_tel = mybd_conn.fetchone()
            print("data_numero_tel ", data_numero_tel, " type ", type(data_numero_tel), " tel ",
                  data_numero_tel["numero_tel"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "tel_update_wtf.html"
            form_update.numero_tel_update_wtf.data = data_numero_tel["numero_tel"]
            form_update.prenom_tel_update_wtf.data = data_numero_tel["prenom_tel"]


    except Exception as Exception_tel_update_wtf:
        raise ExceptiontelUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{tel_update_wtf.__name__} ; "
                                      f"{Exception_tel_update_wtf}")

    return render_template("tel/tel_update_wtf.html", form_update=form_update)



"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /tel_delete
    
    Test : ex. cliquer sur le menu "tel" puis cliquer sur le bouton "DELETE" d'un "tel"
    
    Paramètres : sans
    
    But : Effacer(delete) un tel qui a été sélectionné dans le formulaire "tel_afficher.html"
    
    Remarque :  Dans le champ "numero_tel_delete_wtf" du formulaire "tel/tel_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""

@app.route("/tel_delete", methods=['GET', 'POST'])
def tel_delete_wtf():

    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_tel"
    id_tel_delete = request.values['id_tel_btn_delete_html']

    # Objet formulaire pour effacer le tel sélectionné.
    form_delete = FormWTFDeletetel()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("tel_afficher", order_by="ASC", id_tel_sel=0))






            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_tel": id_tel_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_id_tel = """DELETE FROM t_tel WHERE id_tel = %(value_id_tel)s"""
                # Manière brutale d'effacer d'abord la "fk_tel", même si elle n'existe pas dans la "t_tel_film"
                # Ensuite on peut effacer le tel vu qu'il n'est plus "lié" (INNODB) dans la "t_tel_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_id_tel, valeur_delete_dictionnaire)
                flash(f"tel définitivement effacé !!", "success")
                print(f"tel définitivement effacé !!")

                # afficher les données
                return redirect(url_for('tel_afficher', order_by="ASC", id_tel_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_tel": id_tel_delete}
            print(id_tel_delete, type(id_tel_delete))

            # Requête qui affiche tous les films_tel qui ont le tel que l'utilisateur veut effacer

            with DBconnection() as mydb_conn:


                # Opération sur la BD pour récupérer "id_tel" et "numero_tel" de la "t_tel"
                str_sql_id_tel = "SELECT id_tel, numero_tel FROM t_tel WHERE id_tel = %(value_id_tel)s"

                mydb_conn.execute(str_sql_id_tel, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "ville tel" pour l'action DELETE
                data_numero_tel = mydb_conn.fetchone()
                print("data_numero_tel ", data_numero_tel, " type ", type(data_numero_tel), " tel ",
                      data_numero_tel["numero_tel"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "tel_delete_wtf.html"
            form_delete.numero_tel_delete_wtf.data = data_numero_tel["numero_tel"]

            # Le bouton pour l'action "DELETE" dans le form. "tel_delete_wtf.html" est caché.
            btn_submit_del = True

    except Exception as Exception_tel_delete_wtf:
        raise ExceptiontelDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{tel_delete_wtf.__name__} ; "
                                      f"{Exception_tel_delete_wtf}")

    return render_template("tel/tel_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)
