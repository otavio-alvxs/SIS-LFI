function adicionarLinha() {
    var tabela = document.getElementById("tabelaContas").getElementsByTagName('tbody')[0];
    var novaLinha = tabela.insertRow();

    var cliente = document.getElementById("cliente").value;
    var valor = document.getElementById("valor").value;
    var pagamento = document.getElementById("pagamento").value;
    var datavencimento = document.getElementById("datavencimento").value;
    var datacontracao = document.getElementById("datacontracao").value;

    var celula1 = novaLinha.insertCell(0);
    var celula2 = novaLinha.insertCell(1);
    var celula3 = novaLinha.insertCell(2);
    var celula4 = novaLinha.insertCell(3);
    var celula5 = novaLinha.insertCell(4);
    var celula6 = novaLinha.insertCell(5);

    celula1.innerHTML = cliente;
    celula2.innerHTML = valor;
    celula3.innerHTML = pagamento;
    celula4.innerHTML = datavencimento;
    celula5.innerHTML = datacontracao;
    celula6.innerHTML = '<button class="excluir" type="button" onclick="excluirLinha(this)">Excluir</button>';

    document.getElementById("formcontas").reset();

    salvarDados();
}

function excluirLinha(botao) {
    var linha = botao.parentNode.parentNode;
    linha.parentNode.removeChild(linha);

    salvarDados();
}

function salvarDados() {
    var dadosTabela = [];
    var linhasTabela = document.getElementById("tabelaContas").rows;

    for (var i = 1; i < linhasTabela.length; i++) {
        var dadosLinha = {
            cliente: linhasTabela[i].cells[0].innerHTML,
            valor: linhasTabela[i].cells[1].innerHTML,
            pagamento: linhasTabela[i].cells[2].innerHTML,
            datavencimento: linhasTabela[i].cells[3].innerHTML,
            datacontracao: linhasTabela[i].cells[4].innerHTML,
        };
        dadosTabela.push(dadosLinha);
    }

    localStorage.setItem("dadosContas", JSON.stringify(dadosTabela));
}

function carregarDados() {
    var dadosSalvos = localStorage.getItem("dadosContas");

    if (dadosSalvos) {
        var dadosParseados = JSON.parse(dadosSalvos);

        for (var i = 0; i < dadosParseados.length; i++) {
            var novaLinha = document.getElementById("tabelaContas").getElementsByTagName('tbody')[0].insertRow();
            novaLinha.insertCell(0).innerHTML = dadosParseados[i].cliente;
            novaLinha.insertCell(1).innerHTML = dadosParseados[i].valor;
            novaLinha.insertCell(2).innerHTML = dadosParseados[i].pagamento;
            novaLinha.insertCell(3).innerHTML = dadosParseados[i].datavencimento;
            novaLinha.insertCell(4).innerHTML = dadosParseados[i].datacontracao;
            novaLinha.insertCell(5).innerHTML = '<button class="excluir" type="button" onclick="excluirLinha(this)">Excluir</button>';
        }
    }
}

window.onload = carregarDados;