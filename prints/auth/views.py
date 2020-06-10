from flask import Blueprint

from prints.auth.api import NewBusinessRegistrationAPI, GetTokenLogInAPI

auth_app = Blueprint("auth_app", __name__)


# NEW BUSINESS ENDPOINT URL
newBusinessRegistration_view = NewBusinessRegistrationAPI.as_view('newBusinessRegistration_api')

auth_app.add_url_rule('/auth/signup', 
	view_func=newBusinessRegistration_view, 
	methods=['POST', 'GET' ])




# APP GET TOKEN ENDPOINT URL
GetTokenLogIn_view = GetTokenLogInAPI.as_view('GetTokenLogIn_api')
auth_app.add_url_rule('/auth/token', 
	view_func=GetTokenLogIn_view, methods=['POST', ])
