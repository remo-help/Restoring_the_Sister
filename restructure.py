# -*- encoding: utf-8 -*-
import re
import itertools

################################# DOCUMENTATION ############################
# This script takes our files and makes sure that we ONLY keep lines that have at least ONE Italian (target) cognate
# and one other corresponding cognate
############################################################################

def read_in(textfilename): #this gives us a master read-in function, this reads in the file
	file = str(textfilename) + '.txt'# and then splits the file on newline, and then puts that into a list
	f = open(file, 'r',encoding='utf-8')# the list is returned
	string = f.read()
	listvar = string.split("\n")
	f.close()
	return listvar


def restructure(item): #wrting this in a way that will allow me to jsut call "train" "test" etc.
	target = 'italian_' + str(item)
	target_list =read_in(target)
	spanish= 'spanish_' + str(item)
	french= 'french_' + str(item)
	romanian= 'romanian_' + str(item)
	portuguese= 'portuguese_' + str(item)
	spanish_list = read_in(spanish) #creating the lists 
	french_list = read_in(french)
	romanian_list = read_in(romanian)
	portuguese_list = read_in(portuguese)
	textfilename_target = str(target)+'_res'+'.txt' #creating the textfilenames
	textfilename_spanish = str(spanish)+'_res'+'.txt'
	textfilename_french = str(french)+'_res'+'.txt'
	textfilename_romanian = str(romanian)+'_res'+'.txt'
	textfilename_portuguese = str(portuguese)+'_res'+'.txt'
	textfile_target = open(textfilename_target,'w+',encoding='utf-8') ##opening the textfile
	textfile_spanish = open(textfilename_spanish,'w+',encoding='utf-8')
	textfile_french = open(textfilename_french,'w+',encoding='utf-8')
	textfile_romanian = open(textfilename_romanian,'w+',encoding='utf-8')
	textfile_portuguese = open(textfilename_portuguese,'w+',encoding='utf-8')
	for (t, a, b, c, d) in zip(target_list,spanish_list,french_list,romanian_list,portuguese_list):
		if t == '-':#dont write if the target is a '-'
			pass
		elif a == '-' and b == '-' and c == '-' and d == '-':
			pass
		elif t== target_list[-1]:
			textfile_target.write(t) #writing in the files
			textfile_spanish.write(a)
			textfile_french.write(b)
			textfile_romanian.write(c)
			textfile_portuguese.write(d)
		else:
			textfile_target.write(t)
			textfile_target.write("\n") #writing in the files
			textfile_spanish.write(a)
			textfile_spanish.write("\n")
			textfile_french.write(b)
			textfile_french.write("\n")
			textfile_romanian.write(c)
			textfile_romanian.write("\n")
			textfile_portuguese.write(d)
			textfile_portuguese.write("\n")
	textfile_target.close()#closing the textfile
	textfile_french.close()#closing the textfile
	textfile_spanish.close()#closing the textfile
	textfile_romanian.close()#closing the textfile
	textfile_portuguese.close()#closing the textfile

restructure('training')#let's run it
restructure('test')
restructure('val')
restructure('complete')
