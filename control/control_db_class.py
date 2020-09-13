from db_creating.connection import cursor, database
from mysql.connector import Error
from control.control_department_class import DepartmentController
from control.control_position_class import PositionController
"""Class which contains 'users' table configuration."""


class Controller:
    """Users table control class"""
    def __init__(self):
        self.control = cursor
        self.database = database

    def __str__(self):
        return f"{self.database}"

    def new_user(self):
        """User add function"""
        user_name = input("[?] Enter user name:\n")
        user_surname = input("[?] Enter user surname:\n")
        user_patronymic = input("[?] Enter user patronymic:\n")
        user_date_of_birth = input("[?] Enter user date of birth:\n")
        user_address = input("[?] Enter user address:\n")
        user_salary = int(input("[?] Enter user salary:\n"))
        print("Positions:")
        if PositionController().get_all_positions():
            print(PositionController().get_all_positions())
        else:
            print("[X] Create at least one position.")
            return 0
        try:
            user_position_question = int(input("[?] Enter user position:\n"))
            user_position = PositionController().get_all_positions()[user_position_question]
        except IndexError:
            print("[X] No such position.")
            return 0
        except ValueError:
            print("[X] Answer must be an integer.")
            return 0
        print("Departments:")
        if DepartmentController().get_all_departments():
            print(DepartmentController().get_all_departments())
        else:
            print("[X] Create at least one department.")
            return 0
        try:
            question = int(input("[?] Enter user department:\n"))
            user_department = DepartmentController().get_all_departments()[question]
        except IndexError:
            print("[X] No such department.")
            return 0
        except ValueError:
            print("[X] Answer must be an integer.")
            return 0
        sql = 'INSERT INTO users(name, surname, patronymic, birth_date, adress, salary, position, department) VALUES ' \
              '("%s","%s","%s",STR_TO_DATE(REPLACE("%s", "\'", ""),"%Y-%m-%d"),"%s","%s","%s","%s")'
        val = (
                  user_name,
                  user_surname,
                  user_patronymic,
                  user_date_of_birth,
                  user_address,
                  user_salary,
                  user_position,
                  user_department
              )
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print('[OK] New user has been added.')

    def delete_user(self):
        """Delete user function"""
        user_name = input("[?] Enter username:\n")
        user_surname = input("[?] Enter surname:\n")
        user_address = input("[?] Enter address:\n")
        sql = 'DELETE FROM users WHERE name = "%s" AND  surname = "%s" AND adress = "%s"'
        val = (user_name, user_surname, user_address)
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print('[OK] User has been deleted.')

    def get_user(self):
        """Find users function"""
        get_data = self.get_table_data()
        search_column, columns = get_data[0], get_data[1]
        try:
            if columns[search_column] != 'salary' and columns[search_column] != 'id':
                val = (input("[?] Enter search data:\n"), )
                sql = 'SELECT * FROM users WHERE {column_name} = "%s"'.format(
                    column_name=columns[search_column]
                )
            else:
                val = (int(input("[?] Enter search data:\n")), )
                sql = 'SELECT * FROM users WHERE {column_name} = %s'.format(
                    column_name=columns[search_column]
                )
            try:
                self.control.execute(sql, val)
            except Error:
                print(f"[X] Error with table data parsing {Error}")
                return 0
            answer = self.control.fetchall()
            if answer:
                for i in answer:
                    print(i)
            else:
                print("[X] No such user.")
            print('[OK] Request successful.')
            return 0
        except IndexError:
            print('[X]! No such column.')
            return 0

    def get_table_data(self):
        """Get table columns function"""
        sql = "SHOW COLUMNS FROM users"
        try:
            self.control.execute(sql)
        except Error:
            print(f"[X] Error while parsing columns from table {Error}")
            return 0
        columns = {}
        count = 0
        for res in self.control.fetchall():
            columns.update(
                {
                    count: res[0]
                }
            )
            count += 1
        print("[!] Allowed columns:")
        print(columns)
        try:
            search_column = int(input(f"[?] Enter column to search user: \n"))
            answer = (search_column, columns)
        except ValueError:
            print("[X] Answer must be an integer.")
            return 0
        return answer

    def update_user(self):
        """Update user info function"""
        get_data = self.get_table_data()
        search_column, columns = get_data[0], get_data[1]
        try:
            replace_column = int(input("[?] Enter column to change:\n"))
        except ValueError:
            print("[X] Answer must be an integer.")
            return 0
        if columns[search_column] == 'id' or columns[search_column] == 'salary':
            where_data = int(input('[?] Enter search data:\n'))
        else:
            where_data = input('[?] Enter search data:\n')
        if columns[replace_column] == 'id' or columns[replace_column] == 'salary':
            new_data = int(input('[?] Enter replace data:\n'))
        else:
            new_data = input('[?] Enter replace data:\n')
        sql = 'UPDATE users SET {0} = "%s" WHERE {1} = "%s"'.format(
            columns[replace_column],
            columns[search_column]
        )
        val = (new_data, where_data)
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] {Error}")
            return 0
        return print("[OK] User has been updated.")

    def get_all_users(self):
        """Get all users info function"""
        sql = "SELECT * FROM users"
        try:
            self.control.execute(sql)
        except Error:
            print(f"[X] {Error}")
            return 0
        print("[OK] List of users:")
        for i in self.control.fetchall():
            print(i)
        return print("[OK] Request successful.")

    def change_user_date_of_birth(self):
        """User's birth date changing function"""
        sql = 'UPDATE users SET birth_date = STR_TO_DATE(REPLACE("%s", "\'", ""),"%Y-%m-%d") WHERE' \
              ' id = %s'
        val = (input("[?] Enter new user birth date:\n"), int(input("[?] Enter user id:\n")))
        try:
            self.control.execute(sql, val)
        except Error:
            print(f"[X] Error while updating {Error}")
            return 0
        return print("[OK] User's birth date updated.")



