numero_magico = int(raw_input("Ingresa el numero magico: "))
numero_no_magico = int(raw_input("Adivina el numero magico: "))

while numero_magico != numero_no_magico:#se repite el ciclo hasta que se adivine el valor
	if numero_magico > numero_no_magico:
		numero_no_magico = int(raw_input("Mi pana tu puedes!, intenta con un valor mas grande: "))
		continue
	numero_no_magico = int(raw_input("Dale al coco!, intenta con un valor mas pequeno: "))

print "Bien hecho, ganaste!!"
