CREATE DATABASE creditcard;

USE creditcard;

CREATE TABLE IF NOT EXISTS transaction (
    cc_num VARCHAR(255),
    trans_time TIMESTAMP,
    trans_num VARCHAR(255),
    category VARCHAR(255),
    merchant VARCHAR(255),
    amt DOUBLE PRECISION,
    merch_lat DOUBLE PRECISION,
    merch_long DOUBLE PRECISION,
    distance DOUBLE PRECISION,
    age INT,
    is_fraud INT,
    PRIMARY KEY(cc_num, trans_time)
);

CREATE TABLE IF NOT EXISTS customer (
    cc_num VARCHAR(255),
    first VARCHAR(255),
    last VARCHAR(255),
    gender VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip VARCHAR(255),
    latt DOUBLE PRECISION,
    longt DOUBLE PRECISION,
    job VARCHAR(255),
    dob TIMESTAMP,
    PRIMARY KEY(cc_num)
);