# Este programa es una prueba de la funcion map()
# Se probara para convertir una cadena en un arreglo de enteros

numbers = '6 1 2 3 5 4 6'

numbers = list(map(int, numbers.rstrip().split()))

print(numbers)
