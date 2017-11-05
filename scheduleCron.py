from crontab import CronTab 
my_cron = CronTab(user='admin') 
job = my_cron.new(command='bash /home/putus/val/trick.sh') 
job.minute.every(58) 
my_cron.write()