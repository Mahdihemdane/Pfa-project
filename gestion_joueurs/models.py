from django.db import models

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    identifiant_unique = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Entrainement(models.Model):
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    lieu = models.CharField(max_length=100)

    def __str__(self):
        return f"Entraînement le {self.date} de {self.heure_debut} à {self.heure_fin}"
