CREATE DATABASE ed2;

use ed2;

DROP TABLE usuario, livro;

CREATE TABLE usuario (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome varchar(255),
	email varchar(255)
);

CREATE TABLE livro (
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo varchar(255),
	anoPub char(4),
	autor varchar(255)
);