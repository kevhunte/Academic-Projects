"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; echoes lines until eof when client closes socket;
spawns a thread to handle each client connection; threads share global
memory space with main thread; this is more portable than fork: threads
work on standard Windows systems, but process forks do not;
"""

import time, thread, sys		  # or use threading.Thread().start()
from socket import *                     # get socket constructor and constants
myHost = ''                             # server machine, '' means local host
myPort = 50007                           # listen on a non-reserved port number

if len(sys.argv) > 1:
    myPort = int(sys.argv[1])                # specific port number that wants to be used
    #if len(sys.argv) > 2:

sockobj = socket(AF_INET, SOCK_STREAM)           # make a TCP socket object
sockobj.bind((myHost, myPort))                   # bind it to server port number
sockobj.listen(5)                                # allow up to 5 pending connects

def now():
    return time.ctime(time.time())               # current time on the server
						# HTTP responst message
payload = ''

def handleClient(connection):                    # in spawned thread: reply
    time.sleep(5)                                # simulate a blocking activity
    while True:                                  # read, write a client socket
        data = connection.recv(1024)
        if not data: break
	if data.find('GET',0, 2):		#if data contains GET, store requested file
		data = data.split(' ')		#breaks data into list
		data = data[1]			#store second part of string, contains file wanted
		data = data[1:]			#string slice to take off '/' for correct name of file wanted
		try:
		   file = open(data,'r')
		   payload = 'HTTP/1.1 200 OK\r\n Date: '+now()+'\n Server: '+myHost+'\n Content-Length: 4096\n Connection: Keep-Alive\n Content-Type: text/html; charset=iso-8859-1\n\n'
		   bytes=file.read()
        	   reply = payload+bytes  			#reply with 200, OK message, then send file
        	   connection.send(reply.encode())
		except:				#Message for when file is not found in directory, to avoid error on open()
                   payload = 'HTTP/1.1 404 Not Found\r\n Date: '+now()+'\n Server: '+myHost+'\n Content-Length: 4096\n Connection: Keep-Alive\n Content-Type: text/html; charset=iso-8859-1\n\n'
                   connection.send(payload)
	file.close()
	#while(bytes):				#needed to send all bytes, in case not all sent in one func call
		#connection.send(bytes.encode())

	print data+ ' file sent'		#some acknowledgement that asked file went through
	connection.close()

def dispatcher():                                # listen until process killed
    while True:                                  # wait for next connection,
        connection, address = sockobj.accept()   # pass to thread for service
        print('Server connected by', address)	#took out end=' ' after address, caused errors
        print('at', now())
        #handleClient(connection)		#run function
        thread.start_new_thread(handleClient, (connection,))

dispatcher()
