from urllib2 import urlopen

url = 'http://lorempixel.com/'
categorias = ['abstract','animals','business','cats','city',
			  'food','night','life','fashion','people',
			  'nature','sports','technics','transport']

print "Categorias"
print "=" * 9
print "\n"


for categoria in categorias:
		print categoria 

print "\n"

alto = raw_input('Escribe la altura de la imagen: ')
ancho = raw_input('Escribe la anchura de la imagen: ')
categoria = raw_input('Escribe la categoria de la imagen que buscas:' )

url_req = "%s/%s/%s/%s" % (url,ancho,alto,categorias[int(categoria)])
resultado = urlopen(url_req)
lectura = resultado.read()
f = open("holder.jpg", "wb")#foto
f.write(lectura)
f.close()
