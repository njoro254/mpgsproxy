from flask.views import MethodView
from flask import jsonify,request,abort
from datetime import date
from prints.services.sendmoney.models import pesalinkbank, pesalinkmobile, widthdrawtoequity, widthdrawtomobile, swift, rtgs, eft
import json, requests
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from mainModules.myCryptoFunction.mySigner import myVerifier
from prints.services.cards.functionExtra import get_apitoken
from prints.auth.decorators import auth_required
# from mainModules.disasterPrevention.mylogger import applogger

class PesalinkBankAPI(MethodView):

   
    decorators = [auth_required]

    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')
       
       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       destinationaccountNumber=request.json['destination']['accountNumber']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']

       

       newPesalinkbank=pesalinkbank(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationname, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            destinationaccountNumber=destinationcountryCode, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description
            )
       newPesalinkbank.save()

       # applogger("new pesalink to bank request")
       

       pesalinkbanktext={
       "source":
       {
       "countryCode":sourcecountryCode, 
       "name":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "name": destinationname,
       "countryCode": destinationcountryCode, 
       "accountNumber":destinationaccountNumber
       }, 
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description}
       }
      
       pesalinkbanktext=json.dumps(pesalinkbanktext)

#       return pesalinkbanktext

       authorization=get_apitoken()[0]

       pesalinkbankconcatenation=amount+currencyCode+reference+destinationname+sourceaccountNumber
       pesalinkbankuft8 = pesalinkbankconcatenation.encode('utf-8') 
       digest = SHA256.new()
       digest.update(pesalinkbankuft8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64

       url='https://uat.jengahq.io/transaction/v2/remittance'

       pesalinkbankheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(pesalinkbankheaders)

       resp = requests.post(
            url=url, 
            headers=headers, 
            data=pesalinkbanktext
            )
       data = resp.content
       return data
       return pesalinkbanktext








class PesalinkMobileAPI(MethodView):

   
    decorators = [auth_required]
    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')

       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       bankCode=request.json['destination']['bankCode']
       destinationmobileNumber=request.json['destination']['mobileNumber']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']

       

       newPesalinkmobile=pesalinkmobile(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationtype, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            bankCode=bankCode, 
            destinationmobileNumber=destinationmobileNumber, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description)
       newPesalinkmobile.save()

       # applogger("new pesalink to mobile request")       

       pesalinkmobiletext={
       "source":
       {
       "countryCode":sourcecountryCode, 
       "name":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "name": destinationname,
       "countryCode": destinationcountryCode, 
       "bankCode":bankCode,
       "mobileNumber":destinationmobileNumber
       }, 
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description}
       }
      
       pesalinkmobiletext=json.dumps(pesalinkmobiletext)

#       return pesalinkmobiletext

       authorization=get_apitoken()[0]

       pesalinkmobileconcatenation=amount+currencyCode+reference+destinationname+sourceaccountNumber
       
       pesalinkmobileutf8 = pesalinkmobileconcatenation.encode('utf-8')
       digest = SHA256.new()
       digest.update(pesalinkmobileutf8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64

       url='https://uat.jengahq.io/transaction/v2/remittance'

       pesalinkmobileheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(receivepaymentsheaders)
       resp = requests.post(url=url, headers=headers, data=pesalinkmobiletext)
       data = resp.content
       return data







class EquityToEquityAPI(MethodView):

   
    decorators = [auth_required]
    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')

       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       destinationaccountNumber=request.json['destination']['accountNumber']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']

       

       newwidthdrawtoequity=widthdrawtoequity(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationtype, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            destinationaccountNumber=destinationaccountNumber, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description
            )
       # adding source details to source table
       newwidthdrawtoequity.save()

       # applogger("new widthdraw to equity request")

       widthdrawtoequitytext={
       "source":
       {
       "countryCode":sourcecountryCode, 
       "name":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "name": destinationname,
       "countryCode": destinationcountryCode,
       "accountNumber":destinationaccountNumber
       },
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description
       }
       }
      
       widthdrawtoequitytext=json.dumps(widthdrawtoequitytext)

