function listar() {
    const lista = document.getElementById("lista");
    lista.innerHTML = "<tr><td colspan='5'>Carregando...</td></tr>";

    fetch("http://127.0.0.1:3333/usuario").then(resp => resp.json()).then(dados => mostrar(dados));
}

function mostrar(dados) {
    const lista = document.getElementById("lista");
    lista.innerHTML = "";
    for (let i in dados) {
        lista.innerHTML += "<tr>"
                        + "<td>" + dados[i].idusuario + "</td>"
                        + "<td>" + dados[i].nome + "</td>"
                        + "<td>" + dados[i].telefone + "</td>"
                        + "<td>" + dados[i].email + "</td>"
                        + "<td></td>"
                        + "</tr>";
    }
}
