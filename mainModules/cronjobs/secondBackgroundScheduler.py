from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
def sensor():
""" Function for test purposes. """


sched = BackgroundScheduler(daemon= True )
sched.add_job(sensor, 'interval', minutes= 60 )
sched.start()

# sample cron job method to be called mid scripts