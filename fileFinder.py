#!/usr/bin/python
import os,sys,time
from datetime import datetime
from subprocess import call

""" Customly made version of the 'find' command.
    Has option of thorough search, that returns all paths of desired dir or file.
    Traverses the entire file Directory, right from root folder"""

cwd = os.getcwd()               #same as pwd call
path = "/"			#default search is from root
list = ['fileMap']    		#file options
paths = []
found = False
thorough = False
#starttime = datetime.now().microsecond 	#time in microseconds
#starttime = time.time()				#time in microseconds

def usage():
	print("python [filename] [-t means thorough search]")

def fileWalker(p):		#searches directory and finds file
	global found				#tells python not to make another local var named 'found'
	#count = 0
        try:
		if(thorough == True):
			print("Thorough search starting...")
		else:
			print("regular search starting.. this may take a little while if a broad search range is given")
                for dpath, dname, fname in os.walk(p):
			#print(fname)
                        if((filename in fname) or (filename in dname)):
				#timetaken = (time.time() - starttime) * 1000
				found = True
				#count+=1
                                #print("%d results found ") % count		#To show user that results are being returned
				#paths.append(dpath)	#should help at runtime. Prints all results later
                                print(dpath)
				#print("Took "+timetaken+" seconds")
				#call("ls -l "+dpath,shell=True)	#be careful with shell = True. Executes this command
                                #path = dpath	#set path to path of file for scp input
                                if(thorough == False): 
					return 	#skip exiting the walk when the user wants a thorough search
                if(found==False): print("File not found. Change starting path?")
		"""else: 
			for x in paths: print (x)		#prints paths of results"""
	
        except IOError:
                print("File may not exist")
	except KeyboardInterrupt:
		print("Search ended early")
        #except:

if len(sys.argv) > 1:
	filename = sys.argv[1]		#filename to search for
#elif len(sys.argv) >  2:	#pass this parameter if available
	#filename = sys.argv[1]          #filename to search for
	#path = sys.argv[2]
else:
	usage()

if("-t" in sys.argv):
	thorough = True

fileWalker(path)
