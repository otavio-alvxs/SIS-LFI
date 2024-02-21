function adicionarLinha() {
    var tabela = document.getElementById("tabelaVendas").getElementsByTagName('tbody')[0];
    var novaLinha = tabela.insertRow();

    var produto = document.getElementById("produto").value;
    var nicho = document.getElementById("nicho").value;
    var valorRevenda = document.getElementById("valorRevenda").value;
    var precoCusto = document.getElementById("precoCusto").value;
    var estoque = document.getElementById("estoque").value;

    var celula1 = novaLinha.insertCell(0);
    var celula2 = novaLinha.insertCell(1);
    var celula3 = novaLinha.insertCell(2);
    var celula4 = novaLinha.insertCell(3);
    var celula5 = novaLinha.insertCell(4);
    var celula6 = novaLinha.insertCell(5);

    celula1.innerHTML = produto;
    celula2.innerHTML = nicho;
    celula3.innerHTML = valorRevenda;
    celula4.innerHTML = precoCusto;
    celula5.innerHTML = estoque;
    celula6.innerHTML = '<button type="button" onclick="excluirLinha(this)">Excluir</button>';

    document.getElementById("formularioVendas").reset();

    salvarDados();
}

function excluirLinha(botao) {
    var linha = botao.parentNode.parentNode;
    linha.parentNode.removeChild(linha);

    salvarDados();
}

function salvarDados() {
    var dadosTabela = [];
    var linhasTabela = document.getElementById("tabelaVendas").rows;

    for (var i = 1; i < linhasTabela.length; i++) {
        var dadosLinha = {
            produto: linhasTabela[i].cells[0].innerHTML,
            nicho: linhasTabela[i].cells[1].innerHTML,
            valorRevenda: linhasTabela[i].cells[2].innerHTML,
            precoCusto: linhasTabela[i].cells[3].innerHTML,
            estoque: linhasTabela[i].cells[4].innerHTML,
        };
        dadosTabela.push(dadosLinha);
    }

    localStorage.setItem("dadosVendas", JSON.stringify(dadosTabela));
}

function carregarDados() {
    var dadosSalvos = localStorage.getItem("dadosVendas");

    if (dadosSalvos) {
        var dadosParseados = JSON.parse(dadosSalvos);

        for (var i = 0; i < dadosParseados.length; i++) {
            var novaLinha = document.getElementById("tabelaVendas").getElementsByTagName('tbody')[0].insertRow();
            novaLinha.insertCell(0).innerHTML = dadosParseados[i].produto;
            novaLinha.insertCell(1).innerHTML = dadosParseados[i].nicho;
            novaLinha.insertCell(2).innerHTML = dadosParseados[i].valorRevenda;
            novaLinha.insertCell(3).innerHTML = dadosParseados[i].precoCusto;
            novaLinha.insertCell(4).innerHTML = dadosParseados[i].estoque;
            novaLinha.insertCell(5).innerHTML = '<button type="button" onclick="excluirLinha(this)">Excluir</button>';
        }
    }
}

window.onload = carregarDados;