from application import db

class Forexrates(db.Document):
	forexratesid=db.IntField(db_field="forexratesid")
	countryCode=db.StringField(db_field="countryCode")
	currencyCode=db.StringField(db_field="currencyCode")