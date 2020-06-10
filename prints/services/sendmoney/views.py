from flask import Blueprint
from prints.services.sendmoney.api import PesalinkBankAPI, PesalinkMobileAPI, EquityToEquityAPI, EquityToMobileAPI, EquitytoEFT, EquitytoRTGS, EquitytoSWIFT




sendmoney_app = Blueprint("sendmoney_app", __name__)

pesalinktobank_view = PesalinkBankAPI.as_view('pesalinktobank_api')
sendmoney_app.add_url_rule('/sendmoney/pesalinktobank', view_func=pesalinktobank_view, methods=['POST', ])



pesalinktomobile_view = PesalinkMobileAPI.as_view(' pesalinktomobile_api')
sendmoney_app.add_url_rule('/sendmoney/pesalinktomobile', view_func=pesalinktomobile_view, methods=['POST', ])



equitytoequity_view = EquityToEquityAPI.as_view('equitytoequity_api')
sendmoney_app.add_url_rule('/sendmoney/equitytoequity', view_func=equitytoequity_view, methods=['POST', ])



equitytomobile_view = EquityToMobileAPI.as_view('equitytomobile_api')
sendmoney_app.add_url_rule('/sendmoney/equitytomobile', view_func=equitytomobile_view, methods=['POST', ])



eft_view = EquitytoEFT.as_view('eft_api')
sendmoney_app.add_url_rule('/sendmoney/eft', view_func=eft_view, methods=['POST', ])



rtgs_view = EquitytoRTGS.as_view('rtgs_api')
sendmoney_app.add_url_rule('/sendmoney/rtgs', view_func=rtgs_view, methods=['POST', ])


swift_view = EquitytoSWIFT.as_view('swift_api')
sendmoney_app.add_url_rule('/sendmoney/swift', view_func=swift_view, methods=['POST', ])