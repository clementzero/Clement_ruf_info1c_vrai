"""
    Fichier : gestion_personnes_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterpersonne(FlaskForm):
    """
        Dans le formulaire "personnes_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_personne_wtf = StringField("Clavioter le nom de la personne ", validators=[Length(min=2, max=200, message="min 2 max 200")
                                                                   ])

    prenom_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_personne_wtf = StringField("Clavioter le prenom de la peronne ",
                                              validators=[Length(min=2, max=200, message="min 2 max 200")
                                                          ])
    physique_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    physique_personne_wtf = StringField("Clavioter le satut de la personne ",
                                   validators=[Length(min=2, max=200, message="min 2 max 200")
                                               ])

    moral_personne_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    moral_personne_wtf = StringField("Clavioter l'entreprise ",
                                      validators=[Length(min=2, max=200, message="min 2 max 200")
                                                  ])
    submit = SubmitField("Enregistrer personne")


class FormWTFUpdatepersonne(FlaskForm):
    """
        Dans le formulaire "personne_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_personne_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_personne_update_wtf = StringField("Clavioter le nom de la personne ",
                                   validators=[Length(min=2, max=200, message="min 2 max 200")
                                               ])

    prenom_personne_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    prenom_personne_update_wtf = StringField("Clavioter le prenom de la peronne ",
                                      validators=[Length(min=2, max=200, message="min 2 max 200")
                                                  ])
    physique_personne_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    physique_personne_update_wtf = StringField("Clavioter le satut de la personne ",
                                        validators=[Length(min=2, max=200, message="min 2 max 200")
                                                    ])

    moral_personne_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    moral_personne_update_wtf = StringField("Clavioter l'entreprise ",
                                     validators=[Length(min=2, max=200, message="min 2 max 200")
                                                 ])
    submit = SubmitField("Update personne")


class FormWTFDeletepersonne(FlaskForm):
    """
        Dans le formulaire "personne_delete_wtf.html"

        nom_personne_delete_wtf : Champ qui reçoit la valeur du personne, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "personne".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_fournisseur".
    """

    nom_personne_delete_wtf = StringField("Effacer cette personne")
    submit_btn_del = SubmitField("Effacer personne")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
