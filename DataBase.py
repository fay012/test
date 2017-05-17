#http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
import mysql.connector
from  mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from common_func import *
from import_data import *
from tkinter.filedialog import *
from tkinter import messagebox
from fetch_data import *
import tkinter as tk
BOLD_FONT = ("Verdana bold", 12)
LARGE_FONT = ("Verdana", 12)
MID_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

class DataBase(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='appicon.ico')
        tk.Tk.wm_title(self, "Yoda C0 Database Tool - Innophase Inc")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Page in (StartPage, ImportData, CreateTable, AppendData, Query, QueryAll, QueryCon, DB_Settings):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        #print (self.frames)

        self.show_frame('StartPage')

    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome To Use Data Base!", font=MID_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Import Data",font = MID_FONT, command=lambda: controller.show_frame('ImportData'))
        button1.pack(pady=5, padx=5)

        button2 = tk.Button(self, text="Query",font = MID_FONT, command=lambda: controller.show_frame('Query'))
        button2.pack(pady=5, padx=5)

        button3 = tk.Button(self, text="Change DataBase Settings", font=MID_FONT, command=lambda: controller.show_frame('DB_Settings'))
        button3.pack(pady=5, padx=5)


class ImportData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Import Data", font=MID_FONT)
        label.grid(row=2, column=0, sticky="nsew", pady=1, padx=1)
        button1 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame('StartPage'))
        button1.grid(row=4, column=2, sticky="nsew", pady=30, padx=30)

        button2 = tk.Button(self, text="Create A New Table And Import Data", command=lambda:controller.show_frame('CreateTable'))
        button2.grid(row=1, column=1, sticky="nsew", pady=15, padx=1)

        button3 = tk.Button(self, text="Import Data To An Existing Table",command=lambda:controller.show_frame('AppendData'))
        button3.grid(row=3, column=1, sticky="nsew", pady=15, padx=1)

