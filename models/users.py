# _*_ coding: utf-8 _*_
from database import DataBase, db

class Users:
    def __init__(self, users):
        self.__name = users.get('name', False)
        self.__password = users.get('password', False)

    @staticmethod
    def browse_user(id_user):
        browse_user_query="""select * from users where id_user ={id_user}""".format(id_user=id_user)
        db = DataBase()
        ps_connection = db.session()
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute(browse_user_query)
        user = ps_cursor.fetchone()
        ps_cursor.close()
        return user

    @property
    def name(self):
        return  self.__name

    @property
    def password(self):
        return self.__password

    @name.setter
    def name(self, name):
        self.__name = name

    @password.setter
    def password(self, password):
        self.__password = password

