CREATE DATABASE ed2;

use ed2;

CREATE TABLE usuario (
	idUsuario INT PRIMARY KEY AUTO_INCREMENT,
	nome varchar(255),
	email varchar(255)
);

CREATE TABLE livro (
	idLivro INT PRIMARY KEY AUTO_INCREMENT,
	titulo varchar(255),
	anoPub char(4),
	autor varchar(255),
	disponivel BOOLEAN DEFAULT TRUE
);

CREATE TABLE emprestimo (
	idEmprestimo INT PRIMARY KEY AUTO_INCREMENT,
	idLivro INT,
	idUsuario INT,
	dataEmprestimo varchar(255),
	dataDevolucao varchar(255),
	CONSTRAINT idLivro FOREIGN KEY (idLivro) REFERENCES livro(idLivro),
	CONSTRAINT idUsuario FOREIGN KEY (idUsuario) REFERENCES usuario(idUsuario)
);