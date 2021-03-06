import os, glob
import json
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import pprint

UPLOAD_FOLDER = r'C:\Users\mkeo2\Desktop\MapClient\wrcs'
ALLOWED_EXTENSIONS = {'trc'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))


@app.route('/get', methods=['GET'])
def returnMarkerSet():
    path = os.getcwd()
    path = path + "\\"
    trcFiles = []
    for file in glob.glob("*.trc"):
        trcFiles.append(file)
    for trc in trcFiles:
        with open(trc) as f:
            lis = [line.split() for line in f]        # create a list of lists
    metaData = lis[3]
    metaData = metaData[2:]
    dicts = {}
    i = 1
    for meta in metaData:
        dicts[str(i)] = meta
        i+=1
    return ulify(metaData)


def ulify(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return string


