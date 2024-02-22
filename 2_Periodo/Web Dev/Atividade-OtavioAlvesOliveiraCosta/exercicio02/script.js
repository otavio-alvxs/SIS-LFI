function calcular() {
    var nome = document.getElementById('nome').value;
    var idade = parseFloat(document.getElementById('idade').value);
    var resp = document.getElementById('resp')

    if (idade < 14) {
        resp.innerHTML = 'O atleta ' + nome + ' é considerado um atleta mirim.'
    } else if (idade >= 14 && idade <= 15) {
        resp.innerHTML = 'O atleta ' + nome + ' é considerado um atleta infantil.'
    } else if (idade >= 16 && idade <= 17) {
        resp.innerHTML = 'O atleta ' + nome + ' é considerado um atleta juvenil.'
    } else if (idade >= 18 && idade <= 20) {
        resp.innerHTML = 'O atleta ' + nome + ' é considerado um atleta junior.'
    } else if (idade > 20) {
        resp.innerHTML = 'O atleta ' + nome + ' é considerado um atleta profissional.'
    }

}