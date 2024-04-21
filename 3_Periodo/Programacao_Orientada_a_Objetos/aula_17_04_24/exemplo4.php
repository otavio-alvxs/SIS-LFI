<?php
$xml = simplexml_load_file('paises2.xml');

echo 'Nome: ' . $xml->nome . '<br>';
echo 'Idioma: ' . $xml->idioma . '<br>';
echo '<br>';
echo "*** Informações Geográficas ***";
echo '<br>';
echo 'Clima: ' . $xml->geografia->clima . '<br>';
echo 'Costa: ' . $xml->geografia->costa . '<br>';
echo 'Pico: ' . $xml->geografia->pico . '<br>';
