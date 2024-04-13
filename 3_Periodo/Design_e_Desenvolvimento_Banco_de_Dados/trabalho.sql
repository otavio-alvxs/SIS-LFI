CREATE DATABASE trabalho;

USE trabalho;

CREATE TABLE Marca (
    idmarca INT PRIMARY KEY,
    nomeMarca VARCHAR(255)
);

CREATE TABLE Produto (
    idproduto INT PRIMARY KEY,
    descricao VARCHAR(255),
    precocusto DECIMAL(10, 2),
    precovenda DECIMAL(10, 2),
    saldoestoque INT,
    codbarras VARCHAR(50),
    idmarca INT,
    FOREIGN KEY (idmarca) REFERENCES Marca(idmarca)
);

CREATE TABLE Cidade (
    idcidade INT PRIMARY KEY,
    nomecidade VARCHAR(255),
    uf VARCHAR(2)
);

CREATE TABLE Cliente (
    idcliente INT PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(14),
    logradouro VARCHAR(255),
    numero INT,
    bairro VARCHAR(255),
    cep VARCHAR(9),
    telefone VARCHAR(15),
    idcidade INT,
    FOREIGN KEY (idcidade) REFERENCES Cidade(idcidade)
);

CREATE TABLE Fornecedor (
    idfornecedor INT PRIMARY KEY,
    nome VARCHAR(255),
    cnpj VARCHAR(18),
    logradouro VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(9),
    telefone VARCHAR(15),
    idcidade INT,
    FOREIGN KEY (idcidade) REFERENCES Cidade(idcidade)
);

CREATE TABLE Vendedor (
    idvendedor INT PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(14),
    logradouro VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(9),
    telefone VARCHAR(15),
    percentualcomissao INT,
    idcidade INT,
    FOREIGN KEY (idcidade) REFERENCES Cidade(idcidade)
);

CREATE TABLE Venda (
    idvenda INT PRIMARY KEY,
    numeroNf INT,
    data DATE,
    quantidade INT,
    valor INT,
    comissao INT,
    idcliente INT,
    idvendedor INT,
    FOREIGN KEY (idcliente) REFERENCES Cliente(idcliente),
    FOREIGN KEY (idvendedor) REFERENCES Vendedor(idvendedor)
);

CREATE TABLE Compra (
    idcompra INT PRIMARY KEY,
    numeroNf INT,
    data DATE,
    quantidade INT,
    valor DECIMAL(10, 2),
    idfornecedor INT,
    FOREIGN KEY (idfornecedor) REFERENCES Fornecedor(idfornecedor)
);

CREATE TABLE Caixa (
    idcaixa INT PRIMARY KEY,
    data DATE,
    descricao VARCHAR(255),
    valor INT,
    debitocredito VARCHAR(1)
);

CREATE TABLE ContasReceber (
    idreceber INT PRIMARY KEY,
    data DATE,
    valor INT,
    vencimento DATE,
    pagamento DATE,
    valorpago INT,
    idcliente INT,
    FOREIGN KEY (idcliente) REFERENCES Cliente(idcliente)
);

CREATE TABLE ContasPagar (
    idpagar INT PRIMARY KEY,
    data DATE,
    valor DECIMAL(10, 2),
    vencimento DATE,
    pagamento DATE,
    valorpago INT,
    idfornecedor INT,
    idcompra INT,
    idcaixa INT,
    FOREIGN KEY (idfornecedor) REFERENCES Fornecedor(idfornecedor),
    FOREIGN KEY (idcompra) REFERENCES Compra(idcompra),
    FOREIGN KEY (idcaixa) REFERENCES Caixa(idcaixa)
);

CREATE TABLE Usuarios (
    idusuario INT PRIMARY KEY,
    login VARCHAR(255),
    senha VARCHAR(255),
    email VARCHAR(255)
);
