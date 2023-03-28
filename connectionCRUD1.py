import sqlite3
from sqlite3 import Error



class DataAccessObject():
    def __init__(self):
        #The first time the program is run, the database will be created.
        try:
            self.connection = sqlite3.connect('employees_management.db')
        
        except Error as ex:
            print('Error trying to connect: {0}'.format(ex))


    def createTable(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute('''
                CREATE TABLE employees(
	                id INTEGER AUTOINCREMENT PRIMARY KEY,
                    employee_name VARCHAR(100) NOT NULL,
                    employee_charge VARCHAR(100) NOT NULL,
                    employee_salary INTEGER NOT NULL
                    )
                ''')
            except Error as ex:
                if ex == sqlite3.OperationalError:
                    answer = ("La tabla articulos ya existe") 
                
                else: 
                    answer =('Error trying to connect: {0}' .format(ex))

        return answer
    
    #def dropDataBase(self):
