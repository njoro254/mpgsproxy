# bluprint for apps to get registered and AccessTokens user tokens
from flask_mongoengine.wtf import model_form
from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for
import uuid
from datetime import datetime, timedelta
from prints.auth.models import Business, AccessTokens
from Crypto.Hash import SHA256
from prints.admin.forms import BusinessRegisterForm
# from mainModules.disasterPrevention.mylogger import applogger




class NewBusinessRegistrationAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.form or request.json:
            abort(400)


    # REGISTRATION ENDPOINT /auth/signup/
    def get(self):
        form = BusinessRegisterForm()

        # applogger("new signup get request")

        return render_template('signup.html', form=form)



    def post(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        company = request.form['company_name']
        company_position = request.form['company_position']
        location = request.form['location']
        website = request.form['website']

        # applogger("new signup post request")

        # TODO More Validation to ensure no empty data for all required fields
        if not "username" in request.form and not "email" in request.form:
            error = {
                "USERNAME_OR_EMAIL_IS_MISSING"
            }
            return jsonify({'error': error}), 400



        existing_user = Business.objects.filter(username=username).first()
        existing_email = Business.objects.filter(email=email).first()
        existing_company_name = Business.objects.filter(company=company).first()




        if existing_user:
            error = {
                "code": "USERNAME_IS_TAKEN"
            }
            return jsonify({"error": error}), 400

        elif existing_email:
            error = {
                "code": "EMAIL_IS_ALREADY_IN_USE"
            }
            return jsonify({"error": error}), 400


        elif existing_company_name:
            error = {
                "code": "THIS_company_name_IS_ALREADY_REGISTERED"
            }
            return jsonify({"error": error}), 400


        else:
            # create the Business account
            digest = SHA256.new()
            digest.update(password)
            hashed_password=digest.hexdigest()

            businessEntry = Business(
                external_id=str(uuid.uuid4()),
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                passwordhash=hashed_password,
                company=company,
                company_position=company_position,
                location=location,
                website=website
            ).save()

            return redirect(url_for("landingPages_app.home_api", message="Business registered"))


class GetTokenLogInAPI(MethodView):

    def __init__(self):
        if not request.form:
            abort(400)


    # LOGIN ENDPOINT /auth/login/
    def post(self):
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        # try:
        if not "username" in request.form or not "password" in request.form:
            error = {
                "code": "MISSING_USERNAME_OR_PASSWORD"
            }
            return jsonify({"error": error}), 400

        # Check if user exists
        businessUserMatch = Business.objects.filter(username=username).first()
        if not businessUserMatch:
            error = {
                "code": "USER_DOES_NOT_EXIST"
            }
            return jsonify({"error": error}), 403


        # applogger("new token request")
        digest = SHA256.new()
        digest.update(password)
        hashed_password=digest.hexdigest()
        # print (hashed_password)

        businessUserMatch2 = Business.objects.filter(username=username, passwordhash=hashed_password).first()
        # print (businessUserMatch2)
        biz=Business(username=username)

        # check if password received is correct then generate token
        # if businessUserMatch2:
        #     # delete existing tokens
        #     existing_token = AccessTokens.objects(username=biz).first()
        #     if existing_token.token:
        #         existing_token.delete()
        #     else:
        #         pass
            # uuid generates token
        token = str(uuid.uuid4())
        now = datetime.now()
        
        # token expires after 30days
        expires = now + timedelta(days=30)
    
        # save the AccessTokensTokens token
        AccessTokensObject = AccessTokens.objects.filter(username=username).first()
        # print(AccessTokensObject.username)
        if not AccessTokensObject:
            AccessTokensTokens = AccessTokens(
                username=username,
                token=token,
                expires=expires)
            AccessTokensTokens.save()

        else:
            AccessTokensObject.username=username
            AccessTokensObject.token=token
            AccessTokensObject.expires=expires
            AccessTokensObject.save()


        # api standards to return time formats
        
        return jsonify({"token": token, "expires": expires}), 200


        # except:
        #     error = {
        #         "code": "INCORRECT_CREDENTIALS"
        #     }
        #     return jsonify({"error": error}), 403
