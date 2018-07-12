create schema `app-heroi-social`;


use `app-heroi-social`;

LOAD DATA INFILE 'C:\Users\gabyz\PycharmProjects\heroi-social\app\controllers\endereco.csv'
INTO TABLE endereco
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r'
IGNORE 1 ROWS #Comando para ignorar a primeira linha do arquivo .txt
(codlocal,local1,local2,complemento,numero,bairro,latitude,longitude);

