from flask import Blueprint

from prints.services.kyc.api import KYCAPI

kyc_app = Blueprint("kyc_app", __name__)

kyc_view = KYCAPI.as_view('kyc_api')
kyc_app.add_url_rule('/kyc', view_func=kyc_view, methods=['POST', ])
