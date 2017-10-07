def read_file_string(file_name):
	# Takes a filename string, returns a string of all lines of the file
	f = open(file_name, 'r')
	obj = ''
	strings = f.read()
	f.close()
	print strings

read_file_string("text.txt")