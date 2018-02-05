from random import *
import time

def testrun(): 
    weight = randint(1, 100)
    print ("Weight :{0}".format(weight))
    return

def weightScan(run_event): 
    while run_event.is_set():
        testrun()
        time.sleep(randint(5,15))