
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import sqlite3
import os
import psycopg2

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

def init_db():

    conn = psycopg2.connect("postgres://owshwcafnfsgsx:2b4cf5ade3fb7b2f25e3f1b66cd29d5a7e420fdd1d51b4c01df4b6086f1db630@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5arg29ce13853", sslmode='require')
    print("connexion ok")
    cur = conn.cursor()
    print("cursor ok")
    cur.execute("SELECT * FROM stats;")
    val = cur.fetchone()
    print(val)
    print("type de val: ", type(val))
    return cur,val

