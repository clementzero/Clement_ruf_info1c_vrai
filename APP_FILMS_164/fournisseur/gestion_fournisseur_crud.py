"""Gestion des "routes" FLASK et des données pour les fournisseur.
Fichier : gestion_fournisseur_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import url_for
from flask import session

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.fournisseur.gestion_fournisseur_wtf_forms import FormWTFAjouterfournisseur
from APP_FILMS_164.fournisseur.gestion_fournisseur_wtf_forms import FormWTFDeletefournisseur
from APP_FILMS_164.fournisseur.gestion_fournisseur_wtf_forms import FormWTFUpdatefournisseur

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /fournisseur_afficher
    
    Test : ex : http://127.0.0.1:5005/fournisseur_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_fournisseur_sel = 0 >> tous les fournisseur.
                id_fournisseur_sel = "n" affiche le fournisseur dont l'id est "n"
"""


@app.route("/fournisseur_afficher/<string:order_by>/<int:id_fournisseur_sel>", methods=['GET', 'POST'])
def fournisseur_afficher(order_by, id_fournisseur_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_fournisseur_sel == 0:
                    strsql_fournisseur_afficher = """SELECT id_fournisseur, nom_fournisseur, objet_fournisseur FROM t_fournisseur ORDER BY id_fournisseur ASC"""
                    mc_afficher.execute(strsql_fournisseur_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_fournisseur"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du fournisseur sélectionné avec un nom de variable
                    valeur_id_fournisseur_selected_dictionnaire = {"value_id_fournisseur_selected": id_fournisseur_sel}
                    strsql_fournisseur_afficher = """SELECT id_fournisseur, nom_fournisseur, objet_fournisseur  FROM t_fournisseur WHERE id_fournisseur = %(value_id_fournisseur_selected)s"""

                    mc_afficher.execute(strsql_fournisseur_afficher, valeur_id_fournisseur_selected_dictionnaire)
                else:
                    strsql_fournisseur_afficher = """SELECT id_fournisseur, nom_fournisseur, objet_fournisseur  FROM t_fournisseur ORDER BY id_fournisseur DESC"""

                    mc_afficher.execute(strsql_fournisseur_afficher)

                data_fournisseur = mc_afficher.fetchall()

                print("data_fournisseur ", data_fournisseur, " Type : ", type(data_fournisseur))

                # Différencier les messages si la table est vide.
                if not data_fournisseur and id_fournisseur_sel == 0:
                    flash("""La table "t_fournisseur" est vide. !!""", "warning")
                elif not data_fournisseur and id_fournisseur_sel > 0:
                    # Si l'utilisateur change l'id_fournisseur dans l'URL et que le fournisseur n'existe pas,
                    flash(f"Le fournisseur demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_fournisseur" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données fournisseur affichés !!", "success")

        except Exception as Exception_fournisseur_afficher:
            raise ExceptionfournisseurAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{fournisseur_afficher.__name__} ; "
                                          f"{Exception_fournisseur_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("fournisseur/fournisseur_afficher.html", data=data_fournisseur)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /fournisseur_ajouter
    
    Test : ex : http://127.0.0.1:5005/fournisseur_ajouter
    
    Paramètres : sans
    
    But : Ajouter un fournisseur pour un objet
    
    Remarque :  Dans le champ "name_fournisseur_html" du formulaire "fournisseur/fournisseur_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/fournisseur_ajouter", methods=['GET', 'POST'])
def fournisseur_ajouter_wtf():
    form = FormWTFAjouterfournisseur()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_fournisseur_wtf = form.nom_fournisseur_wtf.data
                objet_fournisseur_wtf = form.objet_fournisseur_wtf.data
                valeurs_insertion_dictionnaire = {"value_nom_fournisseur": nom_fournisseur_wtf,
                                                  "value_objet_fournisseur" : objet_fournisseur_wtf
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)



               #strsql_insert_fournisseur = """INSERT INTO t_fournisseur (id_fournisseur,nom_fournisseur,objet_fournisseur) VALUES (NULL,%(value_nom_fournisseur)s,%(value_batiment_fournisseur)s,%(value_objet_fournisseur)s)"""
                strsql_insert_fournisseur = """INSERT INTO `t_fournisseur` (`id_fournisseur`, `nom_fournisseur`, `objet_fournisseur`) VALUES (NULL, %(value_nom_fournisseur)s, %(value_objet_fournisseur)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_fournisseur, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('fournisseur_afficher', order_by='DESC', id_fournisseur_sel=0))

        except Exception as Exception_fournisseur_ajouter_wtf:
            raise ExceptionfournisseurAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{fournisseur_ajouter_wtf.__name__} ; "
                                            f"{Exception_fournisseur_ajouter_wtf}")

    return render_template("fournisseur/fournisseur_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /fournisseur_update
    
    Test : ex cliquer sur le menu "fournisseur" puis cliquer sur le bouton "EDIT" d'un "fournisseur"
    
    Paramètres : sans
    
    But : Editer(update) un fournisseur qui a été sélectionné dans le formulaire "fournisseur_afficher.html"
    
    Remarque :  Dans le champ "nom_fournisseur_update_wtf" du formulaire "fournisseur/fournisseur_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/fournisseur_update", methods=['GET', 'POST'])
def fournisseur_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_fournisseur"
    id_fournisseur_update = request.values['id_fournisseur_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatefournisseur()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "fournisseur_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_fournisseur_update = form_update.nom_fournisseur_update_wtf.data
          #  name_fournisseur_update = name_fournisseur_update.lower()
            objet_fournisseur_update = form_update.objet_fournisseur_update_wtf.data

            valeur_update_dictionnaire = {"value_id_fournisseur": id_fournisseur_update,
                                          "value_nom_fournisseur": nom_fournisseur_update,
                                          "value_objet_fournisseur": objet_fournisseur_update,
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_villefournisseur = """UPDATE t_fournisseur SET nom_fournisseur = %(value_nom_fournisseur)s, objet_fournisseur = %(value_objet_fournisseur)s WHERE id_fournisseur = %(value_id_fournisseur)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_villefournisseur, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_fournisseur_update"
            return redirect(url_for('fournisseur_afficher', order_by="ASC", id_fournisseur_sel=id_fournisseur_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_fournisseur" et "nom_fournisseur" de la "t_fournisseur"
            str_sql_id_fournisseur = "SELECT id_fournisseur, nom_fournisseur,  objet_fournisseur FROM t_fournisseur " \
                               "WHERE id_fournisseur = %(value_id_fournisseur)s"
            valeur_select_dictionnaire = {"value_id_fournisseur": id_fournisseur_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_fournisseur, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "ville fournisseur" pour l'UPDATE
            data_nom_fournisseur = mybd_conn.fetchone()
            print("data_nom_fournisseur ", data_nom_fournisseur, " type ", type(data_nom_fournisseur), " fournisseur ",
                  data_nom_fournisseur["nom_fournisseur"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "fournisseur_update_wtf.html"
            form_update.nom_fournisseur_update_wtf.data = data_nom_fournisseur["nom_fournisseur"]
            form_update.objet_fournisseur_update_wtf.data = data_nom_fournisseur["objet_fournisseur"]

    except Exception as Exception_fournisseur_update_wtf:
        raise ExceptionfournisseurUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{fournisseur_update_wtf.__name__} ; "
                                      f"{Exception_fournisseur_update_wtf}")

    return render_template("fournisseur/fournisseur_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /fournisseur_delete
    
    Test : ex. cliquer sur le menu "fournisseur" puis cliquer sur le bouton "DELETE" d'un "fournisseur"
    
    Paramètres : sans
    
    But : Effacer(delete) un fournisseur qui a été sélectionné dans le formulaire "fournisseur_afficher.html"
    
    Remarque :  Dans le champ "nom_fournisseur_delete_wtf" du formulaire "fournisseur/fournisseur_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/fournisseur_delete", methods=['GET', 'POST'])
def fournisseur_delete_wtf():

    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_fournisseur"
    id_fournisseur_delete = request.values['id_fournisseur_btn_delete_html']

    # Objet formulaire pour effacer le fournisseur sélectionné.
    form_delete = FormWTFDeletefournisseur()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("fournisseur_afficher", order_by="ASC", id_fournisseur_sel=0))






            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_fournisseur": id_fournisseur_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_id_fournisseur = """DELETE FROM t_fournisseur WHERE id_fournisseur = %(value_id_fournisseur)s"""
                # Manière brutale d'effacer d'abord la "fk_fournisseur", même si elle n'existe pas dans la "t_fournisseur_film"
                # Ensuite on peut effacer le fournisseur vu qu'il n'est plus "lié" (INNODB) dans la "t_fournisseur_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_id_fournisseur, valeur_delete_dictionnaire)
                flash(f"fournisseur définitivement effacé !!", "success")
                print(f"fournisseur définitivement effacé !!")

                # afficher les données
                return redirect(url_for('fournisseur_afficher', order_by="ASC", id_fournisseur_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_fournisseur": id_fournisseur_delete}
            print(id_fournisseur_delete, type(id_fournisseur_delete))

            # Requête qui affiche tous les films_fournisseur qui ont le fournisseur que l'utilisateur veut effacer

            with DBconnection() as mydb_conn:


                # Opération sur la BD pour récupérer "id_fournisseur" et "nom_fournisseur" de la "t_fournisseur"
                str_sql_id_fournisseur = "SELECT id_fournisseur, nom_fournisseur FROM t_fournisseur WHERE id_fournisseur = %(value_id_fournisseur)s"

                mydb_conn.execute(str_sql_id_fournisseur, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "ville fournisseur" pour l'action DELETE
                data_nom_fournisseur = mydb_conn.fetchone()
                print("data_nom_fournisseur ", data_nom_fournisseur, " type ", type(data_nom_fournisseur), " fournisseur ",
                      data_nom_fournisseur["nom_fournisseur"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "fournisseur_delete_wtf.html"
            form_delete.nom_fournisseur_delete_wtf.data = data_nom_fournisseur["nom_fournisseur"]

            # Le bouton pour l'action "DELETE" dans le form. "fournisseur_delete_wtf.html" est caché.
            btn_submit_del = True

    except Exception as Exception_fournisseur_delete_wtf:
        raise ExceptionfournisseurDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{fournisseur_delete_wtf.__name__} ; "
                                      f"{Exception_fournisseur_delete_wtf}")

    return render_template("fournisseur/fournisseur_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)
