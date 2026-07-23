import mysql.connector

print("Connecting to MySQL...")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="MadhuranthiR@1326#",
    database="user",
    connection_timeout=5
)

print("Connected!")

cursor = connection.cursor(dictionary=True)