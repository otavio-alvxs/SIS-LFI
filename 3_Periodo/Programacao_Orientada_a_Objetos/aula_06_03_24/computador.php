<?php

class Computador
{
    var $cpu;
    function ligar()
    {
        echo "Ligando computador a {$this->cpu}...\n";
    }
}

$obj = new Computador;
$obj->cpu = "500Mhz";
$obj->ligar();

$novoobj = new Computador;
$novoobj->cpu = readline("Insira a velocidade da CPU: ");
$novoobj->ligar();
