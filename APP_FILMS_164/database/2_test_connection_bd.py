"""Démonstration d'envoi d'une requête SQL à la BD
Fichier : 2_test_connection_bd.py
Auteur : OM 2021.03.03
"""

from APP_FILMS_164.database.database_tools import DBconnection

try:
    """
        Une seule requête pour montrer la récupération des données de la BD en MySql.
    """
    strsql_fournisseur_afficher = """SELECT id_fournisseur, nom_fournisseur, objet_fournisseur FROM t_fournisseur ORDER BY id_fournisseur ASC"""

    with DBconnection() as db:
        db.execute(strsql_fournisseur_afficher)
        result = db.fetchall()
        print("data_fournisseur ", result, " Type : ", type(result))


except Exception as erreur:
    # print(f"2547821146 Connection à la BD Impossible ! {type(erreur)} args {erreur.args}")
    print(f"2547821146 Test connection BD !"
          f"{__name__,erreur} , "
          f"{repr(erreur)}, "
          f"{type(erreur)}")
