import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


import uuid

# def randomizer():
# 	external_id=str(uuid.uuid4())
# 	first_name=str(uuid.uuid4())
# 	last_name=str(uuid.uuid4())
# 	username=str(uuid.uuid4())
# 	email=str(uuid.uuid4())
# 	passwordhash=str(uuid.uuid4())
# 	company=str(uuid.uuid4())
# 	company_position=str(uuid.uuid4())
# 	location=str(uuid.uuid4())
# 	website=str(uuid.uuid4())

# 	obj=[external_id,first_name, last_name, username, email, passwordhash, company, company_position, location, website]

# 	print (obj)

# def print_date_time():
# 	print(time.strftime( "%A, %d. %B %Y %I:%M:%S %p" ))
# def bazeng():
#         print(" Wewe ndiye bazeng bazeng")
        
	
scheduler = BackgroundScheduler()
# scheduler.add_job(func=print_date_time, trigger= "interval" , seconds=1)
# scheduler.add_job(func=bazeng, trigger= "interval" , seconds=1)
# scheduler.add_job(func=randomizer, trigger= "interval" , seconds=1)
scheduler.start()
# Shut down the scheduler when exiting the app
atexit.register( lambda : scheduler.shutdown())

# sample cron job method to be called mid scripts

