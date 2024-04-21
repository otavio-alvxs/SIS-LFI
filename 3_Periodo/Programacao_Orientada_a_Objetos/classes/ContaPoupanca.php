<?php
class ContaPoupanca extends Conta {
    public $Aniversario;

    function __construct($Agencia, $Codigo, $DataDeCriacao, $Titular, $Senha, $Saldo, $Aniversario) {
        parent::__construct($Agencia, $Codigo, $DataDeCriacao, $Titular, $Senha, $Saldo);
        $this->Aniversario = $Aniversario;
    }
    
    function Retirar($Quantia) {
        if (($this->Saldo + $this->Aniversario) >= $Quantia){
            parent::Retirar($Quantia);
        } else {
            echo "Retirada não permitida... <br>";
            return false;
        }
        return true;
    }
    function Transferir($Conta, $Valor) {
        if ($this-> Retirar($Valor)) 
        {
            $Conta->Depositar($Valor);
        }
    }
    
}

