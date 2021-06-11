import os
import argparse
import sys



def main():
	if len(sys.argv)==1:
		print("Please specify the following arguments:\n --dir: the directory you wish to use, \n --iter: \"Yes\" if you wish to iterate over all lvl 1 sub-directories\n DISCLAIMER: Please be aware that your .yaml files must be configured as if they were in the directory from which execute_all.py is operating")
	parser = argparse.ArgumentParser(description='specify a directory')
	parser.add_argument("--dir", help="The directory where your yaml files are, if this is the directory, try \"here\"" ,required=True) 
	parser.add_argument("--iter", help="If \"Yes\" will look through all level 1 subdirectories of the directory you specified in --dir, default: False" ,required=False) 
	args = parser.parse_args()	# returns data from the options specified (echo
	print("You chose iteratopm:", args.iter)
	print("You chose directory:", args.dir)
	if args.dir == 'here':
		args.dir= os.path.dirname(os.path.realpath(__file__))
	##################

	if args.iter !='Yes':
		print("only executing the directory you specified")
		directory = args.dir
		for entry in os.scandir(directory):
			if (entry.path.endswith(".yaml")
				or entry.path.endswith(".yml")) and entry.is_file():
				print(entry.path)
				command= 'onmt_train --config ' + '\"' + entry.path + '\"'
				os.system(command)
	elif args.iter == 'Yes':
		print("executing this directory and all immediate sub-directories")
		directory = args.dir
		for entry in os.scandir(directory):###we iterate over the directory
			if (entry.path.endswith(".yaml")
				or entry.path.endswith(".yml")) and entry.is_file():
				print(entry.path)
			elif entry.is_dir(): ##here we identify lvl1 subdirectories
				print('test')
				for i in os.scandir(entry): #now we iterate over those
					if (i.path.endswith(".yaml")
						or i.path.endswith(".yml")) and i.is_file():
						print(i.path)
						command= 'onmt_train --config ' + '\"' + i.path + '\"'
						os.system(command)




if __name__ == '__main__':
    main()
