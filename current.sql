create table current(
    temperature float(10,2) not null,
    ,
    ,
    ,
    ,
    ,
    ,
    primary key (temperature, vdd, script)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

load data local infile 'C:/Users/jianxu/PycharmProjects/sqltest/current.csv'
into table current
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows;