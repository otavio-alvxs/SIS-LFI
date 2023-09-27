function verificarTriangulo() {
    var lado1 = parseFloat(document.getElementById('lado1').value);
    var lado2 = parseFloat(document.getElementById('lado2').value);
    var lado3 = parseFloat(document.getElementById('lado3').value);
    var resultado = document.getElementById('resultado');

    if (lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1) {
        if (lado1 === lado2 && lado2 === lado3) {
            resultado.innerHTML = 'É um Triângulo Equilátero.';
        } else if (lado1 === lado2 || lado1 === lado3 || lado2 === lado3) {
            resultado.innerHTML = 'É um Triângulo Isósceles.';
        } else {
            resultado.innerHTML = 'É um Triângulo Escaleno.';
        }
    } else {
        resultado.innerHTML = 'Não é possível formar um triângulo com esses valores.';
    }
}