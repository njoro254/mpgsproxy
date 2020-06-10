from flask import Blueprint

from prints.services.forex.api import ForexAPI

forex_app = Blueprint("forex_app", __name__)

forex_view = ForexAPI.as_view('forex_api')
forex_app.add_url_rule(
	'/forex', 
	view_func=forex_view, 
	methods=['POST', ]
	)

