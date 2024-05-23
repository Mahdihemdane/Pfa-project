# gestion_joueurs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('enregistrer-joueur/', views.enregistrer_joueur, name='enregistrer_joueur'),
    path('liste-joueurs/', views.liste_joueurs, name='liste_joueurs'),
    path('planifier-entrainement/', views.planifier_entrainement, name='planifier_entrainement'),
    path('liste-entrainements/', views.liste_entrainements, name='liste_entrainements'),
]
