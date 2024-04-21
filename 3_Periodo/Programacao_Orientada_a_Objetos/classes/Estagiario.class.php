<?php

class Estagiario extends Funcionario {
    
    /* 
    metodo getSalario sobreescrito
    retorna o $Salario com 12% de bonus
    */

    function GetSalario() {
        return $this->Salario*1.12;
    }
}
