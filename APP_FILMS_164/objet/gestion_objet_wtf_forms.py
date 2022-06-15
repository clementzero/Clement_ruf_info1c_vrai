"""Gestion des formulaires avec WTF pour les objets
Fichier : gestion_objets_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.widgets import TextArea


class FormWTFAjouterobjet(FlaskForm):
    """
        Dans le formulaire "fournisseur_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_objet_regexp = ""
    nom_objet_wtf = StringField("Nom de l'objet ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                               ])
    num_serie_objet_regexp = ""
    num_serie_objet_wtf = StringField("Numero de serie de l'objet ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                               ])
    description_objet_regexp = ""
    description_objet_wtf = StringField("description de l'objet ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                               ])
    creation_objet_regexp = ""
    creation_objet_wtf = StringField("date de creation ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                               ])
    nombre_objet_regexp = ""
    nombre_objet_wtf = StringField("Nombre d'objet ", validators=[Length(min=2, max=2000, message="min 2 max 20")
                                                               ])
    submit = SubmitField("Enregistrer objet")


class FormWTFUpdateobjet(FlaskForm):
    """
        Dans le formulaire "objet_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_objet_update_wtf = StringField("Clavioter le nom", widget=TextArea())
    num_serie_objet_update_wtf = StringField("Clavioter le numero de serie", widget=TextArea())
    description_objet_update_wtf = StringField("Clavioter la description", widget=TextArea())
    creation_objet_update_wtf = StringField("Clavioter la date de création", widget=TextArea())
    nombre_objet_update_wtf = StringField("Clavioter le nombre d'objet", widget=TextArea())
    
    submit = SubmitField("Update objet")


class FormWTFDeleteobjet(FlaskForm):
    """
        Dans le formulaire "objet_delete_wtf.html"

        nom_objet_delete_wtf : Champ qui reçoit la valeur du objet, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "objet".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_objet".
    """
    nom_objet_delete_wtf = StringField("Effacer ce objet")
    submit_btn_del_objet = SubmitField("Effacer objet")
    submit_btn_conf_del_objet = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
