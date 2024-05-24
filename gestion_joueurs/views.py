from django.shortcuts import render, redirect

from .models import Entrainement, Joueur
from .forms import EntrainementForm, JoueurForm


def enregistrer_joueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            joueur = form.save()
            return redirect('liste_joueurs')
    else:
        form = JoueurForm()
    return render(request, 'gestion_joueurs/enregistrer_joueur.html', {'form': form})


def liste_joueurs(request):
    joueurs = Joueur.objects.all()
    return render(request, 'gestion_joueurs/liste_joueurs.html', {'joueurs': joueurs})


def planifier_entrainement(request):
    if request.method == 'POST':
        form = EntrainementForm(request.POST)
        if form.is_valid():
            entrainement = form.save()
            return redirect('liste_entrainements')
    else:
        form = EntrainementForm()
    return render(request, 'gestion_joueurs/planifier_entrainement.html', {'form': form})


def liste_entrainements(request):
    entrainements = Entrainement.objects.all()
    return render(request, 'gestion_joueurs/liste_entrainements.html', {'entrainements': entrainements})


def home(request):
    return render(request, 'pages/coach.html')
