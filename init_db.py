import os
import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect("postgres://owshwcafnfsgsx:2b4cf5ade3fb7b2f25e3f1b66cd29d5a7e420fdd1d51b4c01df4b6086f1db630@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5arg29ce13853", sslmode='require')

print("connexion ok")

cur = conn.cursor()
cur.execute("CREATE TABLE stats (id serial PRIMARY KEY,nom_element varchar, nb_element integer,precision integer);")
print("table stats créée")
conn.commit()
print("commit ok")
cur.close()
print("cursor close")
conn.close()
print("connexion close")


