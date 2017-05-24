create table test11(
    temperature float(10,2) not null,
    ,
    ,
    ,
    ,
    ,
    ,
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

load data local infile 'C:/Users/jianxu/PycharmProjects/sqltest/current.csv'
into table test11
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows;