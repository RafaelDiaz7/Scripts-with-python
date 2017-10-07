from urllib2 import urlopen

print "Extracting linkzzz"
print "\n"
print "+" * 11
print "/" * 11
print "\n"

url = raw_input("Enter the link: ");
result = urlopen(url)
reading = result.read()
info = open("holder.html", "wb")#foto
info.write(reading)
info.close()
