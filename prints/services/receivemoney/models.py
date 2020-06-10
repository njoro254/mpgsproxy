from application import db



class eazzypaypush(db.Document):
   eazzypaypushid=db.IntField(db_field="eazzypaypushid")
   mobileNumber=db.StringField(db_field="mobileNumber")
   countryCode=db.StringField(db_field="countryCode")
   amount =db.StringField(db_field="amount")
   description=db.StringField(db_field="description")
   transactiontype=db.StringField(db_field="transactiontype")
   reference=db.StringField(db_field="reference")



# create table of all source objects

class lipanampesa(db.Document):
   lipanampesaid=db.IntField(db_field="lipanampesaid")
   mobileNumber=db.StringField(db_field="mobileNumber")
   countryCode=db.StringField(db_field="countryCode")
   amount=db.IntField(db_field="amount")
   description=db.StringField(db_field="description")
   businessNumber=db.IntField(db_field="businessNumber")
   reference=db.StringField(db_field="reference")
