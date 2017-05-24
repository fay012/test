create table current_test(
    temperature float(10,2) not null,
    vdd varchar(8) not null,
    script varchar(60) not null,
    V_1v5_V float(7,4) not null,
    I_1v5_A float(7,4) not null,
    V_3v_V float(7,4) not null,
    I_3v_A float(7,4) not null,
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

load data infile 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/current_0822_193338.csv'
into table current_test
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows;