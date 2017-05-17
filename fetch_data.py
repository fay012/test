import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from common_func import *



def fecth_all(TestType):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql0 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + TestType + "';"
        cursor.execute(sql0)
        columns = str(cursor.fetchall()).strip('[]')
        #print(columns)
        sql = "select * from " + TestType
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(results)
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
        columns = str(cursor.fetchall()).strip('[]')
        sql = "select * from " + TestType +'\n where ' + conditions + ';'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(columns,results)
        return columns,results
    except Error as e:
        print(e)

if __name__ == '__main__':
    fetch_con('current',"vdd = 'HV' and temperature = 27")