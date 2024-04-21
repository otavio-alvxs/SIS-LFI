<?php
$xml = simplexml_load_file('paises.xml');

//exibe as informações do objeto criado
echo 'Nome: ' . $xml->nome .  '<br>';
echo 'Idioma: ' . $xml->idioma .  '<br>';
echo 'Moeda: ' . $xml->moeda .  '<br>';
echo 'População: ' . $xml->populacao .  '<br>';
