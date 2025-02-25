const usuarioController = require("./usuarioController")

module.exports = (app) => {
        app.post("/usuario", usuarioController.post);
        app.put("/usuario/:id", usuarioController.put);
        app.delete("/usuario/:id", usuarioController.delete);
        app.get("/usuario", usuarioController.get);
        app.get("/usuario/:id", usuarioController.getById);
}