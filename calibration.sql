create table calibration(
    temperature float(10,2) not null,
    vdd varchar(8) not null,
    script varchar(60) not null,
    boardname varchar(60) not null,
    freq_center_MHz float(10,4) not null,
    lna2_cap_band tinyint(4) not null,
    lna2_cap_coarse tinyint(4) not null,
    lna2_cap_fine tinyint(4) not null,
    lna2_cap_cs_0 tinyint(4) not null,
    lna2_cap_cs_2 tinyint(4) not null,
    lna2_cap_cs_4 tinyint(4) not null,
    lna2_cap_cs_6 tinyint(4) not null,
    lna3_cap_band tinyint(4) not null,
    lna3_cap_coarse tinyint(4) not null,
    lna3_cap_fine tinyint(4) not null,
    lna2_cap_cs_1 tinyint(4) not null,
    lna2_cap_cs_3 tinyint(4) not null,
    lna2_cap_cs_5 tinyint(4) not null,
    lna2_cap_cs_7 tinyint(4) not null,
    lo_coarse tinyint(4) not null,
    lo_fine tinyint(4) not null,
    ilo_band tinyint(4) not null,
    ilo_pvt tinyint(4) not null,
    ilo_acq tinyint(4) not null,
    ilo_track tinyint(4) not null,
    fcenter_MHz float(10,4) not null,
    bandwidth_MHz float(10,4) not null,
    Q float(10,4) not null,
    primary key (temperature, vdd, boardname,freq_center_MHz)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

load data local infile 'C:/datatool/C09_Deg_ta_lnacal_0621_074005.csv'
into table calibration
fields terminated by ','
lines terminated by '\r\n'
ignore 1 rows;