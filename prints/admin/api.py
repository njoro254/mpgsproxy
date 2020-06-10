# blueprint for admin login, forgot password and email verification
from flask.views import MethodView
from flask import request, abort, jsonify, session, render_template, redirect, url_for
from Crypto.Hash import SHA256
from datetime import datetime, timedelta
from mainModules.myMailer.emailtome import myMailer
from prints.auth.models import Business
from prints.admin.forms import LoginForm
# from mainModules.disasterPrevention.mylogger import applogger




class AppAdminLogInAPI(MethodView):

    def get(self):
        form = LoginForm()
        return render_template('login.html', form=form)

    #  admin log in endpoint
    def post(self):
        username = request.form['username']
        password = request.form['password']

        form = LoginForm()

        if form.validate:
            pass
        else:
            return render_template('login.html', form=form, error="Incorrect form-inputs format")

        if not "username" in request.form or not "password" in request.form:
            error = {
                "code": "MISSING_USERNAME_OR_PASSWORD"
            }
            return jsonify({"error": error}), 400

        # Check if user exists
        businessrow = Business.objects.filter(username=username).first()
        if not Business:
            error = {
                "code": "USER_DOES_NOT_EXIST"
            }
            return jsonify({"error": error}), 403

        password=password.encode("utf-8")
        digest=SHA256.new()
        digest.update(password)
        # print (digest.hexdigest())
        # print (businessrow.passwordhash)
        if  digest.hexdigest() != businessrow.passwordhash:
            error = {
                "code": "INCORRECT USERNAME OR PASSWORD"
            }
            return jsonify({"error": error}), 403
        else:
            session['username']=businessrow.username
            # applogger(businessrow.username+"currently in session")
            return  redirect(url_for('landingPages_app.home_api'))



    
class AppAdminForgotPasswordAPI(MethodView):

    def __init__(self):
        if not request.form:
            abort(400)

    # forgot password endpoint /admin/forgotpassword
    def get(self):
        # applogger("forgot password getrequest")
        return render_template("forgotpassword.html", form=ForgotPasswordForm)

    def post(self):
        email=request.form['email']
        subject="Recover Password"
        # applogger("new forgot password post request")
        myEncrypter(email+subject)
        body=myEncrypter
        myMailer(email=email, subject=subject, body=body)
        # applogger("new forgot password mail request")
        return redirect()

class ConfirmEmailAPI(MethodView):


    # CONFIRM EMAIL ENDPOINT /admin/confirm/<emailToken>
    def post(self, emailToken):
        myDecrypter(emailToken)
        # applogger("email confirmation request sucess")
        return redirect(url_for('pagesMembers_app.index_api'))

class LogOutAPI(MethodView):

    def get(self):
        session.pop('username', None)
        # applogger("username logged out")
        return redirect(url_for('landingPages_app.home_api'))


    
