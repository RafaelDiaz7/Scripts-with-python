numero = int(raw_input("Numero al cual correspondra la tabla de multiplicar: "))
for x in xrange(1,11): 
	print str(x) + "*" + str(numero) + "=" + str((numero * x)) 

	#Hace una pregunta que es: Que x este en el rango de 1 al 11, empieza en la primera iteración siendo 1, luego cambirá en las demas iteraciones 2,3,4,etc.
	#Luego se ejecutan las acciones o una
	# Imprimira numero * x = producto de la multiplicación(Asi con todas las iteraciones correspondientes)
	# primera iteración: 1 * 8 = 8
	# Segunda iteracion: 2 * 8 = 16
	#...