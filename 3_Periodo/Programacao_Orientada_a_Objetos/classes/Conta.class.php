<?php

class Conta {
    public $Agencia;
    public $Codigo;
    public $DataDeCriacao;
    public $Titular;
    public $Senha;
    public $Saldo;
    public $Cancelada;


    function __construct($Agencia, $Codigo, $DataDeCriacao, $Titular, $Senha, $Saldo) {
        $this->Agencia = $Agencia;
        $this->Codigo = $Codigo;
        $this->DataDeCriacao = $DataDeCriacao;
        $this->Titular = $Titular;
        $this->Senha = $Senha;

        #Chamada a outro método da Classe 
        $this->Depositar($Saldo);
        $this->Cancelada = false;
    }

    /*
    Método Retirar
    Diminui o Saldo em $quantia
    */
    function Retirar($quantia){
        if ($quantia>0){
            $this->Saldo -= $quantia;
        }
    }

    /*
    Método Depositar
    Aumenta Saldo em $Quantia
    */
    function Depositar($quantia){
        if ($quantia>0){
            $this->Saldo += $quantia;
        }
    }

    /*
    Método ObterSaldo
    Retorna o saldo atual
    */
    function ObterSaldo(){
        return $this->Saldo;
    }

    function __destruct() {
        echo "<br>
        Objeto Conta {$this->Codigo} de {$this->Titular->Nome}
        finalizada...
        <br>";
    }
    
}
