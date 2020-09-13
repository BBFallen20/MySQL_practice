from db_creating.connection import cursor, database
from mysql.connector import Error
"""Class which contains 'company_positions' table configuration."""


class PositionController:
    """'company_positions' table controller"""
    def __init__(self):
        self.control = cursor
        self.database = database

    def new_position(self):
        """Adding position to table"""
        position_name = input("[?] Enter position name:\n")
        sql = 'INSERT INTO company_positions (name) VALUES ("%s")'
        val = (position_name, )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] Position creating failed. {Error}")
            return 0
        return print(f"[OK] New position {position_name} has been added successful.")

    def delete_position(self):
        """Delete position from table"""
        position_name = input("[?] Enter position name:\n")
        sql = 'DELETE FROM company_positions WHERE name = "%s"'
        val = (position_name, )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] Position deleting failed. {Error}")
            return 0
        return print(f"[OK] Position '{position_name}' has been deleted.")

    def get_all_positions(self):
        """Get all positions from table"""
        sql = 'SELECT name FROM company_positions'
        try:
            self.control.execute(sql)
        except Error:
            print(f"[X] Error while getting all positions. {Error}")
            return 0
        answer = {}
        count = 1
        for i in self.control.fetchall():
            answer.update(
                {
                 count: str(i[0]).replace("'", "")
                }
            )
            count += 1
        return answer

    def update_position(self):
        """Update table position"""
        sql = 'UPDATE company_positions SET name = "%s" WHERE name = "%s"'
        val = (
            input("[?] Enter replace position:\n"),
            input("[?] Enter search position:\n")
        )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] Error while updating {Error}")
            return 0
        return print(f"[OK] Position '{val[1]}' updated to '{val[0]}'")
