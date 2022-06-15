"""Gestion des "routes" FLASK et des données pour les objet.
Fichier : gestion_objet_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import url_for
from flask import session

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.objet.gestion_objet_wtf_forms import FormWTFAjouterobjet
from APP_FILMS_164.objet.gestion_objet_wtf_forms import FormWTFDeleteobjet
from APP_FILMS_164.objet.gestion_objet_wtf_forms import FormWTFUpdateobjet

"""Ajouter un objet grâce au formulaire "objet_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /objet

Test : exemple: cliquer sur le menu "objet/objet" puis cliquer sur le bouton "ADD" d'un "objet"

Paramètres : sans


Remarque :  Dans le champ "nom_objet_update_wtf" du formulaire "objet/objet_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/objet_afficher/<string:order_by>/<int:id_objet_sel>", methods=['GET', 'POST'])
def objet_afficher(order_by, id_objet_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_objet_sel == 0:
                    strsql_objet_afficher = """SELECT id_objet,nom_objet, num_serie_objet, creation_objet, description_objet, nombre_objet

                    FROM t_objet ORDER BY id_objet ASC"""

                    mc_afficher.execute(strsql_objet_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_objet"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les villes d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du objet sélectionné avec un ville de variable
                    valeur_id_objet_selected_dictionnaire = {"value_id_objet_selected": id_objet_sel}
                    strsql_objet_afficher = """SELECT id_objet,nom_objet, num_serie_objet, creation_objet, description_objet  FROM t_objet WHERE id_objet = %(value_id_objet_selected)s"""

                    mc_afficher.execute(strsql_objet_afficher, valeur_id_objet_selected_dictionnaire)
                else:
                    strsql_objet_afficher = """SELECT id_objet,nom_objet, num_serie_objet, creation_objet, description_objet  FROM t_objet ORDER BY id_objet DESC"""

                    mc_afficher.execute(strsql_objet_afficher)

                data_objet = mc_afficher.fetchall()

                print("data_objet ", data_objet, " Type : ", type(data_objet))

                # Différencier les messages si la table est vide.
                if not data_objet and id_objet_sel == 0:
                    flash("""La table "t_objet" est vide. !!""", "warning")
                elif not data_objet and id_objet_sel > 0:
                    # Si l'utilisateur change l'id_objet dans l'URL et que le objet n'existe pas,
                    flash(f"Le objet demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_objet" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données objet affichés !!", "success")

        except Exception as Exception_objet_afficher:
            raise ExceptionobjetAfficher(f"fichier : {Path(__file__).name}  ;  "
                                       f"{objet_afficher.__name__} ; "
                                       f"{Exception_objet_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("objet/objet_afficher.html", data=data_objet)



















@app.route("/objet_ajouter", methods=['GET', 'POST'])
def objet_ajouter_wtf():
    form = FormWTFAjouterobjet()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_objet_wtf = form.nom_objet_wtf.data
                num_serie_objet_wtf = form.num_serie_objet_wtf.data
                description_objet_wtf = form.description_objet_wtf.data
                nombre_objet_wtf = form.nombre_objet_wtf.data
                creation_objet_wtf = form.creation_objet_wtf.data
                valeurs_insertion_dictionnaire = {"value_nom_objet": nom_objet_wtf,
                                                  "value_num_serie_objet" : num_serie_objet_wtf,
                                                  "value_description_objet": description_objet_wtf,
                                                  "value_nombre_objet": nombre_objet_wtf,
                                                  "value_creation_objet": creation_objet_wtf

                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)



               #strsql_insert_objet = """INSERT INTO t_objet (id_objet,nom_objet,objet_objet) VALUES (NULL,%(value_nom_objet)s,%(value_batiment_objet)s,%(value_objet_objet)s)"""
                strsql_insert_objet = """INSERT INTO `t_objet` (`id_objet`, `nom_objet`, `num_serie_objet`,`description_objet`, `nombre_objet`, `creation_objet`) VALUES (NULL, %(value_nom_objet)s, %(value_num_serie_objet)s, %(value_description_objet)s, %(value_nombre_objet)s, %(value_creation_objet)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_objet, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('objet_afficher', order_by='DESC', id_objet_sel=0))

        except Exception as Exception_objet_ajouter_wtf:
            raise ExceptionobjetAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{objet_ajouter_wtf.__name__} ; "
                                            f"{Exception_objet_ajouter_wtf}")

    return render_template("objet/objet_ajouter_wtf.html", form=form)


"""Editer(update) un objet qui a été sélectionné dans le formulaire "objet_objet_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /objet_update

Test : exemple: cliquer sur le menu "objet/objet" puis cliquer sur le bouton "EDIT" d'un "objet"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "objet_afficher.html"

Remarque :  Dans le champ "nom_objet_update_wtf" du formulaire "objet/objet_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/objet_update", methods=['GET', 'POST'])
def objet_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_objet"
    id_objet_update = request.values['id_objet_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_objet = FormWTFUpdateobjet()
    try:
        print(" on submit ", form_update_objet.validate_on_submit())
        if form_update_objet.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            nom_objet_update = form_update_objet.nom_objet_update_wtf.data
            num_serie_objet_update = form_update_objet.num_serie_objet_update_wtf.data
            description_objet_update = form_update_objet.description_objet_update_wtf.data
            creation_objet_update = form_update_objet.creation_objet_update_wtf.data
            nombre_objet_update = form_update_objet.nombre_objet_update_wtf.data

            valeur_update_dictionnaire = {"value_id_objet": id_objet_update,
                                          "value_nom_objet": nom_objet_update,
                                          "value_num_serie_objet": num_serie_objet_update,
                                          "value_description_objet": description_objet_update,
                                          "value_creation_objet": creation_objet_update,
                                          "value_nombre_objet": nombre_objet_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_objet = """UPDATE t_objet SET nom_objet = %(value_nom_objet)s,
                                                            num_serie_objet = %(value_num_serie_objet)s,
                                                            description_objet = %(value_description_objet)s,
                                                            creation_objet = %(value_creation_objet)s,
                                                            nombre_objet = %(value_nombre_objet)s
                                                            WHERE id_objet = %(value_id_objet)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_objet, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le objet modifié, "ASC" et l'"id_objet_update"
            return redirect(url_for('objet_objet_afficher', id_objet_sel=id_objet_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_objet" et "intitule_genre" de la "t_genre"
            str_sql_id_objet = "SELECT * FROM t_objet WHERE id_objet = %(value_id_objet)s"
            valeur_select_dictionnaire = {"value_id_objet": id_objet_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_objet, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_objet = mybd_conn.fetchone()
            print("data_objet ", data_objet, " type ", type(data_objet), " genre ",
                  data_objet["nom_objet"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "objet_update_wtf.html"
            form_update_objet.nom_objet_update_wtf.data = data_objet["nom_objet"]
            form_update_objet.num_serie_objet_update_wtf.data = data_objet["num_serie_objet"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" num_serie objet  ", data_objet["num_serie_objet"], "  type ", type(data_objet["num_serie_objet"]))
            form_update_objet.description_objet_update_wtf.data = data_objet["description_objet"]
            form_update_objet.creation_objet_update_wtf.data = data_objet["creation_objet"]
            form_update_objet.nombre_objet_update_wtf.data = data_objet["nombre_objet"]

    except Exception as Exception_objet_update_wtf:
        raise ExceptionobjetUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{objet_update_wtf.__name__} ; "
                                     f"{Exception_objet_update_wtf}")

    return render_template("objet/objet_update_wtf.html", form_update_objet=form_update_objet)


"""Effacer(delete) un objet qui a été sélectionné dans le formulaire "objet_objet_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /objet_delete
    
Test : ex. cliquer sur le menu "objet" puis cliquer sur le bouton "DELETE" d'un "objet"
    
Paramètres : sans

Remarque :  Dans le champ "nom_objet_delete_wtf" du formulaire "objet/objet_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/objet_delete", methods=['GET', 'POST'])
def objet_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_objet_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_objet"
    id_objet_delete = request.values['id_objet_btn_delete_html']

    # Objet formulaire pour effacer le objet sélectionné.
    form_delete_objet = FormWTFDeleteobjet()
    try:
        # Si on clique sur "ANNULER", afficher tous les objet.
        if form_delete_objet.submit_btn_annuler.data:
            return redirect(url_for("objet_objet_afficher", id_objet_sel=0))

        if form_delete_objet.submit_btn_conf_del_objet.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "objet/objet_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_objet_delete = session['data_objet_delete']
            print("data_objet_delete ", data_objet_delete)

            flash(f"Effacer le objet de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_objet.submit_btn_del_objet.data:
            valeur_delete_dictionnaire = {"value_id_objet": id_objet_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_objet_genre = """DELETE FROM t_genre_objet WHERE fk_objet = %(value_id_objet)s"""
            str_sql_delete_objet = """DELETE FROM t_objet WHERE id_objet = %(value_id_objet)s"""
            # Manière brutale d'effacer d'abord la "fk_objet", même si elle n'existe pas dans la "t_genre_objet"
            # Ensuite on peut effacer le objet vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_objet"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_objet_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_objet, valeur_delete_dictionnaire)

            flash(f"objet définitivement effacé !!", "success")
            print(f"objet définitivement effacé !!")

            # afficher les données
            return redirect(url_for('objet_objet_afficher', id_objet_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_objet": id_objet_delete}
            print(id_objet_delete, type(id_objet_delete))

            # Requête qui affiche le objet qui doit être efffacé.
            str_sql_objet_objet_delete = """SELECT * FROM t_objet WHERE id_objet = %(value_id_objet)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_objet_objet_delete, valeur_select_dictionnaire)
                data_objet_delete = mydb_conn.fetchall()
                print("data_objet_delete...", data_objet_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "objet/objet_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_objet_delete'] = data_objet_delete

            # Le bouton pour l'action "DELETE" dans le form. "objet_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_objet_delete_wtf:
        raise ExceptionobjetDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{objet_delete_wtf.__name__} ; "
                                     f"{Exception_objet_delete_wtf}")

    return render_template("objet/objet_delete_wtf.html",
                           form_delete_objet=form_delete_objet,
                           btn_submit_del=btn_submit_del,
                           data_objet_del=data_objet_delete
                           )
