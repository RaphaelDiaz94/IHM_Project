
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import sqlite3
import os
import psycopg2
import boto3
from PIL import Image
import urllib



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():


    s3 = boto3.client('s3',
                    aws_access_key_id='AKIAVA5FQS276OPE5LYU',
                    aws_secret_access_key= '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',
                     )
    BUCKET_NAME='myphotobucketraph'

    #file_name = 'Users_raphaeldiaz_Desktop_test.png'

    theobjects = s3.list_objects_v2(Bucket=BUCKET_NAME)
    liste = []
    for object in theobjects['Contents']:
        liste.append(object['Key'])
        print (object['Key'])

    try :
    
        list_filename = []
        for i in range (len(liste)):

            filename = boto3.client('s3').generate_presigned_url(
                ClientMethod='get_object', 
                Params={'Bucket': BUCKET_NAME, 'Key': liste[i]},
                ExpiresIn=3600)
            
            list_filename.append(filename)

    except Exception as e:
        print(e)
        print('Error downloading image')


    #src=r'/Users/raphaeldiaz/Desktop/IHM_Projet/Users_raphaeldiaz_Desktop_test.png'
    #des=r'/Users/raphaeldiaz/Desktop/IHM_Projet/static/images/Users_raphaeldiaz_Desktop_test.png'
    #os.rename(src,des)

    nom_de_la_rue = 'Rue de la Paix'
    
    conn = psycopg2.connect("postgres://owshwcafnfsgsx:2b4cf5ade3fb7b2f25e3f1b66cd29d5a7e420fdd1d51b4c01df4b6086f1db630@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5arg29ce13853", sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM stats;")
    val = cur.fetchall()

    return render_template('index.html', val=val, cur=cur , list_filename=list_filename , nom_de_la_rue = nom_de_la_rue)


