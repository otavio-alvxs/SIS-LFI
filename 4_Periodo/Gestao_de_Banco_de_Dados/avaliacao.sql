CREATE DATABASE rh

USE rh

CREATE USER 'rhuser'@'localhost' IDENTIFIED BY 'Libert@s';

GRANT ALL PRIVILEGES ON rh.* TO 'rhuser'@'localhost';

FLUSH PRIVILEGES;

CREATE TABLE funcionarios (
id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
sobrenome VARCHAR(50) NOT NULL,
data_nascimento DATE,
id_cargo VARCHAR(20),
id_departamento INT,
salario DECIMAL(10,2)
);

CREATE TABLE departamentos (
id_departamento INT PRIMARY KEY AUTO_INCREMENT,
nome_departamento VARCHAR(50) NOT NULL
);

CREATE TABLE cargos (
id_cargo VARCHAR(20) PRIMARY KEY,
nome_cargo VARCHAR(50) NOT NULL
);

CREATE TABLE treinamentos (
id_treinamento INT PRIMARY KEY AUTO_INCREMENT,
nome_treinamento VARCHAR(100) NOT NULL,
data_inicio DATE,
data_fim DATE,
carga_horaria INT,
local VARCHAR(100),
ministrante VARCHAR(100),
id_funcionario INT
);

ALTER TABLE treinamentos
ADD CONSTRAINT fk_id_funcionario 
FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
ON DELETE RESTRICT;

ALTER TABLE funcionarios
ADD CONSTRAINT fk_id_cargo
FOREIGN KEY (id_cargo) REFERENCES cargos(id_cargo)
ON DELETE RESTRICT;

ALTER TABLE funcionarios
ADD CONSTRAINT fk_id_departamento
FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
ON DELETE RESTRICT;

INSERT INTO funcionarios (nome, sobrenome, data_nascimento, id_cargo, id_departamento, salario) 
VALUES ('João', 'Silva', '1980-05-15', 'DIRETOR', 4, 15000.00);

INSERT INTO funcionarios (nome, sobrenome, data_nascimento, id_cargo, id_departamento, salario) 
VALUES ('Maria', 'Oliveira', '1990-08-20', 'ASSISTENTE', 5, 3000.00);

INSERT INTO treinamentos (nome_treinamento, data_inicio, data_fim, carga_horaria, `local`,
ministrante, id_funcionario)
VALUES
('Introdução ao SQL', '2024-01-01', '2024-01-05', 20, 'Sala de treinamento', 'João Silva',
1),
('Gestão de Projetos', '2024-03-15', '2024-03-20', 30, 'Auditório', 'Maria Santos', 2),
('Desenvolvimento Web', '2024-05-10', '2024-05-25', 40, 'Laboratório', 'Pedro Almeida', 3);

INSERT INTO treinamentos (nome_treinamento, data_inicio, data_fim, carga_horaria, local, ministrante, id_funcionario) 
VALUES ('Introdução ao SQL', '2024-01-10', '2024-01-15', 20, 'Sala de treinamento', 'Carlos Silva', 1);

INSERT INTO treinamentos (nome_treinamento, data_inicio, data_fim, carga_horaria, local, ministrante, id_funcionario) 
VALUES ('Gestão de Projetos', '2024-02-01', '2024-02-05', 16, 'Laboratório', 'Ana Costa', 2);

INSERT INTO treinamentos (nome_treinamento, data_inicio, data_fim, carga_horaria, local, ministrante, id_funcionario) 
VALUES ('Excel Avançado', '2024-03-01', '2024-03-03', 12, 'Auditório', 'Roberto Lima', 3);

SELECT *
FROM funcionarios f
JOIN cargos c ON f.id_cargo = c.id_cargo
JOIN departamentos d ON f.id_departamento = d.id_departamento
LEFT JOIN treinamentos t ON f.id_funcionario = t.id_funcionario;

SELECT f.nome, f.sobrenome, c.nome_cargo, d.nome_departamento, f.salario
FROM funcionarios f
JOIN cargos c ON f.id_cargo = c.id_cargo
JOIN departamentos d ON f.id_departamento = d.id_departamento;

SELECT *
FROM funcionarios
WHERE id_funcionario IN (1, 3, 5);

SELECT MAX(salario) AS maior_salario, MIN(salario) AS menor_salario
FROM funcionarios;

SELECT CONCAT(nome, ' ', sobrenome) AS nome_completo, salario
FROM funcionarios;

SELECT f.*
FROM funcionarios f
JOIN departamentos d ON f.id_departamento = d.id_departamento
WHERE d.nome_departamento = 'Tecnologia da Informação';

SELECT AVG(salario) AS media_salarial
FROM funcionarios;

SELECT *
FROM funcionarios
WHERE MONTH(data_nascimento) = 1;

SELECT AVG(TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE())) AS idade_media
FROM funcionarios;

SELECT f.*
FROM funcionarios f
JOIN treinamentos t ON f.id_funcionario = t.id_funcionario
WHERE t.nome_treinamento = 'Introdução ao SQL';