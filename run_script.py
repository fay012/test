#https://www.quora.com/How-can-I-execute-a-sql-file-in-Python
import mysql.connector
from  mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config

def run_script():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        filename = 'input_csv_test2.sql'
        file = open(filename,'r')
        #sql = s =" ".join(file.readlines())
        #print(sql)
        for sql in file.read().split(';'):
            #print(sql)
            cursor.execute(sql)
        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_script()