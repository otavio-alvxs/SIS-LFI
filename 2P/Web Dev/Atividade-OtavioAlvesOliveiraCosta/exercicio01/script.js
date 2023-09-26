function calcular() {
    var gasolina = document.getElementById('gasolina').value
    var etanol = documet.getElementById('etanol').value

    if (etanol < (gasolina * 0.7)){
        document.getElementById('resp').innerHTML = 'Compensa mais abastecer no etanol.'
    }

    }