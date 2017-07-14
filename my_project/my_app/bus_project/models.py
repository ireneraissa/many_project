from django.db import models

# Create your models here.
class chauffeur(models.Model):
	nom_chauffeur=models.TextField()
	prenom_chauffeur=models.TextField()
	telephone_chauffeur=models.TextField()
	


class Bus(models.Model):
	matricule=models.IntegerField()
	numero_ligne=models.IntegerField()
	nombre_place=models.IntegerField()

	info_chauffeur=models.ForeignKey(chauffeur, on_delete=models.CASCADE)
	id_device=models.TextField()
	status1='opened'
	status2='closed'

