from flask import Blueprint

from prints.reports.api import AccountAlertsAPI

reports_app = Blueprint("reports_app", __name__)

accountalerts_view = AccountAlertsAPI.as_view('accountalerts_api')

reports_app.add_url_rule('/alerts', 
	view_func=accountalerts_view, 
	methods=['POST'])


