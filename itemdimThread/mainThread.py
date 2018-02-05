import threading
import time
import randomseed1
import randomseed2

class weightThread (threading.Thread):
   def __init__(self, threadID, name, run_event):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.run_event = run_event

   def run(self):
      print "Starting " + self.name
      randomseed1.weightScan(self.run_event)
      print "Exiting " + self.name

class dimensionThread (threading.Thread):
   def __init__(self, threadID, name, run_event):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.run_event = run_event

   def run(self):
      print "Starting " + self.name
      randomseed2.dimensionScan(self.run_event)
      print "Exiting " + self.name


def main():
      run_event = threading.Event()
      run_event.set()
      
      # Create new threads
      thread1 = weightThread(1, "weight-Thread", run_event)
      thread2 = dimensionThread(2, "dimension-Thread", run_event)

      # Start new Threads
      thread1.start()
      thread2.start()

      try:
            while 1:
                  time.sleep(.1)
      except KeyboardInterrupt:
            print "attempting to close threads."
            run_event.clear()
            thread1.join()
            thread2.join()
            print "threads successfully closed"

if __name__ == '__main__':
    main()