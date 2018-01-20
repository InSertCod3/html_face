import os
import errno
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from core import utils

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = utils.make_not_exist(os.path.join(CURRENT_PATH, 'uploads'))
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

class IMG_MA(object):
    class __init__(self):
        pass

    def based_face(self, img_pf):
        pass


def allowed_file(filename):
    al_ext = True if os.path.splitext(filename)[1].replace(".", "") in ALLOWED_EXTENSIONS else False
    return '.' in filename and al_ext


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file_in = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file_in.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_in and allowed_file(file_in.filename):
            filename = secure_filename(file_in.filename)
            file_in.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('uploads/{0}'.format(filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
