from flask.views import MethodView
from flask import jsonify,request,abort
from prints.auth.decorators import auth_required, get_profile_id
from datetime import date
from prints.services.receivemoney.models import lipanampesa, eazzypaypush
import json, requests
from prints.services.cards.functionExtra import get_apitoken
from prints.auth.decorators import auth_required
# from mainModules.disasterPrevention.mylogger import applogger



class LipanaMPESAAPI(MethodView):


    decorators = [auth_required]

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
       authorization=request.headers.get('Authorization')
       mobileNumber=request.json['customer']['mobileNumber']
       countryCode=request.json['customer']['countryCode']
       amount=request.json['transaction']['amount']
       description=request.json['transaction']['description']
       businessNumber=request.json['transaction']['businessNumber']
       reference=request.json['transaction']['reference']

       # applogger('new lipa na mpesa post request')


       # adding source details to lipanampesa table
       newlipanampesa=lipanampesa(
        mobileNumber=mobileNumber, 
        countryCode=countryCode, 
        amount=amount, 
        description=description, 
        businessNumber=businessNumber, 
        reference=reference
        )
       
       newlipanampesa.save()

       lipanampesatext= {"customer":
       {"mobileNumber":mobileNumber, 
       "countryCode":countryCode}, 
       "transaction":
       {
       "amount":amount, 
       "description":description, 
       "businessNumber":businessNumber, 
       "reference":reference
       }
       }

       lipanampesatext=json.dumps(lipanampesatext)
   #    return lipanampesatext

       authorization=get_apitoken()[0]

       url='https://uat.jengahq.io/transaction/v2/payment/mpesastkpush'


       lipanampesaheaders={
       "Authorization":authorization,
       "Content-Type":"application/json"
       }

       headers= dict(lipanampesaheaders)
       resp = requests.post(
        url=url, 
        headers=headers, 
        data=lipanampesatext)

       data = resp.json()

       if data.get("status")=='Success. Request accepted for processing':
          return 'transaction accepted'
       elif data.get("response_status")=='unauthorized':
          return 'please restart session, wrong bearer token or bearer token has expired'
       else:
          return 'transaction failed. Please retry'

        

class EazzyPayPushAPI(MethodView):


    decorators = [auth_required]

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
   #    authorization=request.headers.get('Authorization')

       mobileNumber=request.json['customer']['mobileNumber']
       countryCode=request.json['customer']['countryCode']
       amount=request.json['transaction']['amount']
       transactiontype=request.json['transaction']['type']
       description=request.json['transaction']['description']
       reference=request.json['transaction']['reference'] 

       # applogger('new eazzy pay post request')  


       # adding source details to source table
       neweazzypaypush=eazzypaypush(
        mobileNumber=mobileNumber, 
        countryCode=countryCode, 
        amount=amount, 
        description=description, 
        transactiontype=transactiontype, 
        reference=reference
        )
       
       neweazzypaypush.save()
       # print (neweazzypaypush)



       eazzypaypushtext = {
       "customer":
       {"mobileNumber":mobileNumber, 
       "countryCode":countryCode
       }, 
       "transaction":
       {"amount":amount, 
       "description":description, 
       "transactiontype":transactiontype, 
       "reference":reference
       }
       }
       eazzypaypushtext=json.dumps(eazzypaypushtext)

       # return eazzypaypushtext

       eazzypayconcatenation=reference+amount+merchantCode+countryCode
       
       eazzypayutf8 = eazzypayconcatenation.encode('utf-8') 
       digest = SHA256.new()
       digest.update(eazzypayutf8)

       private_key = False
       with open("privatekey.pem", "r") as myfile:
           private_key = RSA.importKey(myfile.read())

       signer = PKCS1_v1_5.new(private_key)
       sigBytes = signer.sign(digest)
       signBase64 = b64encode(sigBytes)

       print (signBase64)

       url='https://sandbox.jengahq.io/transaction-test/v2/payments'

       authorization=get_apitoken()[0]



       eazzypayheaders={
       "Authorization":authorization,
       "signature":signBase64, 
       "Content-Type":"application/json"
       }

       headers= dict(eazzypayheaders)

       resp = requests.post(
        url=url, 
        headers=headers, 
        data=eazzypaypushtext
        )

       data = resp.content
       return data

        
