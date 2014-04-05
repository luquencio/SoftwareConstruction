#!/usr/bin/env python

import datetime
import threading
import time


class MakingThread(threading.Thread):
	def run(self):
		n = datetime.datetime.now()
		print("%s dice Hola Mundo a las: %s \n" % (self.getName(), n) ) 
		time.sleep(10)
		print("%s se va a dormir.\n" % self.getName())

for x in xrange(1,10):
	t = MakingThread()
	t.start()
	t.join()