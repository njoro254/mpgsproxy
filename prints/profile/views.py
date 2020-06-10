from flask import Blueprint

from prints.profile.api import MyProfileAPI, EditProfilePageAPI, CredentialsAPI, ServicesActiveAPI

profile_app = Blueprint("profile_app", __name__)


# THE PROFILE DISPLAY ENDPOINT URL
myProfile_view = MyProfileAPI.as_view('MyProfile_api')
profile_app.add_url_rule('/profile', 
	view_func=myProfile_view, 
	methods=['POST','GET' ])



# EDIT PROFILE  ENDPOINT URL
editProfile_view = EditProfilePageAPI.as_view('EditProfile_api')
profile_app.add_url_rule('/profile/edit', 
	view_func=editProfile_view, 
	methods=['POST','GET' ])


# CREDENTIALS URL
credentials_view = CredentialsAPI.as_view('Credentials_api')
profile_app.add_url_rule('/profile/credentials', 
	view_func=credentials_view, 
	methods=['POST','GET' ])


# ACTIVE SERVICES ENDPOINT URL
services_view = ServicesActiveAPI.as_view('ServicesActive_api')
profile_app.add_url_rule('/profile/servicesactive', 
	view_func=services_view, 
	methods=['POST','GET' ])