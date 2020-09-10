from db_creating.connection import cursor
from mysql.connector import ProgrammingError


try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS company_positions(
    id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))""")
except ProgrammingError:
    print('[X]! Error with table creating. Check settings')
