# gestion_joueurs/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('enregistrer-joueur/', enregistrer_joueur, name='enregistrer_joueur'),
    path('liste-joueurs/', liste_joueurs, name='liste_joueurs'),
    path('planifier-entrainement/', planifier_entrainement, name='planifier_entrainement'),
    path('liste-entrainements/', liste_entrainements, name='liste_entrainements'),
]
