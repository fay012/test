import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from common_func import *

def ScriptGen(csv_name, TestType):

    name = TestType
    script_name = TestType + '.sql'

    script = open(script_name, 'w')

    #script.write('DROP TABLE IF EXISTS `'+ name + '`;\n')
    script.write('create table ' + name + '(\n')
    filename = csv_name
    file = open(filename, 'r')
    columns = file.readline().strip().split(',')
    fp = r'data_type.txt'
    #print(columns)
    for column in columns:
        if column != '':
            type = getvalue(fp, column, 'cmd')
            script.write('    ' +type + ',\n')
    fs = r'key_for_test.txt'
    key = getvalue(fs, TestType, 'primary key' )
    script.write('    ' + key + '\n')
    script.write(')ENGINE=InnoDB DEFAULT CHARSET=utf8;\n')
    script.write('\n')
    script.write("load data local infile '" + csv_name +  "'")
    script.write('\ninto table ' + name + '\n')
    script.write("fields terminated by ','\n")
    script.write(r"lines terminated by '\r\n'")
    script.write('\nignore 1 rows;')


def ScriptGen_temp(csv_name,TestType):
    script_name = 'temp.sql'
    name = 'temp'
    script = open(script_name, 'w')

    script.write('DROP TABLE IF EXISTS `' + name + '`;\n')
    script.write('create table ' + name + '(\n')
    filename = csv_name
    file = open(filename, 'r')
    columns = file.readline().strip().split(',')
    fp = r'data_type.txt'
    # print(columns)
    for column in columns:
        if column != '':
            type = getvalue(fp, column, 'cmd')
            script.write('    ' + type + ',\n')
    fs = r'key_for_test.txt'
    key = getvalue(fs, TestType, 'primary key')
    script.write('    ' + key + '\n')
    script.write(')ENGINE=InnoDB DEFAULT CHARSET=utf8;\n')
    script.write('\n')
    script.write("load data local infile '" + csv_name + "'")
    script.write('\ninto table ' + name + '\n')
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
            #print(sql)
        conn.commit()

    except Error as e:
        print(e)

def Merge(TestType):
    script_name = 'Merge.sql'
    script = open(script_name, 'w')
    script.write('insert ignore into ' + TestType + '\n')
    script.write('select * from temp\n')
    script.close()

def Import_first(TestType,csv_name):
    ScriptGen(csv_name, TestType)
    Run_script(TestType)
    print('Importing Data to '+ TestType + '...')
    print('Finished')

def Import(csv_name,TestType):
    print('Importing Data...')
    ScriptGen_temp(csv_name,TestType)
    Run_script('temp')
    print('Finished')

def Merge_Data(TestType):
    print('Append To Table ' + TestType)
    Merge(TestType)
    Run_script('Merge')
    print('Finished')


if __name__ == '__main__':
    TestType = 'current'
    csv_name = 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/current_0824_182241.csv'
    Import_first(TestType,csv_name)
    #Import(csv_name,TestType)
    #Merge_Data(TestType)

