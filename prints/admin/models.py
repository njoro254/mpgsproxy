from application import db


class APIkey(db.Document):
	username=db.ReferenceField(db_field="username")
	apikey=db.StringField(db_field="apikey")

class EmailVerificationTokens(db.Document):
	username=db.ReferenceField(db_field="username")
	transactionType=db.StringField(db_field="transactionType")
	timeOfRequest=db.IntegerField(db_field="timeOfRequest")
	emailToken=db.StringField(db_field="emailToken")
	encrypt_key=db.StringField(db_field="encrypt_key")