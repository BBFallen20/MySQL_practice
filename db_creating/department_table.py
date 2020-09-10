from mysql.connector import ProgrammingError
from db_creating.connection import cursor


try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS department(
    id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255))""")
except ProgrammingError:
    print('[X]! Error with table creating. Check settings')
