"""
    Fichier : gestion_adresses_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouteradresse(FlaskForm):
    """
        Dans le formulaire "adresses_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    ville_adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ville_adresse_wtf = StringField("Clavioter la ville ", validators=[Length(min=2, max=200, message="min 2 max 200")
                                                                   ])
    batiment_adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    batiment_adresse_wtf = StringField("Clavioter le Batiment ",
                                              validators=[Length(min=2, max=200, message="min 2 max 200")
                                                          ])

    personne_adresse_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    personne_adresse_wtf = StringField("Clavioter le adresse ",
                                              validators=[Length(min=2, max=200, message="min 2 max 200")
                                                          ])
    submit = SubmitField("Enregistrer adresse")


class FormWTFUpdateadresse(FlaskForm):
    """
        Dans le formulaire "adresse_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    ville_adresse_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ville_adresse_update_wtf = StringField("Clavioter la ville ", validators=[Length(min=2, max=200, message="min 2 max 200")
                                                                          ])

    batiment_adresse_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    batiment_adresse_update_wtf = StringField("Clavioter le Batiment ",
                                         validators=[Length(min=2, max=200, message="min 2 max 200")
                                                     ])

    personne_adresse_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    personne_adresse_update_wtf = StringField("Clavioter le adresse ",
                                         validators=[Length(min=2, max=200, message="min 2 max 200")
                                                     ])
    submit = SubmitField("Update adresse")


class FormWTFDeleteadresse(FlaskForm):
    """
        Dans le formulaire "adresse_delete_wtf.html"

        nom_adresse_delete_wtf : Champ qui reçoit la valeur du adresse, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "adresse".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_fournisseur".
    """

    ville_adresse_delete_wtf = StringField("Effacer cette adresse")
    submit_btn_del = SubmitField("Effacer adresse")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
