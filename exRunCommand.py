#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:38:23 2018

@author: isaaclera
"""

import subprocess 
import os
import logging
import time

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)
logging.info("Loading data")
    
print os.getcwd()


#see https://docs.python.org/3/library/subprocess.html#module-subprocess    
def runCommand(arg1,arg2):
    path = os.getcwd()
    cmd = ["python",path+"/fib.py",str(arg1),arg2+"/"]
    proc = subprocess.Popen(cmd)
    return proc


pathTMP = "/mydirectory_"

status = {}
for i in range(2):
    datestamp = time.strftime('%Y%m%d%H%M%S')
    dname = os.getcwd()+pathTMP+datestamp
    logging.info("Creating directory: "+ dname)
    os.makedirs(dname)
    process = runCommand(30,dname) #TODO catch control error in running command
    logging.info("Running process PID: %i"%process.pid)
    status[i]={"dir":dname,"p":process,"time":datestamp}
    time.sleep(1)


#Aquest bucle ha de veure si n'hi ha file in a directori
while len(status)>0:
    for k in status.keys():
        if status[k]["p"].poll() is None:
            logging.info(" Process %i is still running "%k)
            #TODO kill?
            #control automatic kill in case of authorization or deadline or performance saturation
            # .terminate()
                
        else:
            logging.info(" Process %i has finished"%k)
            status.pop(k, None)

    time.sleep(5)
        
    
    
        



