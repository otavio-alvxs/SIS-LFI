function calcular() {
    var coca = 3.50;
    var coxinha = 4.00;
    var paoqueijo = 3.00;
    var entrega = 0;
    var desconto = 0;
    var total = 0;

    var produto = document.getElementById("produto");
    var produto = produto.options[produto.selectedIndex].text;
    var quantidade = document.getElementById("qtd").value;
    var pag = document.getElementById("din").checked;
    var entrega = document.getElementById("entrega").checked;
    
    if (produto == "Coca-Cola Lata") {
        total = (quantidade * coca)
    }   else if (produto == "Coxinha") {
        total = (quantidade * coxinha)
    }   else if (produto == "Pão de queijo") {
        total = (quantidade * paoqueijo)
    }

    if (entrega == true) {
        total = total + 6
    }
    if (pag == true) {
        desconto = (total * 0.10)
    }

    total = (total - desconto);

    document.getElementById("resp").innerHTML = "O valor total da compra foi de R$" + total.toFixed(2);
}
