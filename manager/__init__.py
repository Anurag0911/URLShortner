from flask import Flask, url_for, request, render_template, redirect
from .query import short_url, original_url
from urllib.parse import urlparse
from .shortner import base62, base10
from os import path

import sqlite3

DB_NAME = "database.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET_KEY'

    create_database(app)

    @app.route('/',methods=['GET','POST'])
    def index():
        if request.method=='GET':
            return render_template('main.html')

    @app.route('/get_short_url',methods=['POST'])
    def get_short_url():
        url = request.data.decode("UTF-8")
        
        url = url[1:len(url)-1]
        if not urlparse(url).scheme:
            url = "http://{}".format(url)
        req = short_url(url)
        
        short = base62(req,62)
        short = "http://127.0.0.1:5000/{}".format(short)
        return short

    @app.route('/<st_url>')
    def st_url(st_url):
        try:
            return redirect(original_url(base10(st_url,62)))
        except:
            return "invalid request"

    return app


def create_database(app):
    if not path.exists(DB_NAME):
        with sqlite3.connect('database.db') as conn:
            conn.execute("""CREATE TABLE URL (ID INTEGER PRIMARY KEY, URL TEXT NOT NULL)""")