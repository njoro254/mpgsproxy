# blueprint for landing pages for unregistered users
from flask.views import MethodView
from flask import request, abort, jsonify, render_template
# from mainModules.disasterPrevention.mylogger import applogger



class HomePageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)


    def get(self):
        # applogger("home page get request")
        return render_template("home.html")

        
    def post(self):
        pass




class ServicesPageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)


    # LOGIN ENDPOINT /auth/login/
    def get(self):
        # applogger("services page get request")
        return render_template("services.html")

    def post(self):
        pass
    
class AboutPageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)
    
    def get(self):
        # applogger("about page get request")
        return render_template("about.html")

    def post(self):
        pass

class ContactUsPageAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)

   
    def get(self):
        # applogger("contact us page get request")
        return render_template("contactus.html")


    def post(self):
        pass
    
 