class CreateTable(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        '''Create New Table For A Certain Test Type'''
        label0 = tk.Label(self, text='New Table Name (Test Type)', font=SMALL_FONT)
        label0.grid(row=0, column=1, columnspan=2,  pady=1, padx=1)
        self.entry0_var = StringVar()
        self.entry0_var.set('')
        self.entry0 = tk.Entry(self, textvariable=self.entry0_var, borderwidth=5, width=25)
        self.entry0.grid(row=1, column=1, columnspan=2, pady=1, padx=1)
        button1 = tk.Button(self, text='Next',command=self.ImportFirst)
        button1.grid(row=1, column=4, pady=1, padx=5)
        button2 = tk.Button(self, text='Back',command=lambda:controller.show_frame('ImportData'))
        button2.grid(row=1, column=6, pady=1, padx=5)

    def set_TestType(self):
        self.TestType = self.entry0.get()
        self.entry0.delete(0,END)
        self.entry0.insert(0,self.TestType)
        #String = 'Create A New Table For Test '+ self.TestType
        #messagebox.askquestion('Message', String)
        #print(self.TestType)
        return self.TestType

    def get_TestType(self):
        return self.TestType

    def ImportFirst(self):
        TestType = self.set_TestType()
        self.csv_path = StringVar()
        self.top = Toplevel(self)
        String = 'Table ' + TestType
        label0 = tk.Label(self.top, text=String, font=SMALL_FONT)
        label0.grid(row=0, column=0, pady=1, padx=1)
        '''Choose A .CSV File And Import To The New Table'''
        label1 = tk.Label(self.top, text='File Path', font=SMALL_FONT)
        label1.grid(row=1, column=0, pady=10, padx=10)
        self.entry1 = Entry(self.top,borderwidth=5, width=30)
        self.entry1.grid(row=1, column=1,columnspan=6, padx=1, pady=1)
        button0 = tk.Button(self.top, text='Browse', font=SMALL_FONT,command=self.load_file)
        button0.grid(row=1, column=7,padx=1, pady=1)
        button1 = tk.Button(self.top, text='Import Data', font=SMALL_FONT,command=lambda:self.Import_to_new(self.TestType,self.csv_name))
        button1.grid(row=2, column=3, padx=1, pady=2)


    def load_file(self):
        self.csv_name = askopenfilename(filetypes=(("csv files", "*.csv"), ("All files", "*.*")))
        #print(self.csv_name)
        self.entry1.delete(0, END)
        self.entry1.insert(0, self.csv_name)
        return self.csv_name

    def Import_to_new(self,TestType,csv_name):
        Import_first(TestType,csv_name)
        self.top.withdraw()

class AppendData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label0 = tk.Label(self, text='TestType')
        label0.grid(row=1,column=0, pady=1, padx=1)
        label1 = tk.Label(self, text='File Path', font=SMALL_FONT)
        label1.grid(row=0, column=0, pady=1, padx=1)

        self.entry0 = Entry(self, borderwidth=5, width=30)
        self.entry0.grid(row=1, column=1, columnspan=6, padx=1, pady=1)
        self.entry1 = Entry(self,borderwidth=5, width=30)
        self.entry1.grid(row=0, column=1,columnspan=6, padx=1, pady=1)

        button0 = tk.Button(self, text='Browse', font=SMALL_FONT,command=self.load_file)
        button0.grid(row=0, column=7,padx=1, pady=1)
        button1 = tk.Button(self, text='Import Data', font=SMALL_FONT, command=lambda:self.Import_data(self.csv_name))
        button1.grid(row=1, column=7, padx=1, pady=2)
        button3 = tk.Button(self, text='Back', font=SMALL_FONT, command=lambda:controller.show_frame('ImportData'))
        button3.grid(row=3, column=7, padx=1, pady=8)
        button4 = tk.Button(self, text='Append', font=SMALL_FONT,command=lambda: Merge_Data(self.TestType))
        button4.grid(row=3, column=3, padx=1, pady=2)

    def load_file(self):
        self.csv_name = askopenfilename(filetypes=(("csv files", "*.csv"), ("All files", "*.*")))
        #print(self.csv_name)
        self.entry1.delete(0, END)
        self.entry1.insert(0, self.csv_name)
        return self.csv_name

    def set_TestType(self):
        self.TestType = self.entry0.get()
        self.entry0.delete(0,END)
        self.entry0.insert(0,self.TestType)
        String = 'You Have Choose Table '+ self.TestType +", Press 'Append' to append"
        messagebox.askquestion('Message', String)
        #print(self.TestType)
        return self.TestType

    def Import_data(self,csv_name):
        TestType = self.set_TestType()
        Import(csv_name, TestType)

class Query(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label0 = tk.Label(self,text='Query Data',font=MID_FONT)
        label0.grid(row=1, column=0, padx=20, pady=1)
        button0 = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame('StartPage'))
        button0.grid(row=5, column=2, sticky="nsew", pady=40, padx=40)

        label1 = tk.Label(self,text='Choose Query Type',font=SMALL_FONT)
        label1.grid(row=0, column=1, sticky="nsew", pady=1, padx=1)

        button1 = tk.Button(self, text="Query Whole Table",command=lambda:controller.show_frame('QueryAll'))
        button1.grid(row=1, column=1, sticky="nsew", pady=1, padx=1)

        button1 = tk.Button(self, text="Condition Query",command=lambda:controller.show_frame('QueryCon'))
        button1.grid(row=2, column=1, sticky="nsew", pady=1, padx=1)

        #label1 = tk.Label(self, text='Enter Test Type (Table Name)', font=SMALL_FONT)
        #label1.grid(row=0, column=1, sticky="nsew", pady=1, padx=1)
        #entry1 = tk.Entry(self, borderwidth=5, width=30)
        #entry1.grid(row=0, column=2, padx=1, pady=1)
        #button1 = tk.Button(self, text="Next")
        #button1.grid(row=0, column=3, sticky="nsew", pady=1, padx=1)
class QueryAll(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label0 = tk.Label(self, text='Query All Table', font=SMALL_FONT)
        label0.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)
        label1 = tk.Label(self, text='Enter Test Type (Table Name)', font=SMALL_FONT)
        label1.grid(row=1, column=0, sticky="nsew", pady=1, padx=1)
        self.entry1 = tk.Entry(self, borderwidth=5, width=30)
        self.entry1.grid(row=1, column=1, padx=1, pady=1)
        button1 = tk.Button(self, text="Next",command=self.Fetch_All)
        button1.grid(row=1, column=2, sticky="nsew", pady=1, padx=1)
        button2 = tk.Button(self, text='Back', font=SMALL_FONT, command=lambda:controller.show_frame('Query'))
        button2.grid(row=3, column=2, padx=1, pady=8)

    def set_TestType(self):
        self.TestType = self.entry1.get()
        self.entry1.delete(0,END)
        self.entry1.insert(0,self.TestType)
        #print(self.TestType)
        return self.TestType

    def Fetch_All(self):
        TestType = self.set_TestType()
        Columns,Results = fecth_all(TestType)
        fname = TestType + '.csv'
        file = open(fname, 'w')
        file.write(Columns + '\n')
        for row in Results:
            str_row = str(row).strip('()')
            #print(str_row)
            file.write(str_row + '\n')
        file.close()
        String = 'Query Finished! Please Check ' + TestType + '.csv File'
        messagebox.askquestion('Message', String)

class QueryCon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label0 = tk.Label(self, text='Condition Query', font=SMALL_FONT)
        label0.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)
        label1 = tk.Label(self, text='Enter Test Type (Table Name)', font=SMALL_FONT)
        label1.grid(row=1, column=0, sticky="nsew", pady=1, padx=1)
        self.entry1 = tk.Entry(self, borderwidth=5, width=30)
        self.entry1.grid(row=1, column=1, padx=1, pady=1)

        label2 = tk.Label(self, text="Enter Conditon\n(e.g: vdd = 'HV' and temperature = 27)", font=SMALL_FONT)
        label2.grid(row=2, column=0, sticky="nsew", pady=1, padx=1)
        self.entry2 = tk.Entry(self, borderwidth=5, width=30)
        self.entry2.grid(row=2, column=1, padx=1, pady=1)

        button1 = tk.Button(self, text="Next", command=self.Fetch_con)
        button1.grid(row=2, column=2, sticky="nsew", pady=1, padx=1)
        button2 = tk.Button(self, text='Back', font=SMALL_FONT, command=lambda:controller.show_frame('Query'))
        button2.grid(row=3, column=2, padx=1, pady=8)

    def set_TestType(self):
        self.TestType = self.entry1.get()
        self.entry1.delete(0,END)
        self.entry1.insert(0,self.TestType)
        #print(self.TestType)
        return self.TestType

    def set_conditions(self):
        self.Conditions = self.entry2.get()
        self.entry2.delete(0,END)
        self.entry2.insert(0,self.Conditions)
        #print(self.TestType)
        return self.Conditions

    def Fetch_con(self):
        TestType = self.set_TestType()
        Conditions = self.set_conditions()
        Columns,Results = fetch_con(TestType,Conditions)
        fname = TestType +'_conditon_query.csv'
        file = open(fname, 'w')
        file.write(Columns + '\n')
        for row in Results:
            str_row = str(row).strip('()')
            #print(str_row)
            file.write(str_row + '\n')
        file.close()
        String = 'Query Finished! Please Check ' + fname +' File'
        messagebox.askquestion('Message', String)