#       return widthdrawtoequitytext

       authorization=get_apitoken()[0]

       widthdrawtoequityconcatenation=sourceaccountNumber+amount+currencyCode+reference

       widthdrawtoequityutf8= widthdrawtoequityconcatenation.encode('utf-8')
       digest = SHA256.new()
       digest.update(widthdrawtoequityutf8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64

       url='https://uat.jengahq.io/transaction/v2/remittance'


       widthdrawtoequityheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(widthdrawtoequitytheaders)

       resp = requests.post(
            url=url, 
            headers=headers, 
            data=widthdrawtoequitytext
            )

       data = resp.content
       return data
       return widthdrawtoequitytext






class EquityToMobileAPI(MethodView):

   
    decorators = [auth_required]
    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')

       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       destinationmobileNumber=request.json['destination']['mobileNumber']
       walletName=request.json['destination']['walletName']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']

       

       newwidthdrawtomobile=widthdrawtomobile(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationtype, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            destinationmobileNumber=destinationmobileNumber, 
            walletName=walletName, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description
            )
       # adding source details to source table
       newwidthdrawtomobile.save()

       # applogger("new widthdraw to mobile request")

       widthdrawtomobiletext={
       "source":
       {
       "countryCode":sourcecountryCode, 
       "name":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "name": destinationname,
       "countryCode": destinationcountryCode,
       "mobileNumber":destinationmobileNumber, 
       "walletName":walletName
       }, 
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description
       }
       }
      
       widthdrawtomobiletext=json.dumps(widthdrawtomobiletext)

       # return widthdrawtomobiletext

       authorization=get_apitoken()[0]

       if destinationtype == 'Airtel':
          widthdrawtomobileconcatenation=amount+currencyCode+reference+sourceaccountNumber
       elif destinationtype == 'MPESA':
          widthdrawtomobileconcatenation=amount+currencyCode+reference+sourceaccountNumber
       elif destinationtype == 'Equitel':
          widthdrawtomobileconcatenation=sourceaccountNumber+amount+currencyCode+reference
       else:
          widthdrawtomobileconcatenation=sourceaccountNumber+amount+currencyCode+reference

       widthdrawtomobileutf8 = widthdrawtomobileconcatenation.encode('utf-8') 
       digest = SHA256.new()
       digest.update(widthdrawtomobileutf8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64

       url='https://uat.jengahq.io/transaction/v2/remittance'


       widthdrawtomobiletheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(widthdrawtomobiletheaders)

       resp = requests.post(
            url=url, 
            headers=headers, 
            data=widthdrawtomobiletext
            )

       data = resp.content
       return data
       return widthdrawtomobiletext








class EquitytoEFT(MethodView):

   
    decorators = [auth_required]
    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
       signature=request.headers.get('signature')
#       authorization=request.headers.get('authorization')

       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       bankCode=request.json['destination']['bankCode']
       branchCode=request.json['destination']['branchCode']
       destinationaccountNumber=request.json['destination']['accountNumber']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']



       neweft=eft(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationtype, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            bankCode=bankCode, 
            destinationaccountNumber=destinationaccountNumber, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description
            )
       # adding source details to source table
       neweft.save()

       # applogger("new eft request")

       efttext = {
       "source":
       {
       "countryCode":sourcecountryCode, 
       "name":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "name": destinationname,
       "countryCode": destinationcountryCode, 
       "branchCode":branchCode,
       "bankCode":bankCode,
       "accountNumber":destinationaccountNumber
       }, 
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description
       }
       }  

       efttext=json.dumps(efttext)

#       return efttext

       authorization=get_apitoken()[0]

       eftconcatenation=reference+sourceaccountNumber+destinationaccountNumber+amount+bankCode

       eftutf8 = eftconcatenation.encode('utf-8') 

       digest = SHA256.new()
       digest.update(eftutf8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64

       url='https://uat.jengahq.io/transaction/v2/remittance'


       eftheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(eftheaders)

       resp = requests.post(
            url=url, 
            headers=headers, 
            data=efttext
            )
       data = resp.content
       return data




class EquitytoSWIFT(MethodView):

   
    decorators = [auth_required]
    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
       signature=request.headers.get('signature')
#       authorization=request.headers.get('Authorization')

       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       bankBic=request.json['destination']['bankBic']
       destinationaccountNumber=request.json['destination']['accountNumber']
       addressline1=request.json['destination']['addressline1']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']
       chargeOption=request.json['transfer']['chargeOption']


       newswift=swift(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationtype, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            bankBic=bankBic, 
            destinationaccountNumber=destinationaccountNumber, 
            addressline1=addressline1, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description, 
            chargeOption=chargeOption
            )
       # adding source details to source table
       newswift.save()

       # applogger("new swift request")

       swifttext={
       "source":
       {
       "countryCode":sourcecountryCode, 
       "sourcename":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "destinationname": destinationname,
       "countryCode": destinationcountryCode, 
       "bankBic":bankBic, 
       "accountNumber":destinationaccountNumber, 
       "addressline1":addressline1
       }, 
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description, 
       "chargeOption":chargeOption
       }
       }
      
       swifttext=json.dumps(swifttext)

