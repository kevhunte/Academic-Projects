"""
Client side: use sockets to send data to the server, and print server's
reply to each message line; 'localhost' means that the server is running
on the same machine as the client, which lets us test client and server
on one machine;  to test over the Internet, run a server on a remote
machine, and set serverHost or argv[1] to machine's domain name or IP addr;
Python sockets are a portable BSD socket interface, with object methods
for the standard socket calls available in the system's C library;
"""

import sys
from socket import *              # portable socket interface plus constants
serverHost = 'localhost'          # server name, or: 'starship.python.net'
serverPort = 50007                # non-reserved port used by the server

message = 'Hello network world'          # default text to send to server
                                            # requires bytes: b'' or str.encode()
if len(sys.argv) > 1:       
    serverHost = sys.argv[1]                # server from cmd line arg 1
    if len(sys.argv) > 2:                   # text from cmd line args 2..n  
	message = 'GET /' + sys.argv[2] + ' HTTP/1.0\r\n'	#GET HTTP request line w/ website
	if len(sys.argv) > 3:
	    serverPort = int(sys.argv[3])	#will get port num from command line

sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort))   # connect to server machine + port

data = sockobj.recv(4096)               # receive line from server: up to 4 bytes.
for x in data:
	if x == '\n': print ''    
	else: 
		sys.stdout.write(x)         # cleanly prints out data by ack \n char.
		sys.stdout.flush()
message=raw_input()
sockobj.send(message)				#sends user's answer
print sockobj.recv(4096)			#server response of game answer

sockobj.close()                             # close socket to send eof to server
