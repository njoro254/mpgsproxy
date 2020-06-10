from flask import Flask
from flask_mongoengine import MongoEngine

from subprocess import call

from settings import MONGODB_SETTINGS

db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load Config File
    app.config.from_pyfile('settings.py')

    # Apply Overrides for tests
    app.config.update(config_overrides)

    # Set up db
    db.init_app(app)

    # import blueprints
    from prints.admin.views import admin_app
    from prints.auth.views import auth_app
    from prints.landingPages.views import landingPages_app
    from prints.pagesMembers.views import pagesMembers_app
    from prints.reports.views import reports_app
    from prints.profile.views import profile_app
    from prints.myLogs.views import myLogs_app

    from prints.services.cards.views import card_app    

    from prints.services.sendmoney.views import sendmoney_app
    from prints.services.receivemoney.views import receivemoney_app
    
    from prints.services.credit.views import credit_app
    from prints.services.forex.views import forex_app
    from prints.services.kyc.views import kyc_app
    
    
    # register blueprints
    app.register_blueprint(admin_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(landingPages_app)
    app.register_blueprint(pagesMembers_app)
    app.register_blueprint(profile_app)
    app.register_blueprint(reports_app)
    app.register_blueprint(myLogs_app)

    app.register_blueprint(card_app)

    app.register_blueprint(sendmoney_app)
    app.register_blueprint(receivemoney_app)
    
    app.register_blueprint(forex_app)
    app.register_blueprint(kyc_app)
    app.register_blueprint(credit_app)
    

    return app