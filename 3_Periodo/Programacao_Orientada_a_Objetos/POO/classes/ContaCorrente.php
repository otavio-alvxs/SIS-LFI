<?php
class ContaCorrente extends Conta {
    public $Limite;

    function __construct($Agencia, $Codigo, $DataDeCriacao, $Titular, $Senha, $Saldo, $Limite) {
        parent::__construct($Agencia, $Codigo, $DataDeCriacao, $Titular, $Senha, $Saldo);
        $this->Limite = $Limite;
    }
    
    function Retirar($Quantia) {
        if (($this->Saldo + $this->Limite) >= $Quantia){
            parent::Retirar($Quantia);
        } else {
            echo "Retirada não permitida... <br>";
            return false;
        }
        return true;
    }
}
