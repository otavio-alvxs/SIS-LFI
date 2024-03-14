<?php

// insere a classe
include_once 'classes/Produto.class.php';

$produto = new Produto;
$produto2 = new Produto;

$produto->Codigo = 4001;
$produto->Descricao = 'CD - The best of Eric Clapton';
$produto2->Codigo = 4002;
$produto2->Descricao = 'CD - da Xuxa';
$produto->ImprimeEtiqueta();
$produto2->ImprimeEtiqueta();
