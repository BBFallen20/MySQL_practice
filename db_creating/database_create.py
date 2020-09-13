import mysql.connector
from mysql.connector import Error
"""Database creation file."""


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='756756'
)

cursor = connection.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS company")
except Error:
    print("[X]! Database with this name already exists. Try another name.")
