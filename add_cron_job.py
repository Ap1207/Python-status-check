from crontab import CronTab

cron = CronTab(user='user')
job = cron.new(command='python3 /path/to/test.py', comment='checkstatus')
job.minute.every(5)

cron.write()
