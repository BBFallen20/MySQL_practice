from mysql.connector import Error
from db_creating.connection import cursor
"""Database 'department' table creation"""


try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS department(
    id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255))""")
except Error:
    print('[X]! Error with table creating. Check settings')
