from crontab import CronTab

my_cron = CronTab(user='user')
my_cron.remove_all(comment='checkstatus')
my_cron.write()
