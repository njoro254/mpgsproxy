from application import db


class pesalinkbank(db.Document):
   pesalinkbankid=db.StringField(db_field="pe")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname",max_length=100)
   destinationaccountNumber=db.StringField(db_field="destinationaccountNumber")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference",max_length=12)
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description",max_length=100)



# create table of all source objects
class pesalinkmobile(db.Document):
   pesalinkmobileid=db.StringField(db_field="pesalinkmobile")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname", max_length=100)
   bankCode=db.StringField(db_field="bankCode")
   destinationmobileNumber=db.StringField(db_field="destinationmobileNumber")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference")
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description", max_length=100)

   

# create table of all source objects
class widthdrawtomobile(db.Document):
   widthdrawtomobileid=db.StringField(db_field="widthdrawtomobileid")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname", max_length=100)
   destinationmobileNumber=db.StringField(db_field="destinationmobileNumber")
   walletName=db.StringField(db_field="walletName")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference")
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description", max_length=100)

  

class widthdrawtoequity(db.Document):
   widthdrawtoequityid=db.StringField(db_field="widthdrawtoequityid")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname", max_length=100)
   destinationaccountNumber=db.StringField(db_field="destinationaccountNumber")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference")
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description", max_length=100)


# create table of all source objects
class rtgs(db.Document):
   rtgsid=db.StringField(db_field="rtgsid")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname", max_length=100)
   bankCode=db.StringField(db_field="bankCode")
   destinationaccountNumber=db.StringField(db_field="destinationaccountNumber")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference")
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description", max_length=100)


class eft(db.Document):
   eftid=db.StringField(db_field="eftid")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname", max_length=100)
   bankCode=db.StringField(db_field="bankCode")
   branchCode=db.StringField(db_field="branchCode")
   destinationaccountNumber=db.StringField(db_field="destinationaccountNumber")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference")
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description", max_length=100)



class swift(db.Document):
   swiftid=db.StringField(db_field="swiftid")
   sourcecountryCode=db.StringField(db_field="sourcecountryCode")
   sourcename=db.StringField(db_field="sourcename")
   sourceaccountNumber=db.StringField(db_field="sourceaccountNumber")
   destinationtype =db.StringField(db_field="destinationtype", max_length=100)
   destinationcountryCode=db.StringField(db_field="destinationcountryCode", max_length=3)
   destinationname=db.StringField(db_field="destinationname", max_length=100)
   bankBic=db.StringField(db_field="bankBic")
   destinationaccountNumber=db.StringField(db_field="destinationaccountNumber")
   addressline1=db.StringField(db_field="addressline1")
   transfertype=db.StringField(db_field="transfertype", max_length=100)
   amount=db.StringField(db_field="amount")
   currencyCode=db.StringField(db_field="currencyCode", max_length=3)
   reference=db.StringField(db_field="reference")
   date=db.StringField(db_field="date")
   description=db.StringField(db_field="description", max_length=100)
   chargeOption=db.StringField(db_field="chargeOption")

