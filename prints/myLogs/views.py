from flask import Blueprint

from prints.myLogs.api import TransactionHistoryLogAPI, AccessLogPI, TokenLogAPI, UserLoginLogAPI, AccountActivityLogAPI, OutboundMailLogAPI

myLogs_app = Blueprint("myLogs_app", __name__)

transactionhistory_view = TransactionHistoryLogAPI.as_view('transactionhistory_api')
myLogs_app.add_url_rule('/logs/signup', view_func=transactionhistory_view, methods=['POST', ])


accesslog_view = AccessLogPI.as_view('accesslog_api')
myLogs_app.add_url_rule('/logs/accesslog', view_func=accesslog_view, methods=['POST', ])

tokenlog_view = TokenLogAPI.as_view('tokenlog_view')
myLogs_app.add_url_rule('/logs/tokenlog', view_func=tokenlog_view, methods=['POST', ])


userloginlog_view = UserLoginLogAPI.as_view('userloginlog_api')
myLogs_app.add_url_rule('/logs/userloginlog', view_func=userloginlog_view, methods=['POST', ])

accountactivity_view = AccountActivityLogAPI.as_view('accountactivity_api')
myLogs_app.add_url_rule('/logs/accountactivity', view_func=accountactivity_view, methods=['POST', ])

outboundmail_view = OutboundMailLogAPI.as_view('outboundmail_api')
myLogs_app.add_url_rule('/logs/outboundmail', view_func=outboundmail_view, methods=['POST', ])
