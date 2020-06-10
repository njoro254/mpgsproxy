from application import db
import time 

now=time.time()


class Business(db.Document):
    external_id = db.StringField(db_field="external_id")
    first_name = db.StringField(db_field="first_name", required=True, max_length=50)
    last_name = db.StringField(db_field="last_name", required=True, max_length=50)
    username = db.StringField(db_field="username", unique=True)
    email = db.EmailField(db_field="email", unique= True)
    company = db.StringField(db_field="company",unique=True)
    company_position = db.StringField(db_field="company_position",required=True)
    live = db.BooleanField(db_field="live", default=True)
    timeOfRegistration= db.IntField(db_field="timeOfRegistration", default=now)
    location = db.StringField(db_field="location",default="")
    profile_pic_path = db.StringField(db_field="profile_pic_path",default="")
    website = db.StringField(db_field="website",default="")
    passwordhash=db.StringField(db_field="passwordhash")


class AccessTokens(db.Document):
    # foreign key/reference field in mongo
    username = db.StringField(db_field="username")
    token = db.StringField(db_field="token")
    expires = db.DateTimeField(db_field="expires")
    status=db.StringField(db_field="status")
    seconds2=db.StringField(db_field="seconds2")

class AccessTokensMPGS(db.Document):
    # foreign key/reference field in mongo
    username = db.StringField(db_field="username")
    token = db.StringField(db_field="token")
    endtime = db.DateTimeField(db_field="endtime")
    status=db.StringField(db_field="status")
    notification_secret=db.StringField(db_field="notification_secret")
