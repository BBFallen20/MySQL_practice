from db_creating.connection import cursor, database
from mysql.connector import Error
"""Class which contains 'department' table configurations."""


class DepartmentController:
    """Department table control class"""
    def __init__(self):
        self.control = cursor
        self.database = database

    def __str__(self):
        return f"{self.database}"

    def new_department(self):
        """Create new department"""
        sql = 'INSERT INTO department (name) VALUES ("%s")'
        val = (input("[?] Enter department name:\n"), )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print(f"[OK] New department '{val[0]}' has been added.")

    def update_department(self):
        """Update existing department"""
        sql = 'UPDATE department SET name = "%s" WHERE name = "%s"'
        val = (
            input("[?] Enter replace data:\n"),
            input("[?] Enter search data:\n")
        )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print(f"[OK] Department '{val[1]}' has been changed to '{val[0]}'.")

    def delete_department(self):
        """Delete department"""
        sql = 'DELETE FROM department WHERE name = "%s"'
        val = (input("[?] Enter delete data:\n"))
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print(f"[OK] Department '{val[0]}' has been deleted.")

    def get_all_departments(self):
        """Get list of all existing departments"""
        sql = 'SELECT name FROM department'
        try:
            self.control.execute(sql)
        except Error:
            print(f"[X] {Error}")
            return 1
        answer = {}
        counter = 1
        for i in self.control.fetchall():
            answer.update(
                {
                    counter: str(i[0]).replace("'", "")
                }
            )
            counter += 1
        return answer
