import os

SECRET_KEY = 'this-is-the-jenga-proxy-by-chef-njoro'
DEBUG=True

MONGODB_SETTINGS = {
	'DB' : 'jengaDatabase1',
	'HOST' : '127.0.0.1',
	'PORT' : 27017
	}
	
MONGODB_SETTINGS = {
	'DB' : 'separateJengaDatabaseForAudit',
	'HOST' : '127.0.0.1',
	'PORT' : 27017
	}

IMAGE_UPLOAD_FOLDER = './docs/uploads/pictures'
KYC_UPLOAD_FOLDER = './docs/uploads/kyc'
PDF_DOWNLOAD_FOLDER = './docs/downloads/pdfs'
EXCEL_DOWNLOAD_FOLDER = './docs/downloads/excel'


STATIC_IMAGE_URL = 'images'
STATIC_KYC_URL = 'kyc'
STATIC_PDFS_URL = 'pdfs'
STATIC_EXCEL_URL = 'excel'

IMAGE_ALLOWED_EXTENSIONS = set(['bmp', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'svgj'])
KYC_ALLOWED_EXTENSIONS = set(['txt', 'pdf'])
