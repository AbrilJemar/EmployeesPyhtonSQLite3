from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from connectionCRUD1 import DataAccessObject



root=Tk()
root.title('CRUD APLICATION')
root.geometry('600X350')

Id = StringVar()
Name = StringVar()
Charge = StringVar()
Salary = StringVar()

DAO = DataAccessObject()
aswer = DAO.createTable()

messagebox.showinfo(aswer)


