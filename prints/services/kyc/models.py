from application import db


class kyc(db.Document):
   kycid=db.StringField(db_field="kycid")
   identityDocumentType=db.StringField(db_field="identityDocumentType")
   firstName=db.StringField(db_field="firstName")
   lastName=db.StringField(db_field="lastName")
   dateOfBirth=db.StringField(db_field="dateOfBirth")
   identityDocumentNumber=db.StringField(db_field="identityDocumentNumber")
   countryCode=db.StringField(db_field="countryCode")