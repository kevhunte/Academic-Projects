#!usr/bin/python3
import sys

class Process():
    amount = 0

    def __init__(self, pid, arrive, burst):
        self.pid = int(pid)
        self.arrive = int(arrive)
        self.burst = int(burst)
        self.timeUsed = 0

    def __str__(self):
        return f'\npid: {self.pid}\n arrive time: {self.arrive}\n burst time: {self.burst}\n turnaround time: {self.timeUsed}\n'

    def execute(self,num):
        remainingTime = 0
        if num > self.burst:    # for when process does not use all of the time quantum
            remainingTime = num - self.burst
        self.burst = self.burst - num if self.burst - num > 0 else 0    # ternary op. 0 or greater
        self.timeUsed += (num - remainingTime)      # time given - time needed
        return remainingTime

def startProcessing(processes, timeQuantum, alg):
    copy = processes[:]
    if alg == 'RR':     #RoundRobin
        numProcesses = len(processes)
        totalRunTime = 0.0        # += timeQuantum - p.execute(timeQuantum) => time needed this iter
        procExecStartTime = 0.0   # += totalRunTime for each process where timeUsed == 0
        numCycles = 0

        while len(processes) > 0:
            #print('\n\n--------------\n',*processes, 'Quantum: '+str(timeQuantum))    # debugging
            numCycles += 1

            currProc = processes.pop(0) # dequeue and load into CPU

            if currProc.timeUsed == 0:      #first time in CPU
                procExecStartTime += totalRunTime   #start time for each is the overall time it starts at

            remaining = currProc.execute(timeQuantum)   # simulate execution
            processTime = (timeQuantum - remaining)
            # add processTime to everyone in queue to make correct turnaround. Add to time since started => p's that are not zero
            for p in processes:
                if p.timeUsed != 0:
                    p.timeUsed += processTime

            totalRunTime += processTime   # time used this iter

            if currProc.burst > 0:      # enqueue if still needs processing
                processes.append(currProc)

        print('-------------\nFinal:\n',*copy)
        throughput = totalRunTime / numCycles #numProcesses / totalRunTime
        avgWaitTime = procExecStartTime / numProcesses # sum / n => starts when quantum is up, unless process finishes before that time
        utilization = 1 - (avgWaitTime*0.001) ** numProcesses   # scaling for ms in units
        avgTurnAroundTime = sum(p.timeUsed for p in copy) / numProcesses
        print(f'CPU Utilization: {utilization}\nCPU Throughput: {throughput}\nAverage Wait Time: {avgWaitTime}\nAverage Turnaround Time: {avgTurnAroundTime}')

def handler():
    try:
        args = sys.argv
        if(len(args) == 3):
            fname = args[1]
            quantum = args[2]

        processes = []  #will serve as queue
        for i in open(fname,'r').readlines():
            if 'pid' in i:
                continue
            else:                       #inits processes
                parts = i.split(',')
                p = Process(parts[0],parts[1],parts[2])
                processes.append(p)

        processes.sort(key=lambda x: x.arrive)  # sort by arrival time
        print('\nRound Robin Queue start - time quantum: '+quantum+'\n',*processes)

        startProcessing(processes, int(quantum), 'RR')  # RR for RoundRobin

        # CPU utilization = 1 - avgWaitTime^numProcesses
        # CPU throughput = numProcesses / totalRunTime
        # avgWaitTime = sum(procExecStartTime) / numProcesses => starts when quantum is up, unless process finishes before that time
        # avgTurnAroundTime = sum(timeUsed) / numProcesses

    except:
        print('usage:\n\npython3 target.py processes.csv [timeQuantum amount]\n\nPython 3.6 is the runtime used\n')
        print('Error caught - ',sys.exc_info())

handler()
