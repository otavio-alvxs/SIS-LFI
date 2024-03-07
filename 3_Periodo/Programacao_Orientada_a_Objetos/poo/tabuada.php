<?php

for ($i = 0; $i <=10; $i++) {
    for ($contador = 0; $contador <= 10; $contador++){
        while ($i == $contador) {
            echo "\n\nTabuada do $contador\n";
            break;
        }
    }
    for ($num = 0; $num <= 10; $num ++){
        $calc = $i * $num;
        echo "$i X $num = $calc\n";
    }
}
