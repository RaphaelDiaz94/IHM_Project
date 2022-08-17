import os
import psycopg2


conn = psycopg2.connect("postgres://owshwcafnfsgsx:2b4cf5ade3fb7b2f25e3f1b66cd29d5a7e420fdd1d51b4c01df4b6086f1db630@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5arg29ce13853", sslmode='require')
cur = conn.cursor()
cur.execute("SELECT * FROM stats;")
val = cur.fetchall()
nom_element = []
nb_element = []
precision = []
for i in range(len(val)):
    print(val[i])
    print(type(val[i]))
    t = val[i]
    nom_element.append(t[1])
    nb_element.append(t[2])
    precision.append(t[3])

print(nom_element)
print(nb_element)
print(precision)

