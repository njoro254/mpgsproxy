from flask.views import MethodView
from flask import jsonify,request,abort
from prints.services.forex.models import Forexrates
import requests, json
from prints.services.cards.functionExtra import get_apitoken
from prints.auth.decorators import auth_required
# from mainModules.disasterPrevention.mylogger import applogger


class ForexAPI(MethodView):


    decorators = [auth_required]

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
       authorization=request.headers.get('Authorization')

       countryCode=request.json['countryCode']
       currencyCode=request.json['currencyCode']

       # applogger("new forex request")

       # adding source details to lipanampesa table
       newforexrates=Forexrates(
        countryCode=countryCode, 
        currencyCode=currencyCode)
       newforexrates.save()
       

       forexratestext= {
       "countryCode":countryCode, 
       "currencyCode":currencyCode
       }

       forexratestext=json.dumps(forexratestext)

       # return forexratestext

       get_apitoken()

       url='https://uat.jengahq.io/transaction/v2/foreignexchangerates'


       forexratesheaders={
       "Authorization":authorization,
       "Content-Type":"application/json"
       }

       headers= dict(forexratesheaders)

       resp = requests.post(
        url=url, 
        headers=headers, 
        data=forexratesheaders
        )

       data = resp.content
       return data