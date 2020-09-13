import mysql.connector
from mysql.connector import Error
from settings import db_name, password, user, host, auto_commit
"""Database connection file, check settings.py"""


try:
    database = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        autocommit=auto_commit
    )
    print("[OK] Connection successfully.")
except Error:
    print("[X]! Connection to database failed. Check username, password or database name.")

cursor = database.cursor()



