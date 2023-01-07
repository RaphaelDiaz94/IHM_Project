import os
import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect("postgres://uefiasinsfuytj:6b6db3640fd241f113d864cdee832f81f4eb6e2eb27e96dff12949f914b21c29@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/dfkvk50b8sbucb", sslmode='require')

print("connexion ok")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS stats;")
cur.execute("CREATE TABLE stats (id serial PRIMARY KEY,nom_element char(50), nb_element integer,precision char(50), nom_fichier char(50));")
print("table stats créée")


print("insertion ok")
conn.commit()
print("commit ok")

cur.execute("SELECT * FROM stats;")
val = cur.fetchall()

cur.close()
print("cursor close")
conn.close()
print("connexion close")


