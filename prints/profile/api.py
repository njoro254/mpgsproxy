from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort
from flask.views import MethodView
from flask import request, abort, jsonify
from datetime import datetime, timedelta
from flask_mongoengine import MongoEngine
from prints.auth.models import Business 
import json
# from mainModules.disasterPrevention.mylogger import applogger



class MyProfileAPI(MethodView):

    def __init__(self):
        # If the request doesnt contain json abort
        if (request.method != 'GET') and not request.json:
            abort(400)


    def get(self):
        myprofilequery = Business.objects(username=session.get('username'))
        # profileData=myprofilequery.as_pymongo()
        profileIntermediate=json.loads(myprofilequery.to_json())
        # print (type(profileData))
        profileData=profileIntermediate[0]
        print (type(profileData))
        print (profileData)
        # applogger("new profile page get request")
        return render_template("profile.html", data=profileData)

        
    def post(self):
        pass




class EditProfilePageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)

    
    def get(self):
        # applogger("new edit profile post request")
        return render_template("profile.html", form=ProfileForm)


    def post(self):
        myprofilequery = Business.objects.filter(username=session.get('username')).first()
        
        if (request.method != 'GET') and not request.json:
            abort(400)

        # applogger("new edit profile post request")
        if request.json['first_name'] !=None:
            myprofilequery.first_name =request.json['first_name']
            myprofilequery.save()
        if request.json['last_name'] !=None:
            myprofilequery.last_name = request.json['last_name']
            myprofilequery.save()
        if request.json['username'] !=None:
            myprofilequery.username = request.json['username']
            myprofilequery.save()
        if request.json['email'] !=None:
            myprofilequery.email = request.json['email']
            myprofilequery.save()
        if request.json['password'] !=None:
            digest = SHA256.new()
            digest.update(request.json['password'])
            myprofilequery.passwordhash = digest.hexdigest()
            myprofilequery.save()
        if request.json !=None:
            myprofilequery.location =request.json['location']
            myprofilequery.save()
        if request.json !=None:
            myprofilequery.website =request.json['website']
            myprofilequery.save() 

    
class CredentialsAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)

   # get api key and show username
    def get(self):
        credentialsDate=[]
        # applogger("new profile page request")
        return render_template("profile.html", data=credentialsData)

    def post(self):
        pass


class ServicesActiveAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)

    
    def get(self):
        # applogger("new active services request ")
        servicesActiveData=[]
        return render_template("profile.html", data=servicesActiveData)


    def post(self):
        pass

    

