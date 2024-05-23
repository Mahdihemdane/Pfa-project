from django import forms
from .models import Entrainement, Joueur

class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'prenom', 'date_naissance']

        
class EntrainementForm(forms.ModelForm):
    class Meta:
        model = Entrainement
        fields = ['date', 'heure_debut', 'heure_fin', 'lieu']
