from flask.views import MethodView
from flask import jsonify,request,abort
from prints.services.kyc.models import kyc
import requests, json
from prints.services.cards.functionExtra import get_apitoken
from prints.auth.decorators import auth_required
from datetime import date
# from mainModules.disasterPrevention.mylogger import applogger

class KYCAPI(MethodView):

    decorators = [auth_required]

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def post(self):
    	identityDocumentType=request.json["identity"]["documentType"]
    	firstName=request.json["identity"]["firstName"]
    	lastName=request.json["identity"]["lastName"]
    	dateOfBirth=request.json["identity"]["dateOfBirth"]
    	identityDocumentNumber=request.json["identity"]["documentNumber"]
    	countryCode=request.json["identity"]["countryCode"]

        # applogger("new kyc app request")

    	newkyc=kyc(
			identityDocumentType=identityDocumentType,
			firstName=firstName,
			lastName=lastName,
			dateOfBirth=dateOfBirth,
			identityDocumentNumber=identityDocumentNumber,
			countryCode=countryCode
			)

    	newkyc.save()

    	kyctext={
    	"identity":
    	{
    	"documentType":identityDocumentType,
    	"firstName":firstName,
    	"lastName":lastName,
    	"dateOfBirth":dateOfBirth,
    	"documentNumber":identityDocumentNumber,
    	"countryCode":countryCode
    	}
    	}

    	newkyctext=json.dumps(kyctext)

    	return newkyctext