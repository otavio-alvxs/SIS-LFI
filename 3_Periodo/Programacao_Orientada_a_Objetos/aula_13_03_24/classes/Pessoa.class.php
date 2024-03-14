<?php

class Pessoa {
    public $Codigo;
    public $Nome;
    public $Altura;
    public $Idade;
    public $Nascimento;
    public $Escolaridade;
    public $Salario;

    // Método Crescer
    // Aumenta a altura em centímetros

    function Crescer($centimetros){
        if ($centimetros>0) {
            $this->Altura += $centimetros;
        }
    }

    // Método Formar
    // Altera a escolaridade para $titulacao

    function Formar($titulacao) {
        $this->Escolaridade = $titulacao;
    }

    // Método Envelhecer
    // Aumenta a idade em $Anos

    function Envelhecer($anos){
        if ($anos>0){
            $this->Idade += $anos;
        }
    }
}