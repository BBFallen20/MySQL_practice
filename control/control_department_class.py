from db_creating.connection import cursor, database
from mysql.connector import Error


class DepartmentController:
    """Department table control class"""

    def __init__(self):
        self.control = cursor
        self.database = database

    def __str__(self):
        return f"{self.database}"

    def new_department(self):
        sql = 'INSERT INTO department (name) VALUES ("%s")'
        val = (input("[?] Enter department name:\n"), )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print(f"[OK] New department '{val[0]}' has been added.")

    def update_department(self):
        sql = 'UPDATE department SET name = "%s" WHERE name = "%s"'
        val = (
            input("[?] Enter replace data:\n"),
            input("[?] Enter search data:\n")
        )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 1
        return print(f"[OK] Department '{val[1]}' has been changed to '{val[0]}'.")

    def delete_department(self):
        sql = 'DELETE FROM department WHERE name = "%s"'
        val = (input("[?] Enter delete data:\n"))
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 1
        return print(f"[OK] Department '{val[0]}' has been deleted.")

    def get_all_departments(self):
        sql = 'SELECT * FROM department'
        try:
            self.control.execute(sql)
        except Error:
            print(f"[X] {Error}")
            return 1
        for i in self.control.fetchall():
            print(i)
        return print("[OK] Request successful.")


a = DepartmentController()
a.get_all_departments()
