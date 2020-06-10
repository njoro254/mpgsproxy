# uploads and saves documents
def kyc_uploader():
	
	def allowed_file(filename):
		return '.' in filename and filename.rsplit('.', 1)[1].lower() in KYC_ALLOWED_EXTENSIONS

	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No file selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['KYC_UPLOAD_FOLDER'], filename))
		flash('File successfully uploaded')
		return redirect('/')
	else:
		flash('Allowed file types are text and pdf')
		return redirect(request.url)
	return redirect(request.url)