"""Gestion des "routes" FLASK et des données pour les personne.
Fichier : gestion_personne_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.personne.gestion_personne_wtf_forms import FormWTFAjouterpersonne
from APP_FILMS_164.personne.gestion_personne_wtf_forms import FormWTFDeletepersonne
from APP_FILMS_164.personne.gestion_personne_wtf_forms import FormWTFUpdatepersonne

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /personne_afficher
    
    Test : ex : http://127.0.0.1:5005/personne_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_personne_sel = 0 >> tous les personne.
                id_personne_sel = "n" affiche le personne dont l'id est "n"
"""


@app.route("/personne_afficher/<string:order_by>/<int:id_personne_sel>", methods=['GET', 'POST'])
def personne_afficher(order_by, id_personne_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_personne_sel == 0:
                    strsql_personne_afficher = """SELECT id_personne, 
                    nom_personne,
                    prenom_personne, moral_personne,
                    physique_personne 
                    FROM t_personne ORDER BY id_personne ASC"""


                    mc_afficher.execute(strsql_personne_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_personne"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les villes d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du personne sélectionné avec un ville de variable
                    valeur_id_personne_selected_dictionnaire = {"value_id_personne_selected": id_personne_sel}
                    strsql_personne_afficher = """SELECT id_personne, nom_personne, prenom_personne, moral_personne, physique_personne  FROM t_personne WHERE id_personne = %(value_id_personne_selected)s"""

                    mc_afficher.execute(strsql_personne_afficher, valeur_id_personne_selected_dictionnaire)
                else:
                    strsql_personne_afficher = """SELECT id_personne, nom_personne, prenom_personne, moral_personne, physique_personne   FROM t_personne ORDER BY id_personne DESC"""

                    mc_afficher.execute(strsql_personne_afficher)

                data_personne = mc_afficher.fetchall()

                print("data_personne ", data_personne, " Type : ", type(data_personne))

                # Différencier les messages si la table est vide.
                if not data_personne and id_personne_sel == 0:
                    flash("""La table "t_personne" est vide. !!""", "warning")
                elif not data_personne and id_personne_sel > 0:
                    # Si l'utilisateur change l'id_personne dans l'URL et que le personne n'existe pas,
                    flash(f"Le personne demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_personne" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données personne affichés !!", "success")

        except Exception as Exception_personne_afficher:
            raise ExceptionpersonneAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{personne_afficher.__name__} ; "
                                          f"{Exception_personne_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("personne/personne_afficher.html", data=data_personne)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /personne_ajouter
    
    Test : ex : http://127.0.0.1:5005/personne_ajouter
    
    Paramètres : sans
    
    But : Ajouter un personne pour un personne
    
    Remarque :  Dans le champ "name_personne_html" du formulaire "personne/personne_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/personne_ajouter", methods=['GET', 'POST'])
def personne_ajouter_wtf():
    form = FormWTFAjouterpersonne()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_personne_wtf = form.nom_personne_wtf.data
                prenom_personne_wtf = form.prenom_personne_wtf.data
                moral_personne_wtf = form.moral_personne_wtf.data
                physique_personne_wtf = form.physique_personne_wtf.data
                valeurs_insertion_dictionnaire = {"value_nom_personne": nom_personne_wtf,
                                                  "value_prenom_personne" : prenom_personne_wtf,
                                                  "value_moral_personne": moral_personne_wtf,
                                                  "value_physique_personne": physique_personne_wtf
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)



               #strsql_insert_personne = """INSERT INTO t_personne (id_personne,prenom_personne,prenom_personne) VALUES (NULL,%(value_prenom_personne)s,%(value_batiment_personne)s,%(value_prenom_personne)s)"""
                strsql_insert_personne = """INSERT INTO `t_personne` (`id_personne`, `nom_personne`, `prenom_personne`,`moral_personne`, `physique_personne`) VALUES (NULL, %(value_nom_personne)s, %(value_prenom_personne)s, %(value_moral_personne)s, %(value_physique_personne)s);"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_personne, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('personne_afficher', order_by='DESC', id_personne_sel=0))

        except Exception as Exception_personne_ajouter_wtf:
            raise ExceptionpersonneAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{personne_ajouter_wtf.__name__} ; "
                                            f"{Exception_personne_ajouter_wtf}")

    return render_template("personne/personne_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /personne_update
    
    Test : ex cliquer sur le menu "personne" puis cliquer sur le bouton "EDIT" d'un "personne"
    
    Paramètres : sans
    
    But : Editer(update) un personne qui a été sélectionné dans le formulaire "personne_afficher.html"
    
    Remarque :  Dans le champ "prenom_personne_update_wtf" du formulaire "personne/personne_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""

@app.route("/personne_update", methods=['GET', 'POST'])
def personne_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_personne"
    id_personne_update = request.values['id_personne_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatepersonne()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "personne_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_personne_update = form_update.nom_personne_update_wtf.data
          #  name_personne_update = name_personne_update.lower()
            prenom_personne_update = form_update.prenom_personne_update_wtf.data
            moral_personne_update = form_update.moral_personne_update_wtf.data
            physique_personne_update = form_update.physique_personne_update_wtf.data

            valeur_update_dictionnaire = {"value_id_personne": id_personne_update,
                                          "value_nom_personne": nom_personne_update,
                                          "value_prenom_personne": prenom_personne_update,
                                          "value_moral_personne": moral_personne_update,
                                          "value_physique_personne": physique_personne_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_villepersonne = """UPDATE t_personne SET nom_personne = %(value_nom_personne)s, prenom_personne = %(value_prenom_personne)s, moral_personne = %(value_moral_personne)s, physique_personne = %(value_physique_personne)s WHERE id_personne = %(value_id_personne)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_villepersonne, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_personne_update"
            return redirect(url_for('personne_afficher', order_by="ASC", id_personne_sel=id_personne_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_personne" et "prenom_personne" de la "t_personne"
            str_sql_id_personne = "SELECT id_personne, nom_personne,  prenom_personne, moral_personne,  physique_personne FROM t_personne " \
                               "WHERE id_personne = %(value_id_personne)s"
            valeur_select_dictionnaire = {"value_id_personne": id_personne_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personne, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "ville personne" pour l'UPDATE
            data_prenom_personne = mybd_conn.fetchone()
            print("data_prenom_personne ", data_prenom_personne, " type ", type(data_prenom_personne), " personne ",
                  data_prenom_personne["prenom_personne"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "personne_update_wtf.html"
            form_update.nom_personne_update_wtf.data = data_prenom_personne["nom_personne"]
            form_update.prenom_personne_update_wtf.data = data_prenom_personne["prenom_personne"]
            form_update.moral_personne_update_wtf.data = data_prenom_personne["moral_personne"]
            form_update.physique_personne_update_wtf.data = data_prenom_personne["physique_personne"]

    except Exception as Exception_personne_update_wtf:
        raise ExceptionpersonneUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personne_update_wtf.__name__} ; "
                                      f"{Exception_personne_update_wtf}")

    return render_template("personne/personne_update_wtf.html", form_update=form_update)



"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /personne_delete
    
    Test : ex. cliquer sur le menu "personne" puis cliquer sur le bouton "DELETE" d'un "personne"
    
    Paramètres : sans
    
    But : Effacer(delete) un personne qui a été sélectionné dans le formulaire "personne_afficher.html"
    
    Remarque :  Dans le champ "prenom_personne_delete_wtf" du formulaire "personne/personne_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""

@app.route("/personne_delete", methods=['GET', 'POST'])
def personne_delete_wtf():

    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_personne"
    id_personne_delete = request.values['id_personne_btn_delete_html']

    # Objet formulaire pour effacer le personne sélectionné.
    form_delete = FormWTFDeletepersonne()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("personne_afficher", order_by="ASC", id_personne_sel=0))






            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_personne": id_personne_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_id_personne = """DELETE FROM t_personne WHERE id_personne = %(value_id_personne)s"""
                # Manière brutale d'effacer d'abord la "fk_personne", même si elle n'existe pas dans la "t_personne_film"
                # Ensuite on peut effacer le personne vu qu'il n'est plus "lié" (INNODB) dans la "t_personne_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_id_personne, valeur_delete_dictionnaire)
                flash(f"personne définitivement effacé !!", "success")
                print(f"personne définitivement effacé !!")

                # afficher les données
                return redirect(url_for('personne_afficher', order_by="ASC", id_personne_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_personne": id_personne_delete}
            print(id_personne_delete, type(id_personne_delete))

            # Requête qui affiche tous les films_personne qui ont le personne que l'utilisateur veut effacer

            with DBconnection() as mydb_conn:


                # Opération sur la BD pour récupérer "id_personne" et "prenom_personne" de la "t_personne"
                str_sql_id_personne = "SELECT id_personne, nom_personne FROM t_personne WHERE id_personne = %(value_id_personne)s"

                mydb_conn.execute(str_sql_id_personne, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "ville personne" pour l'action DELETE
                data_nom_personne = mydb_conn.fetchone()
                print("data_nom_personne ", data_nom_personne, " type ", type(data_nom_personne), " personne ",
                      data_nom_personne["nom_personne"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "personne_delete_wtf.html"
            form_delete.nom_personne_delete_wtf.data = data_nom_personne["nom_personne"]

            # Le bouton pour l'action "DELETE" dans le form. "personne_delete_wtf.html" est caché.
            btn_submit_del = True

    except Exception as Exception_personne_delete_wtf:
        raise ExceptionpersonneDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personne_delete_wtf.__name__} ; "
                                      f"{Exception_personne_delete_wtf}")

    return render_template("personne/personne_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)
