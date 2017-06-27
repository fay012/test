DROP TABLE IF EXISTS `temp`;
create table temp(
    temperature float(10,2) not null,
    vdd varchar(8) not null,
    script varchar(60) not null,
    V_1v5_V float(7,4) not null,
    I_1v5_A float(7,4) not null,
    V_3v_V float(7,4) not null,
    I_3v_A float(7,4) not null,
    primary key (temperature, vdd, script)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

load data local infile 'C:/datatool/current_0824_182241.csv'
into table temp
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows;