# -*- encoding: utf-8 -*-
import re

# this is code that seperates the data according to the languages that I need
# this program extracts the cognates from the master file and seperates them according to language
# it creates 4 txt files for each language: a complete file with all words, a training file, used for training, a testing file, used to test the net, and a valuation file, used to evaluate performance



f = open('romance-ortography.txt','r', encoding='utf-8')
t = f.read()
f.close() # reads in data

separators = "\t", "\n" # defines the seperators by which we separate the string
def custom_split(sepr_list, str_to_split): # custom function to allow us to split on multiple delimiters
    regular_exp = '|'.join(map(re.escape, sepr_list)) # defines a regex
    return re.split(regular_exp, str_to_split) # gives us the output of the custom function

words = custom_split(separators,t) #split on tab and newline
words = words[6:]
# removing the language names in the columns
# print(words)

def split(word): #return characters as a list
    return list(word)  

def listToString(s):  
    # initialize an empty string 
    str1 = " " 
# return string   
    return (str1.join(s)) 

stop = 0
for word in words:
#	stop += 1
	index=words.index(word)
	wordnew = list(word)
#	for i in wordnew:
#		i = i + "\s"
	wordnew = listToString(wordnew)
	words.pop(index)
	words.insert(index, wordnew)
	if stop > len(words):
		break


romanian= [] #creating lists for each language
french= []
italian= []
spanish=[]
portuguese=[]
latin=[]

counter = 0 #counter to ensure we keep track

for word in words: #separating the data into different lists
	counter +=1
	if counter ==1:
		romanian.append(word)
	if counter ==2:
		french.append(word)
	if counter ==3:
		italian.append(word)
	if counter ==4:
		spanish.append(word)
	if counter ==5:
		portuguese.append(word)
	if counter ==6:
		latin.append(word)
	if counter ==7:
		romanian.append(word)
		counter =1
if len(french)==len(spanish) == len(latin)==len(romanian) == len(portuguese)==len(italian):
	print('the lists compiled correctly') #making sure everything is in order
else:
	print('something went wrong')
#print(len(french),len(spanish),len(latin), len(romanian),len(portuguese),len(italian))

ro_french_port_span = romanian+french+spanish+portuguese ##creating a large list to get the vocab for concatenation
french_port_span= french+spanish+portuguese# creating vocabularies for different concatenations
french_span= french+spanish
ro_port_span = romanian+spanish+portuguese 


def output(wordlist,textfilename): #custom function to print the language lists into txt files
	textfilename = 'data\\' + str(textfilename)+ '.txt' #defines the name of the textfile
	textfile = open(textfilename,'w+',encoding='utf-8') #opens a new file
	c=0
	for element in wordlist: #iterates over the list
		c+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if c==1: #first entry does not get a newline
			textfile.write(element)
		else:
			textfile.write('\n') #newline for all subsequent entries
			textfile.write(element) #writes in the file
	textfile.close() #close
	############### can use this for everything now, just define a list and print the contents into a file,easy

output(spanish,'spanish_complete') #now we are creating files for the full languages
output(french,'french_complete')
output(romanian,'romanian_complete')
output(italian,'italian_complete')
output(portuguese,'portuguese_complete')
output(latin, 'latin_complete')
################################################################
## now we build training data, for the training data we grab 70% of all words
## we also build the test and evaluation sets, which carry 20% and 10% of the words respectively
################################################################

def train_output(listname,name): ### we create a custom function that does all of the above for us
	training=[] #empty lists to use 
	test=[]
	value=[]
	vocab=['<blank>', '<unk>' ,'<s>','</s>']
	counter = 0 #counter allowing us to only get every n word
	for word in listname: #creating vocab files from the text
		for v in word: #goes through every item of the word
			if v in vocab: #checks if already part of the vocab file
				continue #if so, we go again
			else: #if not we add it
				vocab.append(v)
		counter +=1 #adds one to the counter for every word
		if counter <= 7: #words 1-7 go to training
			training.append(word)
		if counter > 7 and counter <10: #8-9 go to testing
			test.append(word)
		if counter == 10:	 #10 goes to value
			value.append(word)
			counter = 0 #counter is reset
	textfilename_training ='data\\train\\' + str(name)+'_training'+ '.txt' # creates the filename of the training file, using the 'name' input in the function
	textfile_training = open(textfilename_training,'w+',encoding='utf-8') #opens a new file, called name_training
	c=0
	for element in training: #iterates over the list of training items
		c+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if c==1: #first entry does not get a newline
			textfile_training.write(element)
		else:
			textfile_training.write('\n') #newline for all subsequent entries
			textfile_training.write(element) #writes in the file
	textfile_training.close() #close the file
	################################################### rinse and repeat for testing
	textfilename_test = 'data\\test\\' +str(name)+'_test'+ '.txt' #defines the name of the textfile
	textfile_test = open(textfilename_test,'w+',encoding='utf-8') #opens a new file
	d=0
	for element in test: #iterates over the list
		d+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if d==1: #first entry does not get a newline
			textfile_test.write(element)
		else:
			textfile_test.write('\n') #newline for all subsequent entries
			textfile_test.write(element) #writes in the file		
	textfile_test.close()
	################################################################### and again vor valuation
	textfilename_val = str(name)+'_val'+ '.txt' #defines the name of the textfile
	textfile_val = open('data\\val\\' +textfilename_val,'w+',encoding='utf-8') #opens a new file
	i=0
	for element in value: #iterates over the list
		i+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if i==1: #first entry does not get a newline
			textfile_val.write(element)
		else:
			textfile_val.write('\n') #newline for all subsequent entries
			textfile_val.write(element) #writes in the file		
	textfile_val.close()
	######################### creating the vocab file
	textfilename_vocab = 'data\\vocab\\' +str(name)+'_vocab'+ '.txt' #defines the name of the textfile
	textfile_vocab = open(textfilename_vocab,'w+',encoding='utf-8') #opens a new file
	i=0
	for element in vocab: #iterates over the list
		i+=1 #creating a counter so we dont have a trailing newline at the end of the file
		if i==1: #first entry does not get a newline
			textfile_vocab.write(element)
		else:
			textfile_vocab.write('\n') #newline for all subsequent entries
			textfile_vocab.write(element) #writes in the file		
	textfile_vocab.close()
	#########################


train_output(french,'french') #call the function
train_output(latin,'latin')
train_output(romanian,'romanian')
train_output(portuguese,'portuguese')
train_output(french,'french')
train_output(spanish,'spanish')
train_output(italian, 'italian')
train_output(ro_french_port_span,'ro_french_port_span')

train_output(french_port_span,'french_port_span')
train_output(french_span,'french_span')
train_output(ro_port_span,'ro_port_span')
#print(italian)




