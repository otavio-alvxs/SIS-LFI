const animalController = require("./animalController")

module.exports = (app) => {
        app.post("/animal", animalController.post);
        app.put("/animal/:id", animalController.put);
        app.delete("/animal/:id", animalController.delete);
        app.get("/animal", animalController.get);
        app.get("/animal/:id", animalController.getById);
}