from flask import Blueprint

from prints.admin.api import AppAdminForgotPasswordAPI, AppAdminLogInAPI, ConfirmEmailAPI, LogOutAPI

admin_app = Blueprint("admin_app", __name__)

forgotpassword_view = AppAdminForgotPasswordAPI.as_view('forgotpassword_api')
admin_app.add_url_rule('/admin/forgotpassword', view_func=forgotpassword_view, methods=['POST', ])


appAdminLogin_view = AppAdminLogInAPI.as_view('appAdminLogin_api')
# LOGIN ENDPOINT URL
admin_app.add_url_rule('/admin/login', view_func=appAdminLogin_view, methods=['POST', 'GET'])


confirmEmailLogin_view = ConfirmEmailAPI.as_view('confirmEmailLogin_api')
# LOGIN ENDPOINT URL
admin_app.add_url_rule('/admin/confirm/<emailToken>', view_func=confirmEmailLogin_view, methods=['POST','GET' ])

logout_view = LogOutAPI.as_view('logout_api')
# LOGIN ENDPOINT URL
admin_app.add_url_rule('/logout', view_func=logout_view, methods=['POST','GET' ])