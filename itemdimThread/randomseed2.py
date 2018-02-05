from random import *
import time

def testrun(): 
    height = randint(1, 100)
    width = randint(1, 100)
    print ("Width: {0} height:{1}".format(width, height) )
    return

def dimensionScan(run_event): 
    while run_event.is_set():
        testrun()
        time.sleep(randint(5,15))