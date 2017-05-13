import mysql.connector
from  mysql.connector import Error, MySQLConnection
#from python_mysql_dbconfig import read_db_config

def connect():
    """Connect to Mysql database"""
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database = 'python_mysql',
                                       user='root',
                                       password='InnoSD2015')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()




if __name__ == '__main__':
    connect()