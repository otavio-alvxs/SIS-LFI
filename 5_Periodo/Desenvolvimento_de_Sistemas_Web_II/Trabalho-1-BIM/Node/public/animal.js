const modalCadastro = new bootstrap.Modal(document.getElementById('modalCadastro'));

function novo() {
    idAnimalAtual = 0;                                                                                                                                                         
    document.getElementById("nomeAnimal").value = "";
    document.getElementById("reino").value = "";
    document.getElementById("especie").value = "";
    document.getElementById("classificacao").value = "";
    document.getElementById("biomas").value = "";
    modalCadastro.show()
}

function salvar(){
    let nomeAnimal = document.getElementById("nomeAnimal").value;
    let reino = document.getElementById("reino").value;
    let especie = document.getElementById("especie").value;
    let classificacao = document.getElementById("classificacao").value;
    let biomas = document.getElementById("biomas").value;
    let animal = {
        nomeAnimal: nomeAnimal, reino: reino, especie: especie, classificacao: classificacao, biomas: biomas
    }
    let url;
    let metodo;
    if (idAnimalAtual > 0){
        url = "http://127.0.0.1:3333/animal/"+idAnimalAtual;
        metodo = "PUT";
    } else { 
        url = "http://127.0.0.1:3333/animal";
        metodo = "POST";
    }
    fetch(url, {method: metodo, body: JSON.stringify(animal), headers: {"Content-Type" : "application/json"}}).then(function (){ listar(); modalCadastro.hide()})
}

function listar(){
    const lista = document.getElementById("lista");
    lista.innerHTML = "<tr><td colspan='5'>Carregando...</td></tr>";
    
    fetch("http://127.0.0.1:3333/animal").then(resp => resp.json()).then(dados => mostrar(dados));
}
function mostrar(dados){
    const lista = document.getElementById("lista");
    lista.innerHTML = "";
    for (let i in dados){
        lista.innerHTML += "<tr>" 
        + "<td>" + dados[i].idAnimal +"</td>" 
        + "<td>" + dados[i].nomeAnimal +"</td>" 
        + "<td>" + dados[i].reino +"</td>" 
        + "<td>" + dados[i].especie +"</td>" 
        + "<td>" + dados[i].classificacao +"</td>"
        + "<td>" + dados[i].biomas +"</td>" 
        + "<td>"
        + "<button type='button' class='btn btn-primary' onclick='alterar("+dados[i].idAnimal+")'>Alterar</button>" 
        + "<button type='button' class='btn btn-danger' onclick='excluir("+dados[i].idAnimal+")'>Excluir</button>"
        + "</td>" 
        + "</tr>";
    }
}

var idAnimalAtual;

function alterar(idAnimal){
    idAnimalAtual = idAnimal;
    fetch("http://127.0.0.1:3333/cidade/"+idAnimal).then(resp => resp.json()).then(dados =>{
        document.getElementById("nomeAnimal").value = dados.nomeAnimal;
        document.getElementById("reino").value = dados.reino;
        document.getElementById("especie").value = dados.especie;
        document.getElementById("classificacao").value = dados.classificacao;
        document.getElementById("biomas").value = dados.area;
        modalCadastro.show()
    });
}

function excluir(idAnimal){
    fetch("http://127.0.0.1:3333/animal/"+idAnimal, {method: "DELETE"}).then(function (){listar();});

}