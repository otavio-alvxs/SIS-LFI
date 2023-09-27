function calcular() {
    var gasolina = document.getElementById('gasolina').value;
    var etanol = documet.getElementById('etanol').value;

    if (etanol < (gasolina * 0.7)) {
        resp.innerHTML = 'É mais viável abastecer com etanol.';
    }
    else {
        resp.innerHTML = 'É mais viável abastecer com gasolina.';
    }

    }