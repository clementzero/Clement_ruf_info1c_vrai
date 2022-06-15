"""
    Fichier : gestion_objet_fournisseur_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les objet et les fournisseur.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *

"""
    Nom : objet_fournisseur_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /objet_fournisseur_afficher
    
    But : Afficher les objet avec les fournisseur associés pour chaque objet.
    
    Paramètres : id_fournisseur_sel = 0 >> tous les objet.
                 id_fournisseur_sel = "n" affiche le objet dont l'id est "n"
                 
"""


@app.route("/objet_fournisseur_afficher/<int:id_objet_sel>", methods=['GET', 'POST'])
def objet_fournisseur_afficher(id_objet_sel):
    print(" objet_fournisseur_afficher id_objet_sel ", id_objet_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_fournisseur_objet_afficher_data = """SELECT id_objet, nom_objet, num_serie_objet, description_objet, creation_objet, nombre_objet,
                                                            GROUP_CONCAT(nom_fournisseur) as fournisseurobjet FROM t_acheter_marchandise
                                                            RIGHT JOIN t_objet ON t_objet.id_objet = t_acheter_marchandise.fk_objet
                                                            LEFT JOIN t_fournisseur ON t_fournisseur.id_fournisseur = t_acheter_marchandise.fk_fournisseur
                                                            GROUP BY id_objet"""
                if id_objet_sel == 0:
                    # le paramètre 0 permet d'afficher tous les objet
                    # Sinon le paramètre représente la valeur de l'id du objet
                    mc_afficher.execute(strsql_fournisseur_objet_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du objet sélectionné avec un nom de variable
                    valeur_id_objet_selected_dictionnaire = {"value_id_objet_selected": id_objet_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_fournisseur_objet_afficher_data += """ HAVING id_objet= %(value_id_objet_selected)s"""

                    mc_afficher.execute(strsql_fournisseur_objet_afficher_data, valeur_id_objet_selected_dictionnaire)

                # Récupère les données de la requête.
                data_fournisseur_objet_afficher = mc_afficher.fetchall()
                print("data_fournisseur ", data_fournisseur_objet_afficher, " Type : ", type(data_fournisseur_objet_afficher))

                # Différencier les messages.
                if not data_fournisseur_objet_afficher and id_objet_sel == 0:
                    flash("""La table "t_objet" est vide. !""", "warning")
                elif not data_fournisseur_objet_afficher and id_objet_sel > 0:
                    # Si l'utilisateur change l'id_objet dans l'URL et qu'il ne correspond à aucun objet
                    flash(f"Le objet {id_objet_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données objet et fournisseur affichés !!", "success")

        except Exception as Exception_objet_fournisseur_afficher:
            raise ExceptionobjetfournisseurAfficher(f"fichier : {Path(__file__).name}  ;  {objet_fournisseur_afficher.__name__} ;"
                                               f"{Exception_objet_fournisseur_afficher}")

    print("objet_fournisseur_afficher  ", data_fournisseur_objet_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("objet_fournisseur/objet_fournisseur_afficher.html", data=data_fournisseur_objet_afficher)


"""
    nom: edit_acheter_marchandise_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les fournisseur du objet sélectionné par le bouton "MODIFIER" de "objet_fournisseur_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les fournisseur contenus dans la "t_fournisseur".
    2) Les fournisseur attribués au objet selectionné.
    3) Les fournisseur non-attribués au objet sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_acheter_marchandise_selected", methods=['GET', 'POST'])
