
''' CRIA O DATABASE QUE CONTEM AS INFORMAÇOES DO CLIENTE'''
CREATE DATABASE hotel_db;

USE hotel_db;

CREATE TABLE cliente (
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    quarto INTEGER NOT NULL,
    check_in DATETIME,
    check_out DATETIME,
    cafe_manha BOOLEAN,
    periodo VARCHAR (40),

    cpf (PRIMARY KEY)
);