from flask.views import MethodView
from flask import jsonify,request,abort
import json, requests
from datetime import date
from prints.services.credit.models import Credit
from prints.services.cards.functionExtra import get_apitoken
from prints.auth.decorators import auth_required
# from mainModules.disasterPrevention.mylogger import applogger

class CreditAPI(MethodView):


    decorators = [auth_required]

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
           authorization=request.headers.get('Authorization')
           customerid=request.json['customer'][0]['id']
           fullName=request.json['customer'][0]['fullName']
           firstName=request.json['customer'][0]['firstName']
           lastName=request.json['customer'][0]['lastName']
           shortName=request.json['customer'][0]['shortName']
           title=request.json['customer'][0]['title']
           mobileNumber=request.json['customer'][0]['mobileNumber']
           dateOfBirth=request.json['customer'][0]['dateOfBirth']
           identityDocumentdocumentType=request.json['customer'][0]['identityDocument']['documentType']
           identityDocumentdocumentNumber=request.json['customer'][0]['identityDocument']['documentNumber']
           bureaucountryCode=request.json['bureau']['countryCode']
           bureaureportType=request.json['bureau']['reportType']
           loanamount=request.json['loan']['amount']

           # applogger("credit request from ECH app")


           # adding source details to lipanampesa table
           newcreditscore=Credit(
            customerid=customerid,
            fullName=firstName, 
            firstName=firstName, 
            lastName=lastName, 
            shortName=shortName, 
            title=title, 
            mobileNumber=mobileNumber, 
            dateOfBirth=dateOfBirth, 
            identityDocumentdocumentType=identityDocumentdocumentType, 
            identityDocumentdocumentNumber=identityDocumentdocumentNumber, 
            bureaureportType=bureaureportType, 
            bureaucountryCode=bureaucountryCode, 
            loanamount=loanamount)
           
           newcreditscore.save()

           creditscoretext= {
           "customer":
           [{
           "customerid":customerid, 
           "fullName":fullName, 
           "firstName":firstName, 
           "lastName":lastName, 
           "shortName":shortName, 
           "title":title, 
           "mobileNumber":mobileNumber, 
           "dateOfBirth":dateOfBirth
           }],
           "identity":
           {
           "identityDocumentdocumentType":identityDocumentdocumentType, 
           "identityDocumentdocumentNumber":identityDocumentdocumentNumber
           },
           "bureau":
           { 
           "bureaureportType":bureaureportType, 
           "bureaucountryCode":bureaucountryCode
           }, 
           "loanamount":loanamount
           }

           creditscoretext=json.dumps(creditscoretext)

           return creditscoretext

           # authorization=get_apitoken()[0]

           url='https://uat.jengahq.io/customer-test/v2/creditinfo'


           creditscoreheaders={
           "Authorization":authorization,
           "Content-Type":"application/json"
           }
           
           headers= dict(creditscoreheaders)
           
           resp = requests.post(
            url=url, 
            headers=headers, 
            data=creditscoretext
            )

           data = resp.content
           return data