import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from common_func import *



def fetch_all(TestType):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql0 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + TestType + "';"
        cursor.execute(sql0)
        columns_temp = cursor.fetchall()
        columns = ''
        for c in columns_temp:
            c = str(c).strip('()')
            c = c.strip("',")
            columns = columns + ', ' + c
        columns = columns.strip(',')
        sql = "select * from " + TestType
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(columns)
        #print(columns,results)
        return columns,results
    except Error as e:
        print(e)

def fetch_con(TestType, conditions):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql0 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + TestType + "';"
        cursor.execute(sql0)
        columns_temp = cursor.fetchall()
        columns = ''
        for c in columns_temp:
            c = str(c).strip('()')
            c = c.strip("',")
            columns = columns + ', '+c
        columns = columns .strip(',')
        sql = "select * from " + TestType +'\n where ' + conditions + ';'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(columns,results)
        return columns,results
    except Error as e:
        print(e)

def fetch_key(TestType, *keys):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        columns_temp = []
        #column_type = ''
        columns =''
        columns_print = ''
        items = str(keys).strip("()").split(',')
        for item in items:
            key = str(item).strip('""')
            sql0 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + TestType + "' and COLUMN_NAME = " + key +";"
            #print(sql0)
            cursor.execute(sql0)
            columns_temp = columns_temp + cursor.fetchall()
        #print(columns_temp)
        for c in columns_temp:
            column = str(c).strip('()')
            columns = columns + column
            columns_print = columns_print + ', ' + column.strip("',")
            column_type = columns.strip(",")
        columns_print = columns_print.strip(',')
        c1 = column_type.split(',')
        c3 = ''
        for c2 in c1:
            c3 = c3+ ', ' + c2.strip("''")
            c3 = c3.strip(',')
        sql = "select " +  c3 + " from " + TestType + ';'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(columns_print)
        print(columns_print,results)
        return columns_print,results
    except Error as e:
        print(e)

def fetch_key_con(TestType, conditions, *keys):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        columns_temp = []
        columns =''
        columns_print = ''
        items = str(keys).strip("()").split(',')
        for item in items:
            key = str(item).strip('""')
            sql0 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + TestType + "' and COLUMN_NAME = " + key +";"
            #print(sql0)
            cursor.execute(sql0)
            columns_temp = columns_temp + cursor.fetchall()
        for c in columns_temp:
            column = str(c).strip('()')
            columns = columns + column
            columns_print = columns_print + ', ' + column.strip("',")
            column_type = columns.strip(",")
        columns_print = columns_print.strip(',')
        c1 = column_type.split(',')
        c3 = ''
        for c2 in c1:
            c3 = c3+ ', ' + c2.strip("''")
            c3 = c3.strip(',')
        sql = "select " + c3 + " from " + TestType + '\n where ' + conditions + ';'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(columns_print,results)
        return columns_print,results
    except Error as e:
        print(e)


if __name__ == '__main__':
    #columns,results = fetch_all('current')
    #print(columns.split(','))
    fetch_key('current','temperature','vdd',' ')
