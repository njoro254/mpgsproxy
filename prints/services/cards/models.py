from application import db
import time 

def now():
  time.time()

class invoice(db.Document):
   customerName=db.StringField(db_field="customerName", required=True)
   timeOfRequest=db.StringField(db_field="timeOfRequest", default=now())
   reference=db.StringField(db_field="reference", required=True)
   amount=db.StringField(db_field="amount", required=True)
   currency=db.StringField(db_field="currency", required=True)
   channel=db.StringField(db_field="channel", required=True)
   description=db.StringField(db_field="description", required=True)
   outlet=db.StringField(db_field="outlet", required=True)
   billerCode=db.StringField(db_field="billerCode", required=True)

   meta = {
        'indexes' : ['customerName', 'amount', '-timeOfRequest']
    }

class cardPay(db.Document):
   token=db.StringField(db_field="passwordhash", required=True)
   timeOfRequest=db.StringField(db_field="timeOfRequest", default=now())
   outletCode=db.StringField(db_field="outletCode", required=True)
   merchantCode=db.StringField(db_field="merchantCode", required=True)
   billamount=db.StringField(db_field="billamount", required=True)
   orderReference=db.StringField(db_field="orderReference", required=True)
   billReference=db.StringField(db_field="billReference", required=True)
   productType=db.StringField(db_field="productType", required=True)
   productDescription=db.StringField(db_field="productDescription", required=True)
   serviceDate=db.StringField(db_field="serviceDate", required=True)
   customerFirstName=db.StringField(db_field="customerFirstName", required=True)
   customerLastName=db.StringField(db_field="customerLastName", required=True)
   cardNumber=db.StringField(db_field="cardNumber")
   country=db.StringField(db_field="country", required=True)
   emailAddress=db.StringField(db_field="endtime", required=True)
   mobileNumber=db.StringField(db_field="mobileNumber", required=True)
   postalcodeZip=db.StringField(db_field="postalcodeZip", required=True)
   address=db.StringField(db_field="address", required=True)
   city=db.StringField(db_field="city", required=True)
   callbackUrl=db.StringField(db_field="callbackUrl", required=True)
   


   meta = {
        'indexes' : ['billReference', 'emailAddress', 'billamount', '-timeOfRequest']
    }
          # token = token,
    # outletCode = 0000000000,
    # merchantCode = 1039000136,
    # bllamount = 10.35,
    # orderReference = 14071950,
    # billReference = D87A3W,
    # productType = construction,
    # productDescription = cement, 
    # serviceDate = 12/09/2019,
    # customerFirstName = Mark,
    # customerLastName = Njoroge,
    # cardNumber = ,
    # cardSecurity = ,
    # cardExpiryYear = ,
    # cardExpiryMonth = ,
    # country = KENYA,
    # mobileNumber = +254700846598,
    # emailAddress = marknjoroge.m@gmail.com,
    # postalcodeZip = 00621,
    # address = 1017,
    # city = NAIROBI,
    # callbackUrl =