def edit_acheter_marchandise_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_fournisseur_afficher = """SELECT id_fournisseur, nom_fournisseur FROM t_fournisseur ORDER BY id_fournisseur ASC"""
                mc_afficher.execute(strsql_fournisseur_afficher)
            data_fournisseur_all = mc_afficher.fetchall()
            print("dans edit_acheter_marchandise_selected ---> data_fournisseur_all", data_fournisseur_all)

            # Récupère la valeur de "id_objet" du formulaire html "objet_fournisseur_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_objet"
            # grâce à la variable "id_acheter_marchandise_edit_html" dans le fichier "objet_fournisseur_afficher.html"
            # href="{{ url_for('edit_acheter_marchandise_selected', id_acheter_marchandise_edit_html=row.id_objet) }}"
            id_acheter_marchandise_edit = request.values['id_acheter_marchandise_edit_html']

            # Mémorise l'id du objet dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_acheter_marchandise_edit'] = id_acheter_marchandise_edit

            # Constitution d'un dictionnaire pour associer l'id du objet sélectionné avec un nom de variable
            valeur_id_objet_selected_dictionnaire = {"value_id_objet_selected": id_acheter_marchandise_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction fournisseur_objet_afficher_data
            # 1) Sélection du objet choisi
            # 2) Sélection des fournisseur "déjà" attribués pour le objet.
            # 3) Sélection des fournisseur "pas encore" attribués pour le objet choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "fournisseur_objet_afficher_data"
            data_fournisseur_objet_selected, data_fournisseur_objet_non_attribues, data_fournisseur_objet_attribues = \
                fournisseur_objet_afficher_data(valeur_id_objet_selected_dictionnaire)

            print(data_fournisseur_objet_selected)
            lst_data_objet_selected = [item['id_objet'] for item in data_fournisseur_objet_selected]
            print("lst_data_objet_selected  ", lst_data_objet_selected,
                  type(lst_data_objet_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les fournisseur qui ne sont pas encore sélectionnés.
            lst_data_fournisseur_objet_non_attribues = [item['id_fournisseur'] for item in data_fournisseur_objet_non_attribues]
            session['session_lst_data_fournisseur_objet_non_attribues'] = lst_data_fournisseur_objet_non_attribues
            print("lst_data_fournisseur_objet_non_attribues  ", lst_data_fournisseur_objet_non_attribues,
                  type(lst_data_fournisseur_objet_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les fournisseur qui sont déjà sélectionnés.
            lst_data_fournisseur_objet_old_attribues = [item['id_fournisseur'] for item in data_fournisseur_objet_attribues]
            session['session_lst_data_fournisseur_objet_old_attribues'] = lst_data_fournisseur_objet_old_attribues
            print("lst_data_fournisseur_objet_old_attribues  ", lst_data_fournisseur_objet_old_attribues,
                  type(lst_data_fournisseur_objet_old_attribues))

            print(" data data_fournisseur_objet_selected", data_fournisseur_objet_selected, "type ", type(data_fournisseur_objet_selected))
            print(" data data_fournisseur_objet_non_attribues ", data_fournisseur_objet_non_attribues, "type ",
                  type(data_fournisseur_objet_non_attribues))
            print(" data_fournisseur_objet_attribues ", data_fournisseur_objet_attribues, "type ",
                  type(data_fournisseur_objet_attribues))

            # Extrait les valeurs contenues dans la table "t_fournisseur", colonne "nom_fournisseur"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_fournisseur
            lst_data_fournisseur_objet_non_attribues = [item['nom_fournisseur'] for item in data_fournisseur_objet_non_attribues]
            print("lst_all_fournisseur gf_edit_acheter_marchandise_selected ", lst_data_fournisseur_objet_non_attribues,
                  type(lst_data_fournisseur_objet_non_attribues))

        except Exception as Exception_edit_acheter_marchandise_selected:
            raise ExceptionEditfournisseurobjetelected(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{edit_acheter_marchandise_selected.__name__} ; "
                                                 f"{Exception_edit_acheter_marchandise_selected}")

    return render_template("objet_fournisseur/objet_fournisseur_modifier_tags_dropbox.html",
                           data_fournisseur=data_fournisseur_all,
                           data_objet_selected=data_fournisseur_objet_selected,
                           data_fournisseur_attribues=data_fournisseur_objet_attribues,
                           data_fournisseur_non_attribues=data_fournisseur_objet_non_attribues)


"""
    nom: update_fournisseur_objet_selected

    Récupère la liste de tous les fournisseur du objet sélectionné par le bouton "MODIFIER" de "objet_fournisseur_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les fournisseur contenus dans la "t_fournisseur".
    2) Les fournisseur attribués au objet selectionné.
    3) Les fournisseur non-attribués au objet sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_fournisseur_objet_selected", methods=['GET', 'POST'])
def update_fournisseur_objet_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du objet sélectionné
            id_objet_selected = session['session_id_acheter_marchandise_edit']
            print("session['session_id_acheter_marchandise_edit'] ", session['session_id_acheter_marchandise_edit'])

            # Récupère la liste des fournisseur qui ne sont pas associés au objet sélectionné.
            old_lst_data_fournisseur_objet_non_attribues = session['session_lst_data_fournisseur_objet_non_attribues']
            print("old_lst_data_fournisseur_objet_non_attribues ", old_lst_data_fournisseur_objet_non_attribues)

            # Récupère la liste des fournisseur qui sont associés au objet sélectionné.
            old_lst_data_fournisseur_objet_attribues = session['session_lst_data_fournisseur_objet_old_attribues']
            print("old_lst_data_fournisseur_objet_old_attribues ", old_lst_data_fournisseur_objet_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme fournisseur dans le composant "tags-selector-tagselect"
            # dans le fichier "fournisseur_objet_modifier_tags_dropbox.html"
            new_lst_str_fournisseur_objet = request.form.getlist('name_select_tags')
            print("new_lst_str_fournisseur_objet ", new_lst_str_fournisseur_objet)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_acheter_marchandise_old = list(map(int, new_lst_str_fournisseur_objet))
            print("new_lst_acheter_marchandise ", new_lst_int_acheter_marchandise_old, "type new_lst_acheter_marchandise ",
                  type(new_lst_int_acheter_marchandise_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_fournisseur" qui doivent être effacés de la table intermédiaire "t_acheter_marchandise".
            lst_diff_fournisseur_delete_b = list(set(old_lst_data_fournisseur_objet_attribues) -
                                            set(new_lst_int_acheter_marchandise_old))
            print("lst_diff_fournisseur_delete_b ", lst_diff_fournisseur_delete_b)

            # Une liste de "id_fournisseur" qui doivent être ajoutés à la "t_acheter_marchandise"
            lst_diff_fournisseur_insert_a = list(
                set(new_lst_int_acheter_marchandise_old) - set(old_lst_data_fournisseur_objet_attribues))
            print("lst_diff_fournisseur_insert_a ", lst_diff_fournisseur_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_objet"/"id_objet" et "fk_fournisseur"/"id_fournisseur" dans la "t_acheter_marchandise"
            strsql_insert_acheter_marchandise = """INSERT INTO t_acheter_marchandise (id_acheter_marchandise, fk_fournisseur, fk_objet)
                                                    VALUES (NULL, %(value_fk_fournisseur)s, %(value_fk_objet)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_objet" et "id_fournisseur" dans la "t_acheter_marchandise"
            strsql_delete_fournisseur_objet = """DELETE FROM t_acheter_marchandise WHERE fk_fournisseur = %(value_fk_fournisseur)s AND fk_objet = %(value_fk_objet)s"""

            with DBconnection() as mconn_bd:
                # Pour le objet sélectionné, parcourir la liste des fournisseur à INSÉRER dans la "t_acheter_marchandise".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_fournisseur_ins in lst_diff_fournisseur_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du objet sélectionné avec un nom de variable
                    # et "id_fournisseur_ins" (l'id du fournisseur dans la liste) associé à une variable.
                    valeurs_objet_sel_fournisseur_sel_dictionnaire = {"value_fk_objet": id_objet_selected,
                                                               "value_fk_fournisseur": id_fournisseur_ins}

                    mconn_bd.execute(strsql_insert_acheter_marchandise, valeurs_objet_sel_fournisseur_sel_dictionnaire)

                # Pour le objet sélectionné, parcourir la liste des fournisseur à EFFACER dans la "t_acheter_marchandise".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_fournisseur_del in lst_diff_fournisseur_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du objet sélectionné avec un nom de variable
                    # et "id_fournisseur_del" (l'id du fournisseur dans la liste) associé à une variable.
                    valeurs_objet_sel_fournisseur_sel_dictionnaire = {"value_fk_objet": id_objet_selected,
                                                               "value_fk_fournisseur": id_fournisseur_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_fournisseur_objet, valeurs_objet_sel_fournisseur_sel_dictionnaire)

        except Exception as Exception_update_fournisseur_objet_selected:
            raise ExceptionUpdatefournisseurobjetelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_fournisseur_objet_selected.__name__} ; "
                                                   f"{Exception_update_fournisseur_objet_selected}")

    # Après cette mise à jour de la table intermédiaire "t_acheter_marchandise",
    # on affiche les objet et le(urs) fournisseur(s) associé(s).
    return redirect(url_for('objet_fournisseur_afficher', id_objet_sel=id_objet_selected))


"""
    nom: fournisseur_objet_afficher_data

    Récupère la liste de tous les fournisseur du objet sélectionné par le bouton "MODIFIER" de "objet_fournisseur_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des fournisseur, ainsi l'utilisateur voit les fournisseur à disposition

    On signale les erreurs importantes
"""


def fournisseur_objet_afficher_data(valeur_id_objet_selected_dict):
    print("valeur_id_objet_selected_dict...", valeur_id_objet_selected_dict)
    try:

        strsql_objet_selected = """SELECT id_objet, nom_objet, num_serie_objet, description_objet, creation_objet, nombre_objet, GROUP_CONCAT(id_fournisseur) as fournisseurobjet FROM t_acheter_marchandise
                                        INNER JOIN t_objet ON t_objet.id_objet = t_acheter_marchandise.fk_objet
                                        INNER JOIN t_fournisseur ON t_fournisseur.id_fournisseur = t_acheter_marchandise.fk_fournisseur
                                        WHERE id_objet = %(value_id_objet_selected)s"""

        strsql_fournisseur_objet_non_attribues = """SELECT id_fournisseur, nom_fournisseur FROM t_fournisseur WHERE id_fournisseur not in(SELECT id_fournisseur as idfournisseurobjet FROM t_acheter_marchandise
                                                    INNER JOIN t_objet ON t_objet.id_objet = t_acheter_marchandise.fk_objet
                                                    INNER JOIN t_fournisseur ON t_fournisseur.id_fournisseur = t_acheter_marchandise.fk_fournisseur
                                                    WHERE id_objet = %(value_id_objet_selected)s)"""

        strsql_fournisseur_objet_attribues = """SELECT id_objet, id_fournisseur, nom_fournisseur FROM t_acheter_marchandise
                                            INNER JOIN t_objet ON t_objet.id_objet = t_acheter_marchandise.fk_objet
                                            INNER JOIN t_fournisseur ON t_fournisseur.id_fournisseur = t_acheter_marchandise.fk_fournisseur
                                            WHERE id_objet = %(value_id_objet_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_fournisseur_objet_non_attribues, valeur_id_objet_selected_dict)
            # Récupère les données de la requête.
            data_fournisseur_objet_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("fournisseur_objet_afficher_data ----> data_fournisseur_objet_non_attribues ", data_fournisseur_objet_non_attribues,
                  " Type : ",
                  type(data_fournisseur_objet_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_objet_selected, valeur_id_objet_selected_dict)
            # Récupère les données de la requête.
            data_objet_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_objet_selected  ", data_objet_selected, " Type : ", type(data_objet_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_fournisseur_objet_attribues, valeur_id_objet_selected_dict)
            # Récupère les données de la requête.
            data_fournisseur_objet_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_fournisseur_objet_attribues ", data_fournisseur_objet_attribues, " Type : ",
                  type(data_fournisseur_objet_attribues))

            # Retourne les données des "SELECT"
            return data_objet_selected, data_fournisseur_objet_non_attribues, data_fournisseur_objet_attribues

    except Exception as Exception_fournisseur_objet_afficher_data:
        raise ExceptionfournisseurobjetAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                               f"{fournisseur_objet_afficher_data.__name__} ; "
                                               f"{Exception_fournisseur_objet_afficher_data}")
