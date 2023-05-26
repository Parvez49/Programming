import django

import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password789'
)

cursorObject=database.cursor()
cursorObject.execute("CREATE DATABASE db")

print("All done")