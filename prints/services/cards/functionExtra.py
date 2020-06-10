import datetime
from prints.auth.models import AccessTokens, AccessTokensMPGS
import requests

def utc_now_ts():
	return int(time.time())

def get_token():
	authorization="Basic MU4zdmxTUWxGSnhkaFI4cVZWWkM2ZDhhdlNSUnBZSE06SWhHcHhtRGJUdnNGRXU3Mg=="
	headers={
	"Authorization":authorization,
	"Content-Type":"application/x-www-form-urlencoded", 
	"grant_type":"password"
	}

	merchantCode="4390303924"
	password="D0xcxZvC1C4oOlm1uHYWr18QzSJqU7lle"

	body={
	"merchantCode":merchantCode, 
	"password":password
	}

	url='https://api.equitybankgroup.com/v1/token'

	resp = requests.post(
	url=url, 
	headers=headers, 
	data=body
	)

	drone = resp.json()

	print (drone)
	bearer_token='Bearer '+drone.get("payment-token")
	notification_secret=drone.get("notification-secret")

	print ('Your bearer token is: ' + bearer_token)

	seconds2=datetime.datetime.now()
	endtime=seconds2+datetime.timedelta(seconds=3600)
	status='valid'
	newtoken = AccessTokensMPGS(
		token=bearer_token,
		endtime=endtime,
		status=status,
		notification_secret=notification_secret
		)

	newtoken.save()

	authorization=bearer_token
	
	return authorization



def get_apitoken():
	authorization="Basic NVBOZHJZeE5QVmRVVFVxOTBjeTVOaGI0WXhIQXhBbHg6UlZYTkxveEZVakE5UXFhcA=="
	headers={
	"Authorization":authorization,
	"Content-Type":"application/x-www-form-urlencoded", 
	"grant_type":"password"
	}

	username="4390303924"
	password="D0xcxZvC1C4oOlm1uHYWr18QzSJqU7lle"

	body={
	"username":username, 
	"password":password
	}

	url='https://api.jengahq.io/identity/v2/token'

	resp = requests.post(
	url=url, 
	headers=headers, 
	data=body
	)

	drone = resp.json()

	print (drone)
	bearer_token='Bearer '+drone.get("access_token")
	notification_secret=drone.get("notification-secret")

	print ('Your bearer token is: ' + bearer_token)

	seconds2=time.time()
	endtime=seconds2+3600
	endtime=str(endtime)
	seconds2=str(seconds2)
	status='valid'
	newtoken = AccessTokens(
		username=username,
		token=bearer_token, 
		seconds2=seconds2,
		expires=endtime,
		status=status,
		)

	newtoken.save()
	
	authorization=bearer_token
	
	return authorization 



def datetime_format():
	timeOfRegistration=datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
	seconds=time.mktime(timeOfRegistration.timetuple())
	return timeOfRegistration, seconds
