from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre','auteur','date_parution','nombre_pages','resume','imaurl','nom',)
        labels = {
        'titre' :_('Titre'),
        'auteur' :_('Auteur'),
        'date_parution' :_('date de parution'),
        'nombre_pages' :_('nombres de pages'),
        'resume' :_('Résumé'),
        'imaurl':_('Image avec Url'),
        'nom':_('Nom')
        }
class NomForm(ModelForm):
    class Meta:
        model = models.Nom
        fields = ('Nom',)
        labels = {
            'nom':_('Nom')}

