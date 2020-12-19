import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='./html')
app.config['UPLOAD_FOLDER'] = './upload'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('data.html', data="data send here")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/post', methods=['POST'])
def post():
    text = request.form['text']
    file = request.files['file']
    print(text)
    print(file)
    # print(file.read())
    if file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('result.html')

if __name__ == "__main__":
    app.run()
