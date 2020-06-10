from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort
from flask.views import MethodView
from flask import request, abort, jsonify
from datetime import datetime, timedelta
# from mainModules.disasterPrevention.mylogger import applogger





class MembersHomePageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)
        # if session['logged_in'] == True:
        #     pass
        # else:
        #     abort(400)

    # MEMBERS PAGE /index
    def get(self):
        # applogger("new index page request")
        return render_template("index.html")

    def post(self):
        pass



    
class NotificationsPageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)
        # if session['logged_in'] == True:
        #     pass
        # else:
        #     abort(400)

    # NOTiFICATIONS PAGE /notifications
    def get(self):
        # applogger("new notifications page request")
        return render_template("notifications.html")

    def post(self):
        pass
        

class ReportsPageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)
        # if session['logged_in'] == True:
        #     pass
        # else:
        #     abort(400)

    # REPORTS PAGE /reports
    def get(self):
        # applogger("new reports page request")
        return render_template("reports.html")


    def post(self):
        pass
    

class DownloadsPageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)
        # if session['logged_in'] == True:
        #     pass
        # else:
        #     abort(400)

    # DOWNLOADS PAGE /downloads
    def get(self):
        # applogger("new downloads page request")
        return render_template("downloads.html")


    def post(self):
        pass
        