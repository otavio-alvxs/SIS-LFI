<?php

#Carrega as classes
include_once 'classes/Pessoa.class.php';
include_once 'classes/Conta.class.php';

#Criação do objeto Carlos
$carlos = new Pessoa(10,'Carlos da Silva', '18', 185, '10/04/1976', 'Ensino médio', 650.00);
// $carlos->Codigo = 10;
// $carlos->Nome = 'Carlos da Silva';
// $carlos->Altura = 185;
// $carlos->Idade = 25;
// $carlos->Nascimento = '10/04/1976';
// $carlos->Escolaridade = 'Ensino médio';

echo "Manipulando o objeto {$carlos->Nome}: <br>";

echo "{$carlos->Nome} é formado em: {$carlos->Escolaridade} <br>";
$carlos->Formar('Técnico em Eletricidade');
echo "{$carlos->Nome} é formado em: {$carlos->Escolaridade} <br>";

$conta_carlos = new Conta(6677, 'CC.12346-5', '10/07/2022', $carlos, 9876, 567.89);
// $conta_carlos->Agencia = 6677;
// $conta_carlos->Codigo = 'CC.12346-5';
// $conta_carlos->DataDeCriacao = '10/07/2022';
// $conta_carlos->Titular = $carlos;
// $conta_carlos->Senha = 9876;
// $conta_carlos->Saldo = 567.89;
// $conta_carlos->Cancelada = false;

echo '<br>';
echo "Manipulando a conta de: {$conta_carlos->Titular->Nome} <br>";
echo "O saldo atual é R\$ {$conta_carlos->ObterSaldo()} <br>";

$conta_carlos->Depositar(10);
echo "O saldo atual é R\$ {$conta_carlos->ObterSaldo()} <br>";

$conta_carlos->Retirar(10);
echo "O saldo atual é R\$ {$conta_carlos->ObterSaldo()} <br>";
