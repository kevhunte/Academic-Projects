import socket, threading, sys
from queue import Queue

"""
Threaded port scanner. Default host is local and up to port 5000 
Most be ran with Python3

"""


print_lock = threading.Lock() #mutex for threads
until_port = 5001
host = 'localhost'
q=Queue()


if len(sys.argv) > 1:
	host = sys.argv[1]	#only except one command line argument, and that will be a host to check
	if len(sys.argv) > 2:
		until_port = (int)(sys.argv[2])	#convert to int

def pscan(port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp socket
	try:
		connect = s.connect(host,port)
		with print_lock:
			print('port',port,'open')
		connect.close() #close socket connection for other threads to use
	except:
		pass #skip otherwise

def thread_dispatch():
	while True:
		worker = q.get()	#grabs from queue
		pscan(worker)		#work for threads to do
		q.task_done()		#empties queue

for x in range(40):
	t = threading.Thread(target=thread_dispatch) #40 threads, will run thread_dispatch method
	t.daemon = True		#all threads die and reaped when main thread dies
	t.start()

for worker in range(1,until_port):
	q.put(worker) 		#passes parameter to worker from range, ports to check

q.join()			#waits for work to be completed by thread
