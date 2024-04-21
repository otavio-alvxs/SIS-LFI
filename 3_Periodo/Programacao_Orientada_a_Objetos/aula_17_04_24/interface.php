<?php

interface IAluno
{
    function getNome();

    function setNome($Nome);
}

class Aluno implements IAluno
{
    private string $Nome;
    function setNome($Nome){
        $this->Nome = $Nome;
    }
    function getNome(){
        return $this->Nome;
    }
}

$joaninha = new Aluno();
$joaninha -> setNome('Joana Maranhao');
echo $joaninha -> getNome();
