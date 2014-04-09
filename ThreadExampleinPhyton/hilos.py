#!/usr/bin/env python

import threading
from random import randint

numbers = []

for x in xrange(1,1000):
	numbers.append(randint(0,1000))

class sthread(threading.Thread):
	def findmax(self,a): # a = arreglo
		print self.getName() 
		print len (a)
 		print max(a)
		return max(a)
n1 = 0
n2 = 50
maximo=[]


threadLock = threading.Lock()

for i in xrange(1,20):
	threadLock.acquire()
	t= sthread()
	t.start()
	maximo.append(t.findmax(numbers[n1:n2]))
	threadLock.release()
	n1 = n2+1
	n2 += 51

print "Valor maximo: "
print max(maximo)