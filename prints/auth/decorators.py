# On this Decorator, we check if the token passed is valid
from functools import wraps
from flask import jsonify, request
# check token validity
import datetime
import time
# Business models to retrieve Business and AccessTokens token
from prints.auth.models import Business, AccessTokens


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        username = request.headers.get('Username')
        token = request.headers.get('Authorization')

        # If no username or Token in the request
        if username is None or token is None:
            error = {
            "code": "MISSING_USERNAME_OR_AUTHORIZATION_TOKEN"
            }
            return jsonify({"error": error}), 403

        # check if Business username exists
        biz = Business.objects.filter(username=username).first()
        if not biz:
            error = {
                    "code": "USER_DOES_NOT_EXIST"
                }
            return jsonify({"error": error}), 403

        # query the token
        access = AccessTokens.objects.filter(username=username).first()
        if not access:
            error = {
                    "code": "TOKEN_DOES_NOT_EXIST"
                }
            return jsonify({"error": error}), 403
        
        if access.token != token:
            error = {
                    "code": "INVALID_TOKEN"
                }
            return jsonify({"error": error}), 403

        if access.expires < datetime.datetime.now():
            return jsonify({"error": "TOKEN_EXPIRED"}), 403
        
        return f(*args, **kwargs)
    return decorated_function

def get_profile_id():
    username = request.headers.get('Username')
    memberfetch = Member.objects.filter(username=username).first()
    profile_id=memberfetch.external_id
    return profile_id
