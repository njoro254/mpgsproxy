from flask.views import MethodView
from flask import jsonify,request,abort
from datetime import date

class TransactionHistoryLogAPI(MethodView):
    # logs all transactions by a user by app id and transaction


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass
     

class AccessLogPI(MethodView):
    # logs the the times app admin has logged in and out


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass



class TokenLogAPI(MethodView):
    # retrieves all token logs


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass



class UserLoginLogAPI(MethodView):


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass




class AccountActivityLogAPI(MethodView):


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass

class OutboundMailLogAPI(MethodView):


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass

class UserPageRequestLogAPI(MethodView):


    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        pass