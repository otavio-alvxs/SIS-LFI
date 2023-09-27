function calcular() {
    var gasolina = parseFloat(document.getElementById('gasolina').value);
    var etanol = parseFloat(documet.getElementById('etanol').value);
    var resp = document.getElementById('resp');

    if (etanol < (gasolina * 0.7)) {
        resp.innerHTML = 'É mais viável abastecer com etanol.';
    } else {
        resp.innerHTML = 'É mais viável abastecer com gasolina.';
    }
}
