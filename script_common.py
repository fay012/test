import mysql.connector
from  mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config

def run_script_common(TestType):
    filename = TestType+'_script.sql'
    file = open(filename,'w')
    file.write('DROP TABLE IF EXISTS' + '`'+TestType+'`;\n')
    file.write('create table ' + TestType + '(\n    temperature float(10,2) not null,\n    vdd varchar(8) not null,\n    script varchar(60) not null,\n    v_1v5 float(7,4) not null,\n    I_1v5 float(7,4) not null,\n    v_3v float(7,4) not null,\n    I_3v float(7,4) not null,\n    primary key (temperature, vdd, script)\n)ENGINE=InnoDB DEFAULT CHARSET=utf8;\n')
    #file.write("load data infile 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/" + filename + "'\ninto table " + TestType + "\nfields terminated by ','\n")
    #file.write(r"lines terminated by '\r\n'")
    #file.write('\nignore 1 rows;\n')
    file.close()
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        file = open(filename,'r')
        for sql in file.read().split(';'):
            cursor.execute(sql)
        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    run_script_common('current_test')