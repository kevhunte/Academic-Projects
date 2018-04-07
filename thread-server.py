"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; echoes lines until eof when client closes socket;
spawns a thread to handle each client connection; threads share global
memory space with main thread; this is more portable than fork: threads
work on standard Windows systems, but process forks do not;
"""

import time, thread, sys, random	 # or use threading.Thread().start()
from socket import *                     # get socket constructor and constants
from random import shuffle
myHost = ''                              # server machine, '' means local host
myPort = 50007                           # listen on a non-reserved port number
payload = ''

sockobj = socket(AF_INET, SOCK_STREAM)           # make a TCP socket object
sockobj.bind((myHost, myPort))                   # bind it to server port number
sockobj.listen(5)                                # allow up to 5 pending connects

def Jumble(connection):
   time.sleep(5)
   F = open('wordlist.txt')
   words = F.readlines()					#stores words of file in list
   F.close()
   while True:
    	word = words[random.randrange(len(words))]
    	while len(word) > 5 or len(word) == 0:		#if word is too long, pick again
        	word = words[random.randrange(0, len(words))]
    	word = word.rstrip()				#takes out linefeed chars
    	old_word = word
    	word = list(word)
	shuffle(word)
	str_word=''
	for x in word:	str_word+=x+' '		#scramble order,then turn back into string, not list
	connection.send(str_word+'\nType your answer\n')
    	match_word = connection.recv(1024)		#stores string input of user. was input()
	if not match_word: break 
    	new_word = match_word + '\n'
    	if new_word in words and set(match_word) == set(old_word):	#word in list && input == rand word
       		connection.send('You win!')
    	else:
        	connection.send('Incorrect. The answer is ' + old_word)
   connection.close()

def now():
    return time.ctime(time.time())               # current time on the server

def dispatcher():                                # listen until process killed
	while True:                                  # wait for next connection,
        	connection, address = sockobj.accept()   # pass to thread for service
        	print('Server connected by', address)	#took out end=' ' after address, caused errors
        	print('at', now())
        	thread.start_new_thread(Jumble, (connection,))

dispatcher()
