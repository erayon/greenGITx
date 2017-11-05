import shutil
from shutil import copyfile
import argparse
import os
import pip
from time import sleep

def install():
    pip.main(['install', "python-crontab"])

def cPATH(dst):
	shutil.copy2('greenDOT.txt', dst) 
	shutil.copy2('trick.py',dst)
	shutil.copy2('scheduleCron.py',dst)
	shutil.copy2('trick.sh',dst)

def cronSchedule(dst):
	c1    = "from crontab import CronTab \n"
	c2    = "my_cron = CronTab(user='admin') \n"
	c3    =  "job = my_cron.new(command='bash "
	c4    = dst +"/trick.sh') \n"
	c5    = "job.minute.every(58) \n"
	c6    = "my_cron.write()"
	c     = c1+c2+c3+c4+c5+c6
	path  = "scheduleCron.py"
	file  = open(path,'w')
	file.write(c)
	file.close

def shellTrick(dst):
	cx    = "#!/bin/sh \n"
	#c1    = "sudo pip install python-crontab\n"
	c2    = "cd "+dst+"\n"
	c3    = "python trick.py \n"
	c     = cx+c2+c3
	path  = "trick.sh"
	file  = open(path,'w')
	file.write(c)
	file.close

def run(dst):
	install()
	cronSchedule(dst)
	shellTrick(dst)
	sleep(0.1)
	deftrick()
	cPATH(dst)

def deftrick():
	c0  = "#!/usr/bin/env \n"
	c1  = "python import os \n"
	c2  = "import random as random \n"
	c3  = "from time import sleep \n" 
	c4  = 'file = open("greenDOT.txt", "w") \n'
	c5  = "dot = random.random()*100 \n"
	c6  = 'file.write(str(dot)) \n'
	c7  = "file.close() \n"
	c8  = "sleep(0.1) \n"
	c9  = 'os.chdir("'+dst+'") \n'
	c10 = 'os.system("git add greenDOT.txt") \n'
	c11 = 'os.system("git commit -m "modified"") \n'
	c12 = 'os.system("git push") \n' 
	ot= c0+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
	path  = "trick.py"
	file  = open(path,'w')
	file.write(ot)
	file.close

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Input_Folder",help=": path of private repo")
    args  = parser.parse_args()
    dst = args.Input_Folder
    run(dst)
