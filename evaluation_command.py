# -*- encoding: utf-8 -*-
import jellyfish
import itertools 
import argparse

def read_in(textfilename): #this gives us a master read-in function, this reads in the file
	file = str(textfilename) # and then splits the file on newline, and then puts that into a list
	f = open(file, 'r')# the list is returned
	string = f.read()
	listvar = []
	listvar = string.split("\n")
	f.close()
	return listvar

def damerau(stringA,stringB):
	return jellyfish.damerau_levenshtein_distance(stringA, stringB)




def eval(filename1,filename2):
	list1=read_in(filename1)
	list2=read_in(filename2)
	edit_distance={}
	edit_distance[0]=0
	edit_distance[1]=0
	edit_distance[2]=0
	edit_distance[3]=0
	edit_distance[4]=0
	edit_distance['5+']=0
	filename= filename1 +'edit_eval.txt'
	file = open(filename,'w+')
	counter =0
	for (a,b) in zip(list1,list2):
		val=damerau(a,b)
		counter +=1
		if val < 5:
			edit_distance[val] +=1
		else:
			edit_distance['5+'] +=1
	distance1 = int(edit_distance[0])+int(edit_distance[1])
	distance2 = edit_distance[0]+edit_distance[1]+edit_distance[2]
	distance3 = edit_distance[0]+edit_distance[1]+edit_distance[2]+edit_distance[3]
	distance4 = edit_distance[0]+edit_distance[1]+edit_distance[2]+edit_distance[3]+edit_distance[4]
	for key in edit_distance:
		file.write(str(key)+ ':'+ str(edit_distance[key]))
		file.write("\n")
	score = (edit_distance[0] + edit_distance[1]*.9 + edit_distance[2]*.8 + edit_distance[3]*.7 +	edit_distance[4]+.6)/counter
	counter = 'Total strings:' + str(counter)
	score = "score: " + str(score)
	percent0 = edit_distance[0]/717*100
	percent1 = distance1/717*100
	percent2 = distance2/717*100
	percent3 = distance3/717*100
	percent4 = distance4/717*100
	percent0= "within 0 edit:" + str(percent0)
	percent1= "within one edit:" + str(percent1)
	percent2= "within two edit:" + str(percent2)
	percent3= "within three edit:" + str(percent3)
	percent4= "within four edit:" + str(percent4)
	file.write(counter)
	file.write("\n")
	file.write(score)
	file.write("\n")
	file.write(percent0)
	file.write("\n")
	file.write(percent1)
	file.write("\n")
	file.write(percent2)
	file.write("\n")
	file.write(percent3)
	file.write("\n")
	file.write(percent4)
	file.close()### the score is computed by adding the numbers 



counter = 1000 ###this was used for evaluating a series of files
counter_list=[]
while counter < 10001:
	counter_list.append(counter)
	counter +=1000


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--src", help="your translated file" ,required=True) # 
	parser.add_argument("--tgt", help="your target file" ,required=False) #
	args = parser.parse_args()
	if args:
		eval(args.src,args.tgt)



if __name__ == '__main__':
    main() 
