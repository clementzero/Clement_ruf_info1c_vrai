"""
    Fichier : gestion_fournisseurs_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterfournisseur(FlaskForm):
    """
        Dans le formulaire "fournisseurs_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_fournisseur_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_fournisseur_wtf = StringField("Clavioter le fournisseur ", validators=[Length(min=2, max=200, message="min 2 max 20")
                                                                   ])
    objet_fournisseur_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    objet_fournisseur_wtf = StringField("Clavioter l'objet ",
                                      validators=[Length(min=2, max=200, message="min 2 max 20")
                                                  ])
    submit = SubmitField("Enregistrer fournisseur")


class FormWTFUpdatefournisseur(FlaskForm):
    """
        Dans le formulaire "fournisseur_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_fournisseur_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_fournisseur_update_wtf = StringField("Clavioter le fournisseur ", validators=[Length(min=2, max=200, message="min 2 max 20")
                                                                          ])
    objet_fournisseur_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    objet_fournisseur_update_wtf = StringField("Clavioter l'objet ", validators=[Length(min=2, max=200, message="min 2 max 20")
                                                                          ])

    submit = SubmitField("Update fournisseur")


class FormWTFDeletefournisseur(FlaskForm):
    """
        Dans le formulaire "fournisseur_delete_wtf.html"

        nom_fournisseur_delete_wtf : Champ qui reçoit la valeur du fournisseur, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "fournisseur".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_fournisseur".
    """
    nom_fournisseur_delete_wtf = StringField("Effacer ce fournisseur")
    submit_btn_del = SubmitField("Effacer fournisseur")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
