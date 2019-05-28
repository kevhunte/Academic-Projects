import socket, threading, sys, random, datetime, math

"""
This script generates matrices and sums their values in a singular and threaded way.
It then tests which is faster depending on the dimensions of the matrix
"""

mutex = threading.Lock()
global_sum = 0

def usage():
    message = "python "+sys.argv[0]
    message2 = "python "+sys.argv[0]+" -n iterations"
    message3 = "python "+sys.argv[0]+" rows cols"
    print("Incorrect usage. See examples:")
    print message
    print message2
    print message3

def matrix_maker(row,column):
    #n = random.randint(1,101)
    matrix = [[random.randint(1,101) for x in range(row)] for y in range(column)]
    return matrix

def matrix_printer(m):
    rowlen = len(m)
    columnlen = len(m[0])
    if rowlen > 10 or columnlen > 10:
        return                      #will be too many numbers on screen!
    for i in range(rowlen):
        for j in range(columnlen):
            print m[i][j],          #2.7 syntax for inline printing
        print " "

def matrix_sum(m):
    rowlen = len(m)
    columnlen = len(m[0])
    sum = 0
    start = datetime.datetime.now()
    for i in range(rowlen):
        for j in range(columnlen):
            sum = sum + m[i][j]
    end = datetime.datetime.now()
    delta = end.microsecond - start.microsecond
    return sum, delta

def thread_helper(l):
    sum = 0
    global global_sum
    for i in range(len(l)):
        sum = sum + l[i]
    mutex.acquire()          #grab lock
    try:
        global_sum = global_sum + sum    #critical zone
    finally:
        mutex.release()     #release

def threaded_matrix_sum(m):
    rowlen = len(m)
    sum = 0
    threads = []
    start = datetime.datetime.now()
    for row in m:
        t = threading.Thread(target=thread_helper, args=(row,))
        threads.append(t)
        t.start()
    for row in m:
        threads.pop().join()
    end = datetime.datetime.now()
    delta = end.microsecond - start.microsecond
    return delta

def handler(x,y):
    print("running...")
    mat = matrix_maker(x,y)
    matrix_printer(mat)
    sum,time = matrix_sum(mat)
    print("sum: "+str(sum)+" time taken: "+str(time)+"microseconds")
    threadtime = threaded_matrix_sum(mat)
    print("threaded sum: "+str(global_sum)+" time taken: "+str(threadtime)+"microseconds")
    #assert time == threadtime, "singular and thread sumnations do not match"
    if threadtime > time:
        print("single sumnation was faster")
    else:
        print("threaded sumnation was faster")

def limit_finder():
    print("running limit_finder...")
    for n in range(1000,1500,5):        #do in inc of 100
        mat = matrix_maker(n,n)
        matrix_printer(mat)
        sum,time = matrix_sum(mat)
        threadtime = threaded_matrix_sum(mat)
        #assert time == threadtime, "singular and thread sumnations do not match"
        if threadtime < time:
            print("threaded sumnation is faster than singular with matrix dimensions of "+str(n))
            return

if '-n' in sys.argv:
    iters = int(sys.argv[2])
    for n in range(iters):
        limit_finder()
elif len(sys.argv) == 3:
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    handler(rows,cols)
elif len(sys.argv) < 2:
    limit_finder()
else:
    usage()
