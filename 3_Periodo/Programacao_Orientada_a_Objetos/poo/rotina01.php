<?php
//captura valor variável
$umidade = readline("Insira o valor da unidade: ");
//Testa se é maior que 90. Retorna um boolean
$vai_chover = ($umidade>90);

//testa se $vai_chover é verdadeiro
if ($vai_chover){
    echo 'Esta chovendo';
}else{
    echo 'Não está chovendo';
}
