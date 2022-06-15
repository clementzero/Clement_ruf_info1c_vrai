"""
    Fichier : gestion_tels_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormWTFAjoutertel(FlaskForm):
    """
        Dans le formulaire "tels_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    numero_tel_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    numero_tel_wtf = StringField("Clavioter le numero ", validators=[Length(min=2, max=200, message="min 2 max 200")

                                                                   ])

    prenom_tel_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_tel_wtf = StringField("Clavioter le prenom ", validators=[Length(min=2, max=200, message="min 2 max 200")
                                                                   ])
    submit = SubmitField("Enregistrer tel")


class FormWTFUpdatetel(FlaskForm):
    """
        Dans le formulaire "tel_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    numero_tel_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    numero_tel_update_wtf = StringField("Clavioter la ville ",
                                       validators=[Length(min=2, max=200, message="min 2 max 200")
                                                   ])

    prenom_tel_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_tel_update_wtf = StringField("Clavioter le tel ",
                                           validators=[Length(min=2, max=200, message="min 2 max 200")
                                                       ])
    submit = SubmitField("Update tel")


class FormWTFDeletetel(FlaskForm):
    """
        Dans le formulaire "tel_delete_wtf.html"

        nom_tel_delete_wtf : Champ qui reçoit la valeur du tel, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "tel".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_fournisseur".
    """
    numero_tel_delete_wtf = StringField("Effacer cette tel")
    submit_btn_del = SubmitField("Effacer tel")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
