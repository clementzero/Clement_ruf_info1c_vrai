"""Gestion des "routes" FLASK et des données pour les adresse.
Fichier : gestion_adresse_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.adresse.gestion_adresse_wtf_forms import FormWTFAjouteradresse
from APP_FILMS_164.adresse.gestion_adresse_wtf_forms import FormWTFDeleteadresse
from APP_FILMS_164.adresse.gestion_adresse_wtf_forms import FormWTFUpdateadresse

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /adresse_afficher
    
    Test : ex : http://127.0.0.1:5005/adresse_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_adresse_sel = 0 >> tous les adresse.
                id_adresse_sel = "n" affiche le adresse dont l'id est "n"
"""


@app.route("/adresse_afficher/<string:order_by>/<int:id_adresse_sel>", methods=['GET', 'POST'])
def adresse_afficher(order_by, id_adresse_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_adresse_sel == 0:
                    strsql_adresse_afficher = """SELECT id_adresse, 
                    ville_adresse,
                    batiment_adresse, 
                    personne_adresse 
                    FROM t_adresse ORDER BY id_adresse ASC"""


                    mc_afficher.execute(strsql_adresse_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_adresse"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les villes d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du adresse sélectionné avec un ville de variable
                    valeur_id_adresse_selected_dictionnaire = {"value_id_adresse_selected": id_adresse_sel}
                    strsql_adresse_afficher = """SELECT id_adresse, ville_adresse,batiment_adresse, personne_adresse  FROM t_adresse WHERE id_adresse = %(value_id_adresse_selected)s"""

                    mc_afficher.execute(strsql_adresse_afficher, valeur_id_adresse_selected_dictionnaire)
                else:
                    strsql_adresse_afficher = """SELECT id_adresse, ville_adresse,batiment_adresse, personne_adresse  FROM t_adresse ORDER BY id_adresse DESC"""

                    mc_afficher.execute(strsql_adresse_afficher)

                data_adresse = mc_afficher.fetchall()

                print("data_adresse ", data_adresse, " Type : ", type(data_adresse))

                # Différencier les messages si la table est vide.
                if not data_adresse and id_adresse_sel == 0:
                    flash("""La table "t_adresse" est vide. !!""", "warning")
                elif not data_adresse and id_adresse_sel > 0:
                    # Si l'utilisateur change l'id_adresse dans l'URL et que le adresse n'existe pas,
                    flash(f"Le adresse demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_adresse" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données adresse affichés !!", "success")

        except Exception as Exception_adresse_afficher:
            raise ExceptionadresseAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{adresse_afficher.__name__} ; "
                                          f"{Exception_adresse_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("adresse/adresse_afficher.html", data=data_adresse)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /adresse_ajouter
    
    Test : ex : http://127.0.0.1:5005/adresse_ajouter
    
    Paramètres : sans
    
    But : Ajouter un adresse pour un adresse
    
    Remarque :  Dans le champ "name_adresse_html" du formulaire "adresse/adresse_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/adresse_ajouter", methods=['GET', 'POST'])
def adresse_ajouter_wtf():
    form = FormWTFAjouteradresse()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                ville_adresse_wtf = form.ville_adresse_wtf.data
                batiment_adresse_wtf = form.batiment_adresse_wtf.data
                personne_adresse_wtf = form.personne_adresse_wtf.data
                valeurs_insertion_dictionnaire = {"value_ville_adresse": ville_adresse_wtf,
                                                  "value_batiment_adresse" : batiment_adresse_wtf,
                                                  "value_personne_adresse" : personne_adresse_wtf
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)



               #strsql_insert_adresse = """INSERT INTO t_adresse (id_adresse,ville_adresse,batiment_adresse,personne_adresse) VALUES (NULL,%(value_ville_adresse)s,%(value_batiment_adresse)s,%(value_personne_adresse)s)"""
                strsql_insert_adresse = """INSERT INTO `t_adresse` (`id_adresse`, `ville_adresse`, `batiment_adresse`, `personne_adresse`) VALUES (NULL, %(value_ville_adresse)s, %(value_batiment_adresse)s, %(value_personne_adresse)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_adresse, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('adresse_afficher', order_by='DESC', id_adresse_sel=0))

        except Exception as Exception_adresse_ajouter_wtf:
            raise ExceptionadresseAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{adresse_ajouter_wtf.__name__} ; "
                                            f"{Exception_adresse_ajouter_wtf}")

    return render_template("Adresse/adresse_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /adresse_update
    
    Test : ex cliquer sur le menu "adresse" puis cliquer sur le bouton "EDIT" d'un "adresse"
    
    Paramètres : sans
    
    But : Editer(update) un adresse qui a été sélectionné dans le formulaire "adresse_afficher.html"
    
    Remarque :  Dans le champ "ville_adresse_update_wtf" du formulaire "adresse/adresse_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/adresse_update", methods=['GET', 'POST'])
def adresse_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_adresse"
    id_adresse_update = request.values['id_adresse_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateadresse()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "adresse_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            ville_adresse_update = form_update.ville_adresse_update_wtf.data
          #  name_adresse_update = name_adresse_update.lower()
            batiment_adresse_update = form_update.batiment_adresse_update_wtf.data
            personne_adresse_update = form_update.personne_adresse_update_wtf.data

            valeur_update_dictionnaire = {"value_id_adresse": id_adresse_update,
                                          "value_ville_adresse": ville_adresse_update,
                                          "value_personne_adresse": personne_adresse_update,
                                          "value_batiment_adresse": batiment_adresse_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_villeadresse = """UPDATE t_adresse SET ville_adresse = %(value_ville_adresse)s, 
            batiment_adresse = %(value_batiment_adresse)s, personne_adresse = %(value_personne_adresse)s WHERE id_adresse = %(value_id_adresse)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_villeadresse, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_adresse_update"
            return redirect(url_for('Adresse_afficher', order_by="ASC", id_adresse_sel=id_adresse_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_adresse" et "ville_adresse" de la "t_adresse"
            str_sql_id_adresse = "SELECT id_adresse, ville_adresse, batiment_adresse, personne_adresse FROM t_adresse " \
                               "WHERE id_adresse = %(value_id_adresse)s"
            valeur_select_dictionnaire = {"value_id_adresse": id_adresse_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_adresse, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "ville adresse" pour l'UPDATE
            data_ville_adresse = mybd_conn.fetchone()
            print("data_ville_adresse ", data_ville_adresse, " type ", type(data_ville_adresse), " adresse ",
                  data_ville_adresse["ville_adresse"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "adresse_update_wtf.html"
            form_update.ville_adresse_update_wtf.data = data_ville_adresse["ville_adresse"]
            form_update.batiment_adresse_update_wtf.data = data_ville_adresse["batiment_adresse"]
            form_update.personne_adresse_update_wtf.data = data_ville_adresse["personne_adresse"]

    except Exception as Exception_adresse_update_wtf:
        raise ExceptionadresseUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{adresse_update_wtf.__name__} ; "
                                      f"{Exception_adresse_update_wtf}")

    return render_template("Adresse/adresse_update_wtf.html", form_update=form_update)



"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /adresse_delete
    
    Test : ex. cliquer sur le menu "adresse" puis cliquer sur le bouton "DELETE" d'un "adresse"
    
    Paramètres : sans
    
    But : Effacer(delete) un adresse qui a été sélectionné dans le formulaire "adresse_afficher.html"
    
    Remarque :  Dans le champ "ville_adresse_delete_wtf" du formulaire "adresse/adresse_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""

@app.route("/adresse_delete", methods=['GET', 'POST'])
def adresse_delete_wtf():

    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_adresse"
    id_adresse_delete = request.values['id_adresse_btn_delete_html']

    # Objet formulaire pour effacer le adresse sélectionné.
    form_delete = FormWTFDeleteadresse()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("Adresse_afficher", order_by="ASC", id_adresse_sel=0))






            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_adresse": id_adresse_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_id_adresse = """DELETE FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"""
                # Manière brutale d'effacer d'abord la "fk_adresse", même si elle n'existe pas dans la "t_adresse_film"
                # Ensuite on peut effacer le adresse vu qu'il n'est plus "lié" (INNODB) dans la "t_adresse_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_id_adresse, valeur_delete_dictionnaire)
                flash(f"adresse définitivement effacé !!", "success")
                print(f"adresse définitivement effacé !!")

                # afficher les données
                return redirect(url_for('Adresse_afficher', order_by="ASC", id_adresse_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_adresse": id_adresse_delete}
            print(id_adresse_delete, type(id_adresse_delete))

            # Requête qui affiche tous les films_Adresse qui ont le adresse que l'utilisateur veut effacer

            with DBconnection() as mydb_conn:


                # Opération sur la BD pour récupérer "id_adresse" et "ville_adresse" de la "t_adresse"
                str_sql_id_adresse = "SELECT id_adresse, ville_adresse FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"

                mydb_conn.execute(str_sql_id_adresse, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "ville adresse" pour l'action DELETE
                data_ville_adresse = mydb_conn.fetchone()
                print("data_ville_adresse ", data_ville_adresse, " type ", type(data_ville_adresse), " adresse ",
                      data_ville_adresse["ville_adresse"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "adresse_delete_wtf.html"
            form_delete.ville_adresse_delete_wtf.data = data_ville_adresse["ville_adresse"]

            # Le bouton pour l'action "DELETE" dans le form. "adresse_delete_wtf.html" est caché.
            btn_submit_del = True

    except Exception as Exception_adresse_delete_wtf:
        raise ExceptionadresseDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{adresse_delete_wtf.__name__} ; "
                                      f"{Exception_adresse_delete_wtf}")

    return render_template("Adresse/adresse_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)
