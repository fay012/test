import mysql.connector
from  mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from common_func import *
from import_data import *
from tkinter.filedialog import *
import tkinter as tk

BOLD_FONT = ("Verdana bold", 12)
LARGE_FONT = ("Verdana", 12)
MID_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

class DataBase(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='appicon.ico')
        tk.Tk.wm_title(self, "Yoda C0 Database Tool - Innophase Inc")
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        frame = StartPage(self,container)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        frame = ImportData(self,container)
        self.frames[ImportData] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button0 = tk.Button(self, text="Import Data", command=lambda: controller.show_frame(ImportData))
        button0.pack(pady=5, padx=5)



class ImportData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="grey")
        label = tk.Label(self, text="Import Data", font=BOLD_FONT)
        label.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)
        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=1, sticky="nsew", pady=1, padx=1)

        button2 = tk.Button(self, text="Create A New Table And Import Data")
        button2.grid(row=1, column=1, sticky="nsew", pady=1, padx=1)

        button3 = tk.Button(self, text="Import Data To ")
        button3.grid(row=1, column=1, sticky="nsew", pady=1, padx=1)





app = DataBase()
app.mainloop()