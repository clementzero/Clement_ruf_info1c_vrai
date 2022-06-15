"""
    Fichier : gestion_mails_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjoutermail(FlaskForm):
    """
        Dans le formulaire "mails_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    mail_mail_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    mail_mail_wtf = StringField("Clavioter le mail ", validators=[Length(min=2, max=200, message="min 2 max 200")
                                                                   ])

    personne_mail_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    personne_mail_wtf = StringField("Clavioter la peronne ",
                                              validators=[Length(min=2, max=200, message="min 2 max 200")
                                                          ])
    submit = SubmitField("Enregistrer mail")


class FormWTFUpdatemail(FlaskForm):
    """
        Dans le formulaire "mail_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    mail_mail_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    mail_mail_update_wtf = StringField("Clavioter la ville ", validators=[Length(min=2, max=200, message="min 2 max 200")
                                                                          ])

    personne_mail_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    personne_mail_update_wtf = StringField("Clavioter le mail ",
                                         validators=[Length(min=2, max=200, message="min 2 max 200")
                                                     ])
    submit = SubmitField("Update mail")


class FormWTFDeletemail(FlaskForm):
    """
        Dans le formulaire "mail_delete_wtf.html"

        nom_mail_delete_wtf : Champ qui reçoit la valeur du mail, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "mail".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_fournisseur".
    """

    mail_mail_delete_wtf = StringField("Effacer cette mail")
    submit_btn_del = SubmitField("Effacer mail")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
