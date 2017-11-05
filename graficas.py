from matplotlib import pyplot

lenguajes =('Python', 'C', 'Java', 'Go', 'JAVASCRIPT')
slices = (100, 130, 90, 80, 128)
colores = ('red', 'blue', 'green', '#DD98AA', '#18492D')
valores = (0.1, 0, 0, 0, 0)

_, _, texto = pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%', explode=valores, startangle=90)

for tex in texto:
	tex.set_color('white')

pyplot.axis('equal')
pyplot.title('Lenguajes de programacion')
pyplot.show()

pyplot.rcParams['toolbar'] = 'None'