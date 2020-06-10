from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed
import re


class BusinessRegisterForm(Form):
	first_name = StringField('Administrator First Name', [
		validators.DataRequired()])

	last_name = StringField('Administrator Last Name', [
		validators.DataRequired()])

	email = EmailField('Email address', [
		validators.DataRequired(), 
		validators.Email()])

	company_name=StringField('Company Name', [
		validators.DataRequired()])

	company_position=StringField('Position at Company', [
		validators.DataRequired()])

	username = StringField('Username', [
		validators.DataRequired(), 
		validators.Length(min=4, max=25)])

	location = StringField('location', [
		validators.DataRequired(), 
		validators.Length(min=4, max=25)])

	website = StringField('Website', [
		validators.DataRequired(), 
		validators.Length(min=4, max=25)])

	password = PasswordField('Password', [
		validators.Required(), 
		validators.EqualTo('confirm', message='Passwords must match'), 
		validators.length(min=4, max=80)])

	confirm = PasswordField('Repeat Password')

	image = FileField('Profile Image', 
		validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'],
			'Only JPEG, PNG and GIFs allowed')])
	
	
	
	def validate_username(form, field):
		if Member.objects.filter(username=field.data).first(): #check if username exists
			raise ValidationError("Username already exists")

		#if not re.match("^[a-zA-Z0-9_-]$"):
			#raise validationError("Invalid username")
	def validate_email(form, field):
		if Member.objects.filter(email=field.data).first(): #check if email exists
			raise ValidationError("Email is already in use")
	



class LoginForm(Form):
	username = StringField('Username', [
			validators.DataRequired(),
			validators.Length(min=4, max=25)
		])

	password = PasswordField('Password', [
			validators.DataRequired(),
			validators.Length(min=4, max=80)
		])



class ForgotPasswordForm(Form):
	username = StringField('Username', [
			validators.DataRequired(),
			validators.Length(min=4, max=25)
		])

	password = PasswordField('Password', [
			validators.DataRequired(),
			validators.Length(min=4, max=80)
		])


class ConfirmEmailForm(Form):
	email = StringField('email', [
			validators.DataRequired(),
			validators.Length(min=4, max=25)
		])

	
class EditProfileForm(Form):
	name = StringField('Administrator Name', [
		validators.DataRequired()])

	email = EmailField('Email address', [
		validators.DataRequired(), 
		validators.Email()])

	company_name=StringField('Company Name', [
		validators.DataRequired()])

	company_position=StringField('Position at Company', [
		validators.DataRequired()])

	username = StringField('Username', [
		validators.DataRequired(), 
		validators.Length(min=4, max=25)])

	password = PasswordField('Password', [
		validators.Required(), 
		validators.EqualTo('confirm', message='Passwords must match'), 
		validators.length(min=4, max=80)])

	confirm = PasswordField('Repeat Password')
		

class ContactUsForm(Form):
	name = StringField('Administrator Name', [
		validators.DataRequired()])

	email = EmailField('Email address', [
		validators.DataRequired(), 
		validators.Email()])

	message = StringField('Message', [
		validators.DataRequired(), 
		validators.Length(min=4, max=1000)])
