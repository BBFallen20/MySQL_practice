import mysql.connector
from mysql.connector import ProgrammingError
from settings import db_name, password, user, host

try:
    database = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print("[OK] Connection successfully.")
except ProgrammingError:
    print("[X]! Connection to database failed. Check username, password or database name.")

cursor = database.cursor()



