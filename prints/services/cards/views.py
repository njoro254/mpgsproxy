from flask import Blueprint

from prints.services.cards.api import InvoiceAPI, BillCheckOutAPI

card_app = Blueprint("card_app", __name__)

invoice_view = InvoiceAPI.as_view('invoice_api')
card_app.add_url_rule('/card/invoice', view_func=invoice_view, methods=['POST', ])


billCheckOut_view = BillCheckOutAPI.as_view('BillCheckOut_api')
card_app.add_url_rule('/card/checkout', view_func=billCheckOut_view, methods=['POST', ])
