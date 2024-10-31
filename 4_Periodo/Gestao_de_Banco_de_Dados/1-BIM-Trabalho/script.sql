CREATE DATABASE livros;

USE livros;

CREATE USER 'libertass'@'%' IDENTIFIED BY 'Alunos4p';

GRANT ALL PRIVILEGES ON livros.* TO 'libertass'@'%';

FLUSH PRIVILEGES;

CREATE TABLE autores (
    idautor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE livros (
    idlivros INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    titulo VARCHAR(255),
    idautor INT,
    anopub YEAR,
    CONSTRAINT fkidautor
    FOREIGN KEY (idautor) 
    REFERENCES autores(idautor)
);

CREATE TABLE emprestimos (
    idemprestimo INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    idlivros INT,
    dataEmprestimo VARCHAR(10),
    dataDevolucao VARCHAR(10),
  	CONSTRAINT fklivroid  
    FOREIGN KEY (idlivros) 
    REFERENCES livros(idlivros)
);

INSERT INTO livros (titulo, idautor, anopub) VALUES ('Harry Potter e a Pedra Filosofal', 1, 1997);
INSERT INTO livros (titulo, idautor, anopub) VALUES ('As Crônicas de Gelo e Fogo', 2, 1996);
INSERT INTO livros (titulo, idautor, anopub) VALUES ('O Senhor dos Anéis', 3, 1954);

INSERT INTO autores (nome) VALUES ('J.K. Rowling');
INSERT INTO autores (nome) VALUES ('George R.R. Martin');
INSERT INTO autores (nome) VALUES ('J.R.R. Tolkien');

INSERT INTO emprestimos (idlivros, dataEmprestimo, dataDevolucao) VALUES (8, '2024-08-01', '2024-08-15');
INSERT INTO emprestimos (idlivros, dataEmprestimo, dataDevolucao) VALUES (9, '2024-08-05', '2024-08-20');
INSERT INTO emprestimos (idlivros, dataEmprestimo, dataDevolucao) VALUES (10, '2024-08-10', '2024-08-25');

select * from emprestimos

-- consulta1 

select * from livros;

-- consulta2

select * from autores;

-- consulta3

SELECT l.idlivros AS id, l.titulo, a.nome AS autor_nome
FROM livros l
JOIN autores a ON l.idautor = a.idautor;

-- consulta4

SELECT l.titulo, COUNT(e.idemprestimo) AS qtdEmprestimo
FROM livros l
LEFT JOIN emprestimos e ON l.idlivros = e.idlivros
GROUP BY l.titulo;
