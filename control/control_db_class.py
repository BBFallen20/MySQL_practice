from db_creating.connection import cursor, database


class Controller:
    def __init__(self):
        self.control = cursor
        self.database = database

    def new_user(self):
        user_name = input("[?] Enter user name:\n")
        user_surname = input("[?] Enter user surname:\n")
        user_patronymic = input("[?] Enter user patronymic:\n")
        user_date_of_birth = input("[?] Enter user date of birth:\n")
        user_address = input("[?] Enter user address:\n")
        user_salary = int(input("[?] Enter user salary:\n"))
        user_position = input("[?] Enter user position:\n")
        user_department = input("[?] Enter user department:\n")
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
        self.control.execute(sql, val)
        self.database.commit()
        return print('[OK] New user has been added.')

    def delete_user(self):
        user_name = input("[?] Enter username:\n")
        user_surname = input("[?] Enter surname:\n")
        user_address = input("[?] Enter address:\n")
        sql = 'DELETE FROM users WHERE name = "%s" AND  surname = "%s" AND adress = "%s"'
        val = (user_name, user_surname, user_address)
        self.control.execute(sql, val)
        self.database.commit()
        return print('[OK] User has been deleted.')

    def get_user(self):
        sql = "SHOW COLUMNS FROM users"
        self.control.execute(sql)
        columns = []
        count = 0
        for res in self.control.fetchall():
            columns.append(
                {
                    count: res[0]
                }
            )
            count += 1
        print("[!] Allowed columns:")
        for i in columns:
            print(i)
        search_column = int(input(f"[?] Enter column to search user: \n"))
        try:
            val = (input("Enter value:\n") if columns[search_column][search_column] != 'salary' else
                   int(input("Enter value:\n")), )
            sql = 'SELECT * FROM users WHERE {column_name} = "%s"'.format(
                column_name=columns[search_column][search_column]
            )
            self.control.execute(sql, val)
            answer = self.control.fetchall()
            if answer:
                for i in answer:
                    print(i)
            else:
                print("[X] No such user.")
            return print('[OK] Request successful.')
        except IndexError:
            return print('[X]! No such column.')


a = Controller()
a.get_user()
