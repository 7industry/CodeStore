#!/usr/bin/env python     
# -*- coding: UTF-8 -*- 

import threading,time

class myThread(threading.Thread):
  
  def doA(self):
    print(self.name,"gotlockA doA",time.ctime())
    time.sleep(0.1)
  
  def doB(self):
    time.sleep(0.1)
    print(self.name,"gotlockA doB",time.ctime())

  def run(self):
    with lockA:
      self.doA()
      self.doB()
      
      
def select():
  
  for i in range(2):
    t = threading.Thread(target=fib,args=(35,))
    t.start()
    
  main_thread = threading.current_thread()
  
  for t in threading.enumerate():
    if t is main_thread:
      continue
    t.join()
    
    
def update():
  for i in range(2):
    t = threading.Thread(target=fib,args=(35,))
    t.start()
  main_thread = threading.current_thread()
  for t in threading.enumerate():
    if t is main_thread:
      continue
    t.join()      
    
        
if __name__=="__main__":

    lockA=threading.Lock()
    threads=[]
    for i in range(10):
        threads.append(myThread())
        
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
  
        