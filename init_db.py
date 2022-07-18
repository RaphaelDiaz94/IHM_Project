import os
import psycopg2

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

