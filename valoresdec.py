c = 0
a = 100
b = 1

while a >= b:
    if a%b == 0:
        c = a/b
        print('Valor entero de c: ',int(c))
    b = b + 1
