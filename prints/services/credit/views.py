from flask import Blueprint

from prints.services.credit.api import CreditAPI

credit_app = Blueprint("credit_app", __name__)

credit_view = CreditAPI.as_view('credit_api')
credit_app.add_url_rule('/credit', view_func=credit_view, methods=['POST', ])