class DB_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label0 = tk.Label(self, text='host', font=SMALL_FONT)
        label0.grid(row=0, column=1, columnspan=2, pady=1, padx=1)
        self.e0_var = StringVar()
        self.e0_var.set('localhost')
        self.entry0 = tk.Entry(self, textvariable=self.e0_var, borderwidth=2, width=25)
        self.entry0.grid(row=1, column=1, columnspan=2, pady=1, padx=1)

        label1 = tk.Label(self, text='database', font=SMALL_FONT)
        label1.grid(row=2, column=1, columnspan=2, pady=1, padx=40)
        self.e1_var = StringVar()
        self.e1_var.set('test')
        self.entry1 = tk.Entry(self, textvariable=self.e1_var, borderwidth=2, width=25)
        self.entry1.grid(row=3, column=1, columnspan=2, pady=1, padx=40)

        label2 = tk.Label(self, text='user', font=SMALL_FONT)
        label2.grid(row=0, column=3, columnspan=2, pady=1, padx=20)
        self.e2_var = StringVar()
        self.e2_var.set('root')
        self.entry2 = tk.Entry(self, textvariable=self.e2_var, borderwidth=2, width=25)
        self.entry2.grid(row=1, column=3, columnspan=2, pady=1, padx=20)

        label3 = tk.Label(self, text='password', font=SMALL_FONT)
        label3.grid(row=2, column=3, columnspan=2, pady=1, padx=20)
        self.e3_var = StringVar()
        self.e3_var.set('InnoSD2015')
        self.entry3 = tk.Entry(self, textvariable=self.e3_var, borderwidth=2, width=25)
        self.entry3.grid(row=3, column=3, columnspan=2, pady=1, padx=20)

        button1 = tk.Button(self, text="Set", command=self.Set)
        button1.grid(row=4, column=5, sticky="nsew", pady=10, padx=1)
        button2 = tk.Button(self, text='Back', font=SMALL_FONT, command=lambda: controller.show_frame('StartPage'))
        button2.grid(row=5, column=5, padx=10, pady=1)

    def GetValues(self):
        self.host = self.entry0.get()
        self.entry0.delete(0, END)
        self.entry0.insert(0, self.host)

        self.database = self.entry1.get()
        self.entry1.delete(0, END)
        self.entry1.insert(0, self.database)

        self.user = self.entry2.get()
        self.entry2.delete(0, END)
        self.entry2.insert(0, self.user)

        self.password = self.entry3.get()
        self.entry3.delete(0, END)
        self.entry3.insert(0, self.password)

    def Set(self):
        self.GetValues()
        fname = 'config.ini'
        f = open(fname, 'w')
        f.write('[mysql]\n')
        f.write('host = ' + self.host + '\n')
        f.write('database = ' + self.database + '\n')
        f.write('user = ' + self.user + '\n')
        f.write('password = ' + self.password + '\n')
        String = 'Data Base Settings Updated!'
        messagebox.askquestion('Message', String)









app = DataBase()
app.mainloop()

