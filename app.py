
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import sqlite3
import os
import psycopg2
import boto3
from PIL import Image



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():


    s3 = boto3.client('s3',
                    aws_access_key_id='AKIAVA5FQS27ZQZRC4ER',
                    aws_secret_access_key= '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',
                     )
    BUCKET_NAME='myphotobucketraph'

    file_name = 'Users_raphaeldiaz_Desktop_test.png'
    print("test")

    try :
        img = s3.download_file(
            Bucket = BUCKET_NAME,
            Filename=file_name,  
            Key = file_name,  
            )
    
    except Exception as e:
        print(e)
        print('Error downloading image')


    #src=r'/Users/raphaeldiaz/Desktop/IHM_Projet/Users_raphaeldiaz_Desktop_test.png'
    #des=r'/Users/raphaeldiaz/Desktop/IHM_Projet/static/images/Users_raphaeldiaz_Desktop_test.png'
    #os.rename(src,des)

    print(e)
    print("OK")

    
    conn = psycopg2.connect("postgres://owshwcafnfsgsx:2b4cf5ade3fb7b2f25e3f1b66cd29d5a7e420fdd1d51b4c01df4b6086f1db630@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5arg29ce13853", sslmode='require')
    print("connexion ok")
    cur = conn.cursor()
    print("cursor ok")
    cur.execute("SELECT * FROM stats;")
    val = cur.fetchall()
    print(val)
    print("type de val: ", type(val))

    return render_template('index.html', val=val, cur=cur , img=img)


