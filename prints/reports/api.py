from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort
from flask.views import MethodView
from flask import request, abort, jsonify
from datetime import datetime, timedelta
from prints.reports.models import AccountAlerts, AccountInvoiceAlerts
# from mainModules.disasterPrevention.mylogger import applogger
import json

class AccountAlertsAPI(MethodView):



    def post(self):
        receiptdictionary=request.get_json()
      
        # print('orderReference' in receiptdictionary)
        # print('transaction' in receiptdictionary)

        if 'transaction' in receiptdictionary:
          customername=request.json["customer"]["name"]
          customermobileNumber=request.json["customer"]["mobileNumber"]
          customerreference=request.json["customer"]["reference"]
          transactiondate=request.json["transaction"]["date"]
          transactionreference=request.json["transaction"]["reference"]
          transactionpaymentMode=request.json["transaction"]["paymentMode"]
          transactionamount=request.json["transaction"]["amount"]
          transactiontill=request.json["transaction"]["till"]
          transactionbillNumber=request.json["transaction"]["billNumber"]
          transactionservedBy=request.json["transaction"]["servedBy"]
          transactionadditionalInfo=request.json["transaction"]["additionalInfo"]
          bankreference=request.json["bank"]["reference"]
          banktransactionType=request.json["bank"]["transactionType"]
          bankaccount=request.json["bank"]["account"]

          newAccountAlerts=AccountAlerts(
                  customername=customername,
                  customermobileNumber=customermobileNumber,
                  customerreference=customerreference,
                  transactiondate=transactiondate,
                  transactionreference=transactionreference,
                  transactionpaymentMode=transactionpaymentMode,
                  transactionamount=transactionamount,
                  transactiontill=transactiontill,
                  transactionbillNumber=transactionbillNumber,
                  transactionservedBy=transactionservedBy,
                  transactionadditionalInfo=transactionadditionalInfo,
                  bankreference=bankreference,
                  banktransactionType=banktransactionType,
                  bankaccount=bankaccount
                  )
          newAccountAlerts.save()

          transactiontext={
          "customerreference":customerreference, 
          "transactionreference":transactionreference, 
          "bankreference":bankreference
          }
          message={
          "transactiontext":transactiontext,
          "status":"ok", 
          "code":200
          }
          message=json.dumps(message)
          return message, 200



      
        elif 'orderReference' in receiptdictionary:
          orderAmount=request.json["orderAmount"]
          orderReference=request.json["orderReference"]
          orderStatus=request.json["orderStatus"]
          message=request.json["message"]
          dateTime=request.json["dateTime"]
          billReference=request.json["billReference"]
          transactionRef=request.json["transactionRef"]

          newAccountInvoice=AccountInvoiceAlerts(
            orderAmount=orderAmount, 
            orderReference=orderReference, 
            orderStatus=orderStatus,
            message=message,
            dateTime=dateTime,
            billReference=billReference,
            transactionRef=transactionRef)
          newAccountInvoice.save()

          # print (orderStatus)

          if orderStatus =="Transaction Failed":
            transactiontext="Transaction failed"
            message={
            "transactiontext":transactiontext,
            "status":"ok", 
            "code":200
            }
            message=json.dumps(message)
            return message, 200
            
          elif orderStatus =="Transaction Successful":
            transactiontext="Transaction Successful"
            message={
            "body":receiptdictionary,
            "transactiontext":transactiontext,
            "status":"ok", 
            "code":200
            }
            message=json.dumps(message)
            return message, 200

        else:
          return receiptdictionary

        message={"status":"ok", "code":200}
        message=json.dumps(message)
        return message, 200



	
      #  {
      #   "customer": {
      #     "name": "John Doe",
      #     "mobileNumber": "1234567889",
      #     "reference": "dssv6s6vs6v"
      #   },
      #   "transaction": {
      #     "date": "2017-08-31",
      #     "reference": "x22d5dq6",
      #     "paymentMode": "Cash",
      #     "amount": "1000.00",
      #     "till": "1",
      #     "billNumber": "5",
      #     "servedBy": "ABC",
      #     "additionalInfo": "Pay On Delivery"
      #   },
      #   "bank": {
      #     "reference": "6zc6wvsv1",
      #     "transactionType": "credit",
      #     "account": "123654789"
      #   }
      # }
