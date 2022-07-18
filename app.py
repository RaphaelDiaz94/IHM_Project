
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

    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    print("connexion ok")

    cur = conn.cursor()

    try :
        cur.execute("CREATE TABLE image (id serial PRIMARY KEY, name varchar);")
        print("table image créée")

    except psycopg2.Error as e:

        print(e)

    conn.close()

    print("connexion close")

init_db()