	drop database if exists PeTAG;
	create database PeTAG;
	use PeTAG;

	create table Usuario(
		userID INT AUTO_INCREMENT primary key,
		nome varchar(40),
		email varchar(40),
		senha varchar(40)
	);

	create table Dispositivo(
		idDispositivo INT AUTO_INCREMENT primary key,
		nomeDispositivo varchar(40),
		longitude float(20),
		latitude float(20)
	);

	create table HistoricoCoordenadas (
	idHistorico INT AUTO_INCREMENT PRIMARY KEY,
	idDispositivo INT,
	latitude FLOAT(20),
	longitude FLOAT(20),
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (idDispositivo) REFERENCES Dispositivo(idDispositivo)
	);

	INSERT INTO Usuario (userID, nome, email, senha) 
	VALUES 
	(1, 'João', 'joão@gmail.com', 'senha123');

	INSERT INTO Dispositivo	 (nomeDispositivo, latitude, longitude) 
	VALUES 
	('Rex', 0, 0);

	update Dispositivo set latitude = -22.95278084088744 , longitude = -46.54846591250378 where idDispositivo = 1;
    update Dispositivo set latitude = 48.85286423416817 , longitude = 2.370712607481553 where idDispositivo = 1;
	 update Dispositivo set latitude = 0 , longitude = 0 where idDispositivo = 1;

	select * from HistoricoCoordenadas;