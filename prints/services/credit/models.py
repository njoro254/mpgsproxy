from application import db


class Credit(db.Document):
   customerid=db.StringField(db_field="customerid")
   fullName=db.StringField(db_field="fullName")
   firstName=db.StringField(db_field="firstName")
   lastName=db.StringField(db_field="lastName")
   shortName=db.StringField(db_field="shortName ")
   title=db.StringField(db_field="title")
   mobileNumber=db.StringField(db_field="mobileNumber")
   dateOfBirth=db.StringField(db_field="dateOfBirth")
   identityDocumentdocumentType=db.StringField(db_field="identityDocumentdocumentType")
   identityDocumentdocumentNumber=db.StringField(db_field="identityDocumentdocumentNumber")
   bureaureportType=db.StringField(db_field="bureaureportType")
   bureaucountryCode=db.StringField(db_field="bureaucountryCode")
   loanamount=db.StringField(db_field="loanamount")