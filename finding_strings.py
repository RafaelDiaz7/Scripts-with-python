string = "A Successful mind is the key to feel better experiences in the present moment with the energetic things and the material also."

def find_string(target_string):
	finded_string_idx = string.find(target_string)
	print "The index of the string is =>" + str(finded_string_idx)
	print string[finded_string_idx:19]

find_string("Successful")

text = "A zip file are zipped and the zip algorithm is maked for compress"

first_zip = text.find("zip")
second_zip = text.find("zip", first_zip + 1)
# Another solution: print text.find("zip" text.find("zip" + 1))
