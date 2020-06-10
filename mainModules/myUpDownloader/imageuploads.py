# uploads and saves images
from werkzeug import secure_filename
from flask import request, redirect
import os

def image_uploader():

	def allowed_file(filename):
		return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGE_ALLOWED_EXTENSIONS

	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No file selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], filename))
		flash('File successfully uploaded')
		return redirect('/')
	else:
		flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
		return redirect(request.url)
	return redirect(request.url)


# user = Business.objects.filter(username=session.get('username')).first()
# if user:
#     form = RegisterForm(obj=user)
#     if form.validate_on_submit():
#         # check if image
#         image_ts=None
#         # basedir = os.path.abspath(os.path.dirname(__file__))
#         if form.image:
#             filename = secure_filename(form.image.data.filename)
#             file_path = os.path.join(UPLOAD_FOLDER, 'user', filename)
#             form.image.data.save(file_path)
#             image_ts = str(thumbnail_process(file_path, 'user', str(user.id)))
            
#         if not error:
#             form.populate_obj(user)
#             if image_ts:
#                 user.profile_image = image_ts
#                 user.save()
#             if not message:
#                 message = "Image Posted"