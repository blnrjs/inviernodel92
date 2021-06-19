# -*- coding: utf-8 -*-
from data_base import DataBase

class Users:
    def __init__(self, users):

        self._id_user = users.get('id_user', False)
        self._name = users.get('name', False)
        self._password = users.get('password', False)
    
    @staticmethod
    def browse_user(id_user):
        browse_user_query= """ select * from users where id_user= 
        {id_user}""".format(id_user=id_user)
        db = DataBase()
        ps_connection = db.session()
        ps_cursor = ps_connection.cursor() 
        ps_cursor.execute(browse_user_query)
        user = ps_cursor.fetchone()
        ps_cursor.close()
        return user

    @property
    def id_user(self):
        return self._id_user

    @property
    def name(self):
        return self._name
    
    @property
    def password(self):
        return self._password

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @name.setter
    def name(self, name):
        self._name = name
    
    @password.setter
    def password(self, password):
        self._password = password

    

        