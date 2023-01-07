from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import psycopg2
import boto3

#test
app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():

    s3 = boto3.client(
        "s3",
        aws_access_key_id="AKIAVA5FQS275KLPM7ND",
        aws_secret_access_key="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",
    )
    BUCKET_NAME = "myphotobucketraph"

    theobjects = s3.list_objects_v2(Bucket=BUCKET_NAME)
    liste = []
    if "Contents" in theobjects:
        for object in theobjects["Contents"]:
            liste.append(object["Key"])
            print(object["Key"])

    try:

        list_filename = []
        nom_rue = []
        for i in range(len(liste)):

            filename = boto3.client("s3").generate_presigned_url(
                ClientMethod="get_object",
                Params={"Bucket": BUCKET_NAME, "Key": liste[i]},
                ExpiresIn=3600,
            )

            list_filename.append(filename)
            x = liste[i].split("_", 3)
            x = x[3].split(".", 1)
            nom_rue.append(x[0])

    except Exception as e:
        print(e)
        print("Error downloading image")

    nom_de_la_rue = "Rue de la Paix"

    conn = psycopg2.connect(
        "postgres://uefiasinsfuytj:6b6db3640fd241f113d864cdee832f81f4eb6e2eb27e96dff12949f914b21c29@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/dfkvk50b8sbucb",
        sslmode="require",
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM stats;")
    val = cur.fetchall()

    nom_element = []
    nb_element = []
    precision = []
    for i in range(len(val)):
        t = val[i]
        nom_element.append(t[1])
        nb_element.append(t[2])
        precision.append(t[3])

    legend = "Nombre d element en fonction du type"
    labels = nom_element
    values = nb_element

    return render_template(
        "index.html",
        val=val,
        cur=cur,
        list_filename=list_filename,
        nom_de_la_rue=nom_de_la_rue,
        legend=legend,
        labels=labels,
        values=values,
        nom_rue=nom_rue,
    )


@app.route("/aide")
def aide():

    return render_template("aide.html")
