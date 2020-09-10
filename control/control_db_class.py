from db_creating.connection import cursor, database


class Controller:
    def __init__(self):
        self.control = cursor
        self.database = database

    def new_user(self):
        user_name = 'Anton'
        user_surname = 'Pavlov'
        user_patronymic = 'Yurievich'
        user_date_of_birth = '1998-10-20'
        user_adress = 'Soborniy, 4'
        user_salary = 12000
        user_position = 'Manager'
        user_department = "Marketing"
        sql = 'INSERT INTO users(name, surname, patronymic, birth_date, adress, salary, position, department) VALUES ' \
              '("%s","%s","%s",STR_TO_DATE(REPLACE("%s", "\'", ""),"%Y-%m-%d"),"%s","%s","%s","%s")'
        val = (
                  user_name,
                  user_surname,
                  user_patronymic,
                  user_date_of_birth,
                  user_adress,
                  user_salary,
                  user_position,
                  user_department
              )
        self.control.execute(sql, val)
        self.database.commit()
        return print('[OK] New user has been added.')

    def delete_user(self):
        user_name = 'Anton'
        user_surname = 'Pavlov'
        user_adress = 'Soborniy, 4'
        sql = 'DELETE FROM users WHERE name = "%s" AND  surname = "%s" AND adress = "%s"'
        val = (user_name, user_surname, user_adress)
        self.control.execute(sql, val)
        self.database.commit()
        return print('[OK] User has been deleted.')


a = Controller()
a.delete_user()
