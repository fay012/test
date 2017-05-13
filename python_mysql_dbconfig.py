from configparser import ConfigParser

def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        #print(items)
        for item in items:
            #print(item)
            db[item[0]] = item[1] #dict, key: item[0], value: item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section,filename))
    return db
if __name__ == '__main__':
    read_db_config()
