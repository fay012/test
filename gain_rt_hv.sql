create table gain_rt_hv(
    temperature varchar(8) not null,
    vdd varchar(8) not null,
    script varchar(60) not null,
    boardname varchar(60) not null,
    freq_MHz float(10,4) not null,
    amplitude_dBm float(10,4) not null,
    gain_dB float(10,4) not null,
    primary key (temperature, vdd, boardname,freq_MHz)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

load data local infile 'C:/Users/jianxu/PycharmProjects/sqltest/C09/C09_2412MHz_gain_sweep_0612_134807.csv'
into table gain_rt_hv
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows;