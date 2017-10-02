# encoding: utf-8 
class Persona: 
	def _init_(self,edad,nom): 
		self.edad = edad 
		self.nombre = nom 

	def saludar(self,saludo): 
	print saludo

class IngSistemas(Persona):
	def programar(self,lenguaje):
		print "Voy a programar en", lenguaje

class LicDerecho(Persona):
	def estudiarCaso(self,de):
		print "Estudiare el caso de", de
		

# Creamos objetos 
Smayth = IngSistemas(28,'Smayth') 
Omar = LicDerecho(45,'Omar') 

# utilizamos los atributos y metodos de la clase 
Smayth.saludar("Hola Soy " + Smayth.nombre + " y tengo " + str(Smayth.edad) + " años de Edad") 

#el resultado es-> Hola Soy Smayth y tengo 28 años de Edad