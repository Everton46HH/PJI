drop database if exists PeTAG ;
create database PeTAG;

use PeTAG;

create table Usuario(
	userID INT primary key,
    nome varchar(40),
    email varchar(40),
    senha varchar(40)
);
create table Dispositivo(
	idDispositivo INT primary key,
    nomeDispositivo varchar(40),
    longitude float(20),
    latitude float(20)
);

INSERT INTO Usuario (userID, nome, email, senha) 
VALUES 
(1, 'João', 'joão@gmail.com', 'senha123');

INSERT INTO Dispositivo	 (idDispositivo, nomeDispositivo, latitude, longitude) 
VALUES 
(1, 'Rex', 0, 0);

UPDATE Usuario
SET latitude = '4.86484812877389'
WHERE idDispositivo = 1;
commit;