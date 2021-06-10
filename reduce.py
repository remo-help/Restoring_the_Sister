# -*- encoding: utf-8 -*-

def read_in(textfilename): #this gives us a master read-in function, this reads in the file
	file = str(textfilename) + '.txt'# and then splits the file on newline, and then puts that into a list
	f = open(file, 'r',encoding='utf-8')# the list is returned
	string = f.read()
	listvar = []
	listvar = string.split("\n")
	f.close()
	return listvar

def reduce1(listname,filename): #this reduces the data to 90% of the original
	listname = read_in(listname) 
	counter = 0
	filename = filename + '10'+ '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter < 10:
			file.write(line)
			file.write("\n")
		else:
			counter=0
		counter +=1

def reduce2(listname,filename): #this reduces to 80%
	listname = read_in(listname) 
	counter = 0
	filename = filename + '20'+  '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		counter +=1
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter == 5:
			pass
		elif counter < 11 and counter != 5:
			file.write(line)
			file.write("\n")
		else:
			counter=0
		

def reduce3(listname,filename): #this reduces to 70%
	listname = read_in(listname) 
	counter = 0
	filename = filename + '30'+ '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		counter +=1
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter == 2:
			pass
		elif counter == 5:
			pass
		elif counter < 11 and counter != 5:
			file.write(line)
			file.write("\n")
		else:
			counter=0
		

def reduce4(listname,filename): #this reduces to 60%
	listname = read_in(listname) 
	counter = 0
	filename = filename + '40'+  '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		counter +=1
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter == 2:
			pass
		elif counter == 5:
			pass
		elif counter == 7:
			pass
		elif counter < 11 and counter != 5:
			file.write(line)
			file.write("\n")
		else:
			counter=0
		

def reduce5(listname,filename): #this reduces to 50%
	listname = read_in(listname) 
	counter = 0
	filename = filename +'50'+ '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		counter +=1
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter == 1:
			pass
		elif counter == 3:
			pass
		elif counter == 5:
			pass
		elif counter == 7:
			pass
		elif counter < 11 and counter != 5:
			file.write(line)
			file.write("\n")
		else:
			counter=0

def reduce6(listname,filename): #this reduces to 60%
	listname = read_in(listname) 
	counter = 0
	filename = filename +'60'+ '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		counter +=1
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter == 1:
			pass
		elif counter == 3:
			pass
		elif counter == 5:
			pass
		elif counter == 7:
			pass
		elif counter == 9:
			pass
		elif counter < 11 and counter != 5:
			file.write(line)
			file.write("\n")
		else:
			counter=0

def reduce7(listname,filename): #this reduces to 70%
	listname = read_in(listname) 
	counter = 0
	filename = filename +'70'+ '.txt' #creating a file to write in
	file = open(filename,'w+',encoding='utf-8')
	for line in listname:
		counter +=1
		if line == "": #there is an empty line at the end of the data, we dont want to add a second
			continue
		elif counter == 1:
			pass
		elif counter == 2:
			pass
		elif counter == 3:
			pass
		elif counter == 5:
			pass
		elif counter == 7:
			pass
		elif counter == 9:
			pass
		elif counter < 11 and counter != 5:
			file.write(line)
			file.write("\n")
		else:
			counter=0
		

def reduce(listname,filename):
	reduce1(listname,filename)
	reduce2(listname,filename)
	reduce3(listname,filename)
	reduce4(listname,filename)
	reduce5(listname,filename)
	reduce6(listname,filename)
	reduce7(listname,filename)

reduce("concatenate_input_complex","input_complex_reduced")
reduce("italian_training_res","italian_training_reduced")
reduce("concatenate_fre_po_sp_input","concatenate_fre_po_sp_input_reduced")