#!/usr/bin/env python

import threading
from random import randint

Array = [randint(0,1000) for i in range(1000)]
print Array


class myThread(threading.Thread):
	"""docstring for """

	def Run(self, rlimit, llimit):
	 	print self.getName() 
 		print max(Array[rlimit:llimit])
 		return max(Array[rlimit:llimit])

threadsResults = {}

threads  = [] 

for item in xrange(1,20):
	item = myThread()
	threads.append(item)
	
for item in threads:
	item.start()


pool = threading.Semaphore(value=3)

rlimit=0 
llimit=50

for item in threads:
	##Critical pool 
	Area.acquire()
	threadsResults[item.getName()] = item.Run(rlimit,llimit)	
	pool.release()
	## Critical area ^
	rlimit=llimit+1
	llimit+=50 

print "El mayor valor del array es: "
print str(max(threadsResults, key = threadsResults.get)) +" --- "+ str(threadsResults[max(threadsResults, key = threadsResults.get)])
