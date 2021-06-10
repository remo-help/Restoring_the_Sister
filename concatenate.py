# -*- encoding: utf-8 -*-

from itertools import chain, zip_longest

def read_in(textfilename): #this gives us a master read-in function, this reads in the file
	file = str(textfilename) + '.txt'# and then splits the file on newline, and then puts that into a list
	f = open(file, 'r',encoding='utf-8')# the list is returned
	string = f.read()
	listvar = []
	listvar = string.split("\n")
	f.close()
	return listvar

##############reading in the files
french_training = read_in('french_training_res')
spanish_training = read_in('spanish_training_res')
romanian_training = read_in('romanian_training_res')
portuguese_training = read_in('portuguese_training_res')
italian_training = read_in('italian_training_res')

french_val = read_in('french_val_res')
spanish_val = read_in('spanish_val_res')
romanian_val = read_in('romanian_val_res')
portuguese_val = read_in('portuguese_val_res')
italian_val = read_in('italian_val_res')

french_test = read_in('french_test_res')
spanish_test = read_in('spanish_test_res')
romanian_test = read_in('romanian_test_res')
portuguese_test = read_in('portuguese_test_res')
italian_test = read_in('italian_test_res')



##########we need these functions for the complex concatenation v2
def interspace_strings(string1): #function that allows us to interspace the strings
    return ''.join(chain(*zip_longest(string1, ' ', fillvalue=' ')))
def interleave_strings(string1, string2, string3, string4): #ok, so we use itertools chain and zip_longest to interweave, this function allows us to return a string output
    return ''.join(chain(*zip_longest(string1, string2, string3, string4, fillvalue='')))
def interleave_strings3(string1, string2, string3): #ok, interleave 3 strings
    return ''.join(chain(*zip_longest(string1, string2, string3, fillvalue='')))
def interleave_strings2(string1, string2): #ok, for two strings
    return ''.join(chain(*zip_longest(string1, string2, fillvalue='')))


###########################this is the smart complex concatenation, it interweaves the strings, removes all spaces, and then adds spaces between each character
def concatenatecomplexv2(filename, listname1,listname2,listname3,listname4):
	newlist =[]
	index = -1
	for i in listname1: #first we get every single line
		index += 1
		string2 =listname2[index]
		string3=listname3[index]
		string4=listname4[index]
		newstring=interleave_strings(i, string2, string3, string4)
		newstring = newstring.replace(" ", "")
		newstring = interspace_strings(newstring)
		newlist.append(newstring)
	#print(newlist)
	textfilename_complex = filename + '.txt' # creates the filename of the training file, using the 'name' input in the function
	textfile_complex = open(textfilename_complex,'w+',encoding='utf-8')
	c=0
	for element in newlist: #iterates over the list of training items
		c+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if c==1: #first entry does not get a newline
			textfile_complex.write(element)
		else:
			textfile_complex.write('\n') #newline for all subsequent entries
			textfile_complex.write(element) #writes in the file
	textfile_complex.close() #close the file

####################### concatenate with 3 languages
def concatenatecomplex_triple(filename, listname1,listname2,listname3):
	newlist =[]
	index = -1
	for i in listname1: #first we get every single line
		index += 1
		string2 =listname2[index]
		string3=listname3[index]
		newstring=interleave_strings3(i, string2, string3)
		newstring = newstring.replace(" ", "")
		newstring = interspace_strings(newstring)
		newlist.append(newstring)
	#print(newlist)
	textfilename_complex = filename + '.txt' # creates the filename of the training file, using the 'name' input in the function
	textfile_complex = open(textfilename_complex,'w+',encoding='utf-8')
	c=0
	for element in newlist: #iterates over the list of training items
		c+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if c==1: #first entry does not get a newline
			textfile_complex.write(element)
		else:
			textfile_complex.write('\n') #newline for all subsequent entries
			textfile_complex.write(element) #writes in the file
	textfile_complex.close() #close the file

###########################concatenate 2 languages

def concatenatecomplex_duple(filename, listname1,listname2):
	newlist =[]
	index = -1
	for i in listname1: #first we get every single line
		index += 1
		string2 =listname2[index]
		newstring=interleave_strings2(i, string2)
		newstring = newstring.replace(" ", "")
		newstring = interspace_strings(newstring)
		newlist.append(newstring)
	#print(newlist)
	textfilename_complex = filename + '.txt' # creates the filename of the training file, using the 'name' input in the function
	textfile_complex = open(textfilename_complex,'w+',encoding='utf-8')
	c=0
	for element in newlist: #iterates over the list of training items
		c+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if c==1: #first entry does not get a newline
			textfile_complex.write(element)
		else:
			textfile_complex.write('\n') #newline for all subsequent entries
			textfile_complex.write(element) #writes in the file
	textfile_complex.close() #close the file


####EXECUTE


concatenatecomplexv2('concatenate_input_complex',french_training,romanian_training,portuguese_training,spanish_training)
concatenatecomplexv2('concatenate_val_complex',french_val,romanian_val,portuguese_val,spanish_val)
concatenatecomplexv2('concatenate_test_complex',french_test,romanian_test,portuguese_test,spanish_test)

concatenatecomplex_triple('concatenate_fre_po_it_input',french_training,portuguese_training,spanish_training)
concatenatecomplex_triple('concatenate_fre_po_it_val',french_val,portuguese_val,spanish_val)
concatenatecomplex_triple('concatenate_fre_po_it_test',french_test,portuguese_test,spanish_test)

concatenatecomplex_duple('concatenate_fre_it_input',french_training, spanish_training)
concatenatecomplex_duple('concatenate_fre_it_val',french_val, spanish_val)
concatenatecomplex_duple('concatenate_fre_it_test',french_test, spanish_test)
