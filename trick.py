#!/usr/bin/env 
python import os 
import random as random 
from time import sleep 
file = open("greenDOT.txt", "w") 
dot = random.random()*100 
file.write(str(dot)) 
file.close() 
sleep(0.1) 
os.chdir("/home/putus/val") 
os.system("git add greenDOT.txt") 
os.system("git commit -m "modified"") 
os.system("git push") 
