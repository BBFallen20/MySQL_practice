from db_creating.connection import cursor, database
from mysql.connector import Error


class PositionController:
    def __init__(self):
        self.control = cursor
        self.database = database

    def new_position(self):
        position_name = input("[?] Enter position name:\n")
        sql = 'INSERT INTO company_positions (name) VALUES ("%s")'
        val = (position_name, )
        try:
            self.control.execute(sql, val)
        except Error:
            return print(f"[X] Position creating failed. {Error}")
        return print(f"[OK] New position {position_name} has been added successful.")

    def delete_position(self):
        position_name = input("[?] Enter position name:\n")
        sql = 'DELETE FROM company_positions WHERE name = "%s"'
        val = (position_name, )
        try:
            self.control.execute(sql, val)
        except Error:
            return print(f"[X] Position deleting failed. {Error}")
        return print(f"[OK] Position '{position_name}' has been deleted.")

    def get_all_positions(self):
        sql = 'SELECT name FROM company_positions'
        try:
            self.control.execute(sql)
        except Error:
            return print(f"[X] Error while getting all positions. {Error}")
        answer = {}
        count = 1
        for i in self.control.fetchall():
            answer.update(
                {
                 count: str(i[0]).replace("'", "")
                }
            )
            count += 1
        print(answer)
        return answer


PositionController().delete_position()
