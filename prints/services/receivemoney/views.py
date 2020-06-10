from flask import Blueprint
from prints.services.receivemoney.api import LipanaMPESAAPI, EazzyPayPushAPI




receivemoney_app = Blueprint("receivemoney_app", __name__)


lipanampesa_view = LipanaMPESAAPI.as_view('receivemoney_api')
receivemoney_app.add_url_rule('/receivemoney/lipanampesa', view_func=lipanampesa_view, methods=['POST', ])



eazzypaypush_view = EazzyPayPushAPI.as_view('eazzypaypush_api')
receivemoney_app.add_url_rule('/receivemoney/eazzypaypush', view_func=eazzypaypush_view, methods=['POST', ])
