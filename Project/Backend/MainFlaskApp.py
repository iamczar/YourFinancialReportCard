import os
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)

app.secret_key = "secret key"

#It will allow below 16MB contents only, you can change it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path_to_bankstatement = "../BankStatements"
UPLOAD_FOLDER = os.path.join(path_to_bankstatement,'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/hello')
# def hello_world():
#     result = str(''.join(str(e) for e in HandleBankStatement.handle_bankstatement()))

#     return str("<html><head></head><body>"+result+"</body></html>")

@app.route('/upload-bankstatements.html')
def upload_form():
    return render_template('upload_bankstatements.html')

@app.route('/')
def index():
    return render_template('summary.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/upload-bankstatements',methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files)
        if 'files[]' not in request.files:
            return 'No file part'
            #return flash('No file part')
            #return redirect('/data?upload=true')

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return 'File(s) successfully uploaded'
        #return redirect('/data?upload=true')


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)
