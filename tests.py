import pytest
from app import app
import os
import psycopg2

def tests():
    i = 0
    j=0

    conn = psycopg2.connect("postgres://owshwcafnfsgsx:2b4cf5ade3fb7b2f25e3f1b66cd29d5a7e420fdd1d51b4c01df4b6086f1db630@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5arg29ce13853", sslmode='require')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS tests;")
    cur.execute("CREATE TABLE tests (id serial PRIMARY KEY,nom_element char(50), nb_element integer,precision char(50), nomrue char(50));")
    cur.execute("INSERT INTO tests (nom_element, nb_element, precision ,nomrue) VALUES (%s, %s ,%s ,%s)",("trotinette",3, "01-09-2022", "rue de la foi"))
    cur.execute("INSERT INTO tests (nom_element, nb_element, precision, nomrue) VALUES (%s, %s ,%s ,%s)",("avion",1, "01-09-2022", "rue de la foi"))

    conn.commit()
    cur.execute("SELECT * FROM tests;")
    val = cur.fetchall()
    assert type(val) == list
    assert len(val) != 0
    assert len(val[0])== 5
    assert len(val[1])== 5
    for i in range (len(val)):
        temp = val[i]
        print(temp)
        print(type(temp))
        for j in range (len(temp)):
            assert type(temp[j]) == str or type(temp[j]) == int
    




    cur.close()
    conn.close()