#       return swifttext

       authorization=get_apitoken()[0]

       swiftconcatenation=reference+date+sourceaccountNumber+destinationaccountNumber+amount

       swiftutf8 = swiftconcatenation.encode('utf-8') 
       digest = SHA256.new()
       digest.update(swiftutf8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64



       url='https://uat.jengahq.io/transaction/v2/remittance'


       swiftheaders={
       "Authorization":authorization,
       "signature":signature, 
       "Content-Type":"application/json"
       }
       headers= dict(swiftheaders)

       resp = requests.post(
            url=url, 
            headers=headers, 
            data=swifttext
            )
       data = resp.content
       return data


class EquitytoRTGS(MethodView):

   
    decorators = [auth_required]
    
    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')

       sourcecountryCode=request.json['source']['countryCode']
       sourcename=request.json['source']['name']
       sourceaccountNumber=request.json['source']['accountNumber']
       destinationtype=request.json['destination']['type']
       destinationname=request.json['destination']['name']
       destinationcountryCode=request.json['destination']['countryCode']
       bankCode=request.json['destination']['bankCode']
       destinationaccountNumber=request.json['destination']['accountNumber']
       transfertype=request.json['transfer']['type']
       amount=request.json['transfer']['amount']
       currencyCode=request.json['transfer']['currencyCode']
       reference=request.json['transfer']['reference']
       date=request.json['transfer']['date']
       description=request.json['transfer']['description']

       

       newrtgs=rtgs(
            sourcecountryCode=sourcecountryCode, 
            sourcename=sourcename, 
            sourceaccountNumber=sourceaccountNumber, 
            destinationtype=destinationtype, 
            destinationname=destinationname, 
            destinationcountryCode=destinationcountryCode, 
            bankCode=bankCode, 
            destinationaccountNumber=destinationaccountNumber, 
            transfertype=transfertype, 
            amount=amount, 
            currencyCode=currencyCode, 
            reference=reference, 
            date=date, 
            description=description
            )
       # adding source details to source table
       newrtgs.save()

       # applogger("new rtgs request")

       rtgstext= {
       "source":
       {
       "countryCode":sourcecountryCode, 
       "name":sourcename, 
       "accountNumber":sourceaccountNumber
       }, 
       "destination":
       {
       "type":destinationtype,
       "name": destinationname,
       "countryCode": destinationcountryCode, 
       "bankCode":bankCode,
       "accountNumber":destinationaccountNumber
       }, 
       "transfer":
       {
       "type":transfertype,
       "amount":amount, 
       "currencyCode":currencyCode, 
       "reference":reference,
       "date":date, 
       "description":description
       }
       }
      
       rtgstext=json.dumps(rtgstext)

#       return rtgstext

       authorization=get_apitoken()[0]

       rtgsconcatenation=reference+date+sourceaccountNumber+destinationaccountNumber+amount

       
       rtgsutf8 = rtgsconcatenation.encode('utf-8') 
       digest = SHA256.new()
       digest.update(rtgsutf8)

       private_key = False
       with open("./mainModules/myCryptoFunction/privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       # return signBase64


       url='https://uat.jengahq.io/transaction/v2/remittance'

       
       rtgsheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(rtgsheaders)

       # myVerifier(digest=digest, signBase64=sigBytes)
       
       resp = requests.post(
            url=url, 
            headers=headers, 
            data=rtgstext
            )

       data = resp.content
       return data
#       return rtgstext
