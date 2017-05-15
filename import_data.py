import mysql.connector
from  mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config

def ScriptGen(csv_name):
    script_name = 'temp.sql'
    script = open(script_name, 'w')
    script.write('DROP TABLE IF EXISTS `temp`;\n')
    script.write(
        'create table temp(\n    temperature float(10,2) not null,\n    vdd varchar(8) not null,\n    script varchar(60) not null,\n    v_1v5 float(7,4) not null,\n    I_1v5 float(7,4) not null,\n    v_3v float(7,4) not null,\n    I_3v float(7,4) not null,\n    primary key (temperature, vdd, script)\n)ENGINE=InnoDB DEFAULT CHARSET=utf8;\n')
    script.write('\n')
    script.write("load data infile 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/" + csv_name + ".csv'")
    script.write('\ninto table temp\n')
    script.write("fields terminated by ','\n")
    script.write(r"lines terminated by '\r\n'")
    script.write('\nignore 1 rows;')

def Run_script(script_name):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        filename = script_name + '.sql'
        file = open(filename,'r')
        for sql in file.read().split(';'):
            cursor.execute(sql)
            print(sql)
        conn.commit()

    except Error as e:
        print(e)

def Merge(TestType):
    script_name = 'Merge.sql'
    script = open(script_name, 'w')
    script.write('insert ignore into ' + TestType + '\n')
    script.write('select * from temp\n')
    script.close()

if __name__ == '__main__':
    ScriptGen('current_0822_193338')
    Run_script('temp')
    Merge('current_test')
    Run_script('Merge')
