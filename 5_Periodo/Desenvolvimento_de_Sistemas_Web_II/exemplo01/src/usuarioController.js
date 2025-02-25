exports.post = (req, res, next) => {
    res.status(201).send("rota post");
}
exports.put = (req, res, next) => {
    let id = req.params.id;
    res.status(201).send("rota put " + id);
}
exports.delete = (req, res, next) => {
    let id = req.params.id;
    res.status(200).send("rota delete " + id);
}
exports.get = (req, res, next) => {
    res.status(200).send("rota get");
}
exports.getById = (req, res, next) => {
    let id = req.params.id;
    res.status(200).send("rota getById " + id);
}