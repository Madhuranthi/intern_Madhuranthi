import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sujitha37",
        database="user"
    )

    print("Database Connected Successfully!")

except Exception as e:
    print(e)