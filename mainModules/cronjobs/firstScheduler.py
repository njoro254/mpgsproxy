import atexit
from apscheduler.scheduler import Scheduler


cron = Scheduler (daemon= True )


cron.start()
@cron.interval_schedule(seconds= 1)
def job_function(function):
	print ('twende')
	
atexit.register( lambda : cron.shutdown(wait= False))

# sample cron job method to be at routes
