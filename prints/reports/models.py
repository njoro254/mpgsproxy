from application import db

import time


class AccountAlerts(db.Document):
    customername=db.StringField(db_field="customername")
    customermobileNumber=db.StringField(db_field="customermobileNumber")
    customerreference=db.StringField(db_field="customerreference")
    transactiondate=db.StringField(db_field="transactiondate")
    transactionreference=db.StringField(db_field="transactionreference")
    transactionpaymentMode=db.StringField(db_field="transactionpaymentMode")
    transactionamount=db.StringField(db_field="transactionamount")
    transactiontill=db.StringField(db_field="transactiontill")
    transactionbillNumber=db.StringField(db_field="transactionbillNumber")
    transactionservedBy=db.StringField(db_field="transactionservedBy")
    transactionadditionalInfo=db.StringField(db_field="transactionadditionalInfo")
    bankreference=db.StringField(db_field="bankreference")
    banktransactionType=db.StringField(db_field="banktransactionType")
    bankaccount=db.StringField(db_field="bankaccount")
    timeofalert=db.IntField(db_field="timeofalert", default=time.time())

class AccountInvoiceAlerts(db.Document):
    orderAmount=db.StringField(db_field="orderAmount")
    orderReference=db.StringField(db_field="orderReference")
    orderStatus=db.StringField(db_field="orderStatus")
    message=db.StringField(db_field="message")
    dateTime=db.StringField(db_field="dateTime")
    billReference=db.StringField(db_field="billReference")
    transactionRef=db.StringField(db_field="transactionRef")
    timeofalert=db.IntField(db_field="timeofalert", default=time.time())
