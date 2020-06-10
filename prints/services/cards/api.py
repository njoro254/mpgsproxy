# jenga payment gateway - the module receives payments from both the client server and individual consumer, saves data and services Jenga

from flask.views import MethodView
from flask import jsonify,request,abort,session
from datetime import date
from prints.services.cards.models import invoice, cardPay
from prints.services.cards.functionExtra import get_token
import requests, json
from prints.auth.decorators import auth_required
# from mainModules.disasterPrevention.mylogger import applogger


class InvoiceAPI(MethodView):

    # def __init__(self):
    #     if (request.method != 'GET') and not request.json:
    #         abort(400)
        # if session['logged_in'] is True:
        #     pass
        # else:
        #     abort(400)

    # def get(self):
    #   pass

    decorators = [auth_required]

    def get(self):
      pass



      # load proceed payment form in page with details from vendor
      # receive get request from server with relevant details
      # display webpage using details containing submit button


       # name=request.json['customer']['name']
       # reference=request.json['order']['reference']
       # amount=request.json['order']['amount']
       # currency=request.json['order']['currency']
       # channel=request.json['order']['channel']
       # description=request.json['order']['description']
       # outlet=request.json['order']['outlet']
       # billerCode=request.json['order']['billerCode']

       # message="Hello, <name> welcome to site. kindly confirm the payment of "
       # "<currency> <amount> to <outlet> for the product <description>"

       # return render_template("invoiceConfirmer.html", formMessage=message, form=proceedPaymentForm)



    def post(self):
      # receive details direct from vendor and proceed to create invoice 
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')
      
       name=request.json['customer']['name']
       reference=request.json['order']['reference']
       amount=request.json['order']['amount']
       currency=request.json['order']['currency']
       channel=request.json['order']['channel']
       description=request.json['order']['description']
       outlet=request.json['order']['outlet']
       billerCode=request.json['order']['billerCode']

       # applogger("card invoice creation request")
     
       newinvoice=invoice(
        customerName=name, 
        reference=reference, 
        amount=amount, 
        currency=currency, 
        channel=channel, 
        description=description, 
        outlet=outlet, 
        billerCode=billerCode
        )
       newinvoice.save()

       authorization=get_token()[0]

#       authorization=bearer_token

       # adding source details to invoice table

       invoicetext= {
       "customer":{"name":name
       }, 
       "transaction":
       {
       "reference":reference, 
       "amount":amount, 
       "currency":currency, 
       "channel":channel, 
       "description":description, 
       "outlet":outlet, 
       "billerCode":billerCode
       }
       }

       invoicetext=json.dumps(invoicetext)
       # return invoicetext

       url='https://api.jengahq.io/payment/v2/bills '


       invoiceheaders={
       "Authorization":authorization,
       "Content-Type":"application/json"
       }

       headers= dict(invoiceheaders)

       resp = requests.post(
        url=url, 
        headers=headers, 
        data=invoicetext
        )

       data = resp.json()
       data=json.dumps(data)
       print (data)
       return data

        # billReference=request.json['reference']
        # billamount=request.json['amount']
        # serviceId=request.json['serviceId']
        # status=request.json['status']
        # orderReference=request.json['orderRef']
        # channel=request.json['channel']
        # remarks=request.json['remarks']
        # systemCode=request.json['systemCode']

        # if status==0:
        #   return "transaction failed"

        # elif status==1:
        #   saveInvoiceResponse=InvoiceResponse(
        #     billReference=billReference,
        #     billamount=billamount,
        #     serviceId=serviceId,
        #     status=status,
        #     orderReference=orderReference,
        #     channel=channel,
        #     remarks=remarks,
        #     systemCode=systemCode)
        #   saveInvoiceResponse.save()

        #   return redirect("billCheckOut.html", billamount=billamount, billReference=billReference)


       

class BillCheckOutAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET') and not request.json:
            abort(400)
        

    def get(self):
      pass
      # on submit fetch details regarding payer and proceed to checkout


      # message="Hello, <name> welcome to site. kindly confirm the payment of "
      #  "<currency> <billamount> to <outlet> for the product <productType>:<description>"
      #  "kindly enter your payment details to complete the payment"
      # cardPaymentForm= "serviceDate, customerFirstName, customerLastName, cardNumber, country, mobileNumber, emailAddress, postalcodeZip, address, city"
      # return render_template("cardPayer.html", formMessage=message, form=cardPaymentForm)
      

    
    def post(self):
#       authorization=request.headers.get('Authorization')
       signature=request.headers.get('signature')

       token=request.json['token']
       outletCode=request.json['outletCode']
       merchantCode=request.json['merchantCode']
       billamount=request.json['billamount']
       orderReference=request.json['orderReference']
       billReference=request.json['billReference']
       productType=request.json['productType']
       productDescription=request.json['productDescription']
       serviceDate=request.json['serviceDate']
       customerFirstName=request.json['customerFirstName']
       customerLastName=request.json['customerLastName']
       cardNumber=request.json['cardNumber']
       cardSecurity=request.json['cardSecurity']
       cardExpiryYear=request.json['cardExpiryYear']
       cardExpiryMonth=request.json['cardExpiryMonth']
       country=request.json['country']
       mobileNumber=request.json['mobileNumber']
       emailAddress=request.json['emailAddress']
       postalcodeZip=request.json['postalcodeZip']
       address=request.json['address']
       city=request.json['city']
       callbackUrl=request.json['callbackUrl']

       # applogger("card bill creation request")

       # adding source details to cardPaytable
       newCardPay=cardPay(
        token = token,
        outletCode = outletCode,
        merchantCode = merchantCode,
        billamount = billamount,
        orderReference = orderReference,
        billReference = billamount,
        productType = productType,
        productDescription = productDescription, 
        serviceDate = serviceDate,
        customerFirstName = customerFirstName,
        customerLastName = customerLastName,
        cardNumber = cardNumber[-4:],
        country =country,
        mobileNumber = mobileNumber,
        emailAddress = emailAddress,
        postalcodeZip = postalcodeZip,
        address = address,
        city = city,
        callbackUrl = callbackUrl
        )
       newCardPay.save()

       authorization=get_token()[0]


       # authorization=bearer_token

     

       cardPaytext= {
        "token" : token,
        "outletCode" : outletCode,
        "merchantCode" : merchantCode,
        "billamount" : billamount,
        "orderReference" : orderReference,
        "billReference" : billamount,
        "productType" : productType,
        "productDescription" : productDescription, 
        "serviceDate" : serviceDate,
        "customerFirstName" : customerFirstName,
        "customerLastName" : customerLastName,
        "cardNumber" : cardNumber,
        "cardSecurity" : cardSecurity,
        "cardExpiryYear" :cardExpiryYear,
        "cardExpiryMonth" :cardExpiryMonth,
        "country" :country,
        "mobileNumber" : mobileNumber,
        "emailAddress" : emailAddress,
        "postalcodeZip" : postalcodeZip,
        "address" : address,
        "city" : city,
        "callbackUrl" : callbackUrl       
       }

       cardPaytext=json.dumps(cardPaytext)

#       return cardPaytext

       url='https://test-pay.jengahq.io/cardPay'


       cardPayheaders={
       "Authorization":authorization,
       "Content-Type":"application/json"
       }

       headers= dict(cardPayheaders)

       resp = requests.post(
        url=url, 
        headers=headers, 
        data=cardPaytext
        )
       data = resp.json()
       data=json.dumps(data)
       print (data)
       return data

