import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from common_func import *

def get_parlist(TestType):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql0 = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + TestType + "';"
        cursor.execute(sql0)
        temp = cursor.fetchall()
        #print(temp)
        col = ''
        for c in temp:
            c = str(c).strip('()')
            c = c.strip("',")
            col = col + ',' + c
        col = col.strip(',')
        #print(col)
        #print(col,output)
        output = col.split(',')
        return output
    except Error as e:
        print(e)

if __name__ == '__main__':
    print(get_parlist('current'))
