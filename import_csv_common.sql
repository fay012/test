create table current1(
	temperature float(10,2) not null,
    vdd varchar(8) not null,
    script varchar(60) not null,
    v_1v5 float(7,4) not null,
    I_1v5 float(7,4) not null,
    v_3v float(7,4) not null,
    I_3v float(7,4) not null,
    primary key (temperature, vdd, script)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;