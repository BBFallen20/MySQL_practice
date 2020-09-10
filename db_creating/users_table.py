from db_creating.connection import cursor
from mysql.connector import ProgrammingError
try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
        (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL ,
        name VARCHAR(255) NOT NULL ,
        surname VARCHAR(255) NOT NULL , 
        patronymic VARCHAR(255) NOT NULL ,
        position VARCHAR(255) NOT NULL ,
        birth_date DATE,
        adress VARCHAR(255) NOT NULL ,
        salary INT NOT NULL ,
        department VARCHAR(255) NOT NULL 
        )""")
except ProgrammingError:
    print('[X]! Error with table creating. Check settings')

