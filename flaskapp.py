import json
import requests
from bs4 import BeautifulSoup
import datetime
from flask import Flask, render_template, request
flaskapp = Flask(__name__)

@flaskapp.route('/')
def welcome():
    greet_message = "Hello World"
    return greet_message

@flaskapp.route('/form')
def form():
    return render_template('form.html')

@flaskapp.route('/decided', methods = ['POST', 'GET'])
def decided():
   if request.method == 'POST':
        dates = request.form['h']
        data = datetime.datetime(dates)

        homeUrl = '/form'
        return render_template("decided.html", data=data, homeUrl=homeUrl)

if __name__ == "__main__":
    flaskapp.run(port=8000, debug=True)
