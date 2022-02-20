from flask import Flask, render_template, request
from werkzeug import secure_filename
import jyserver.Flask as jsf

app = Flask(__name__)

@jsf.use(app) 
class App:
    def __init__(self):
        self.salary = 0
        self.avgsalary = 0

@app.route('/uploader', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    