const modalCadastro = new bootstrap.Modal(document.getElementById('modalCadastro'));

function alterar(id){
    
}

function excluir(idusuario){
    fetch("http://127.0.0.1:3333/usuario/" + idusuario,
        {
            method: "DELETE"
        }
    ).then(function () {
        //recarrega a lista
        listar();
        //esconde o modal
        modalCadastro.hide();
    });
}

function salvar() {
    let vnome = document.getElementById("nome").value;
    let vtelefone = document.getElementById("telefone").value;
    let vemail = document.getElementById("email").value;

    let usuario = {
        nome: vnome, telefone: vtelefone, vemail:email
    }
    
    fetch("http://127.0.0.1:3333/usuario",
        {
            method: "POST",
            body: JSON.stringify(usuario)
        }
    ).then(function () {
        //recarrega a lista
        listar();
        //esconde o modal
        modalCadastro.hide();
    })

}

function novo() {
    document.getElementById("nome").value = "";
    document.getElementById("telefone").value = "";
    document.getElementById("nome").value = "";
    modalCadastro.show()
}

function listar(){
    const lista = document.getElementById("lista");
    lista.innerHTML = "<tr><td colspan='5'>Carregando...</td></tr>";
    
    fetch("http://127.0.0.1:3333/usuario").then(resp => resp.json()).then(dados => mostrar(dados));
}
function mostrar(dados){
    const lista = document.getElementById("lista");
    lista.innerHTML = "";
    for (let i in dados){
        lista.innerHTML += "<tr>"
                        + "<td>" + dados[i].idusuario + "</td>"
                        + "<td>" + dados[i].nome + "</td>"
                        + "<td>" + dados[i].telefone + "</td>"
                        + "<td>" + dados[i].email + "</td>"
                        + "<td>"
                        + "<button type='button' class='btn btn-primary' onclick='alterar("+dados[i].idusuario+")'>A</button>"
                        + "<button type='button' class='btn btn-danger' onclick='excluir("+dados[i].idusuario+")'>X</button>"
                        "</td>" + "<tr>";
    }
}