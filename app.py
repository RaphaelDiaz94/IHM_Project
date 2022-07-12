from tkinter import Variable
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
Bootstrap4(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
