from flask import abort, request
from logging.config import fileConfig
# import requests
import time
 
# file containing app log settings used for logging server logs with custom messages
fileConfig('./mainModules/disasterPrevention/logging.cfg')
# fileConfig(os.path.join(sys.path[0], "docs/mainModules/disasterPrevention/logging.cfg"))

def applogger(message):
	app.logger.info(message)






# ip whitelist method
def ipcheck():
	clientip=request.remote_addr
	clientip=request.environ['REMOTE_ADDR']
	iplist=["13.234.34.84","13.127.190.17"]
	
	if clientip not in iplist:
		abort(403)
		return ("Unknown user")



# time to leave method
def timeoutcheck(clienttimestamp):
	endtime=clienttimestamp+30
	nowtime=time.time()
	if nowtime>endtime:
		abort(400, "timeoutcheck")

