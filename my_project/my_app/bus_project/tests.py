from django.test import TestCase
from .models import chauffeur, Bus
import pandas as pd 
# Create your tests here.
# test afin de gerer un parc de bus muni d'ecran
class fonctionnalite(TestCase):
	BUS=[]
	bus=Bus(matricule=12342, numero_ligne=2, nombre_place=60)
	

	def test_add_bus(self):

		#ajout=input('id_device')


		#if ajout!=None:

		response=BUS.append(le_bus)
		self.assertEqual(len(response), 1)

	def test_list_of_bus(self):
		printer=print(Bus)

		self.assertTrue(printer , True)



	def test_modify_bus(self):
		#modifier=input('entrer id a modifier')
		
		if modifier in Bus:

			bus.matricule=45687
			response= bus.matricule == 12342

		self.assertTrue(response, True)



	def test_delete_bus(self):
		supprimer=
		#supprimer=input('entrer id que vous voulez supprimer')
		#if supprimer in Bus:
		del Bus[supprimer]
		self.assertIs(BUS, None)

	def test_import(self):


		import_bus=Bus.to_csv('infos_bus.csv', index=False)
		response=pd.read_csv(import_bus)
		self.assertIs(response, True)