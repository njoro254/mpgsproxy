# from flask import Flask
# from flask_mail import Mail, Message
# import os

# app = Flask(__name__)
# mail = Mail(app)

# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 587,
#     "MAIL_USE_TLS": True,
#     "MAIL_USE_SSL": False,
#     "MAIL_USERNAME": "EMAIL_USER",
#     "MAIL_PASSWORD": "EMAIL_PASSWORD"
# }

# app.config.update(mail_settings)

# if __name__ == '__main__':
#     with app.app_context():
#         msg = Message(subject="Hello",
#                       sender=app.config.get("MAIL_USERNAME"),
#                       recipients=["<marknjoroge.m@gmail.com>"], # replace with your email for testing
#                       body="This is a test email I sent with Gmail and Python!")
#         mail.send(msg)






# mailer method to be sent to mailgun php client for email verification, two factor authentication and notification services
def myMailer(recipientslist, subject, body):

  emailData={
  "recipients":recipientslist,
  "subject":subject,
  "body":body
  }

  resp = requests.post(
    url=url, 
    headers=headers, 
    data=emailData
    )

  emailApiResponseData = resp.content
  return emailApiResponseData

  