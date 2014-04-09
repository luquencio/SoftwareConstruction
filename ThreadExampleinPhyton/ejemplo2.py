#!/usr/bin/env python
#Python Enhancement Proposal (PEP)

import datetime
import threading
import time 


class MakingThread(threading.Thread):
	""" HOLA """
	def run(self):
		""" HOLA """
		born = datetime.datetime.now()
		print("%s, Hola Mundo. Naci a las: %s \n" % (self.getName(), born)) 
		time.sleep(3)
		print("%s se va a dormir.\n" % self.getName())

for items in range(1, 10)
:	items = MakingThread()
	items.start()
	#t.join()