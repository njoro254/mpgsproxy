from flask import Blueprint

from prints.landingPages.api import HomePageAPI, ServicesPageAPI, AboutPageAPI, ContactUsPageAPI

landingPages_app = Blueprint("landingPages_app", __name__)

home_view = ServicesPageAPI.as_view('home_api')
landingPages_app.add_url_rule('/', view_func=home_view, methods=['POST', 'GET'])


services_view = ServicesPageAPI.as_view('services_api')
landingPages_app.add_url_rule('/services', view_func=services_view, methods=['POST', 'GET'])



about_view = AboutPageAPI.as_view('about_api')
landingPages_app.add_url_rule('/about', view_func=about_view, methods=['POST', 'GET' ])



contactus_view = ContactUsPageAPI.as_view('contactus_api')
landingPages_app.add_url_rule('/contactus', view_func=contactus_view, methods=['POST', 'GET' ])