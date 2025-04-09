async function connect() {
    if (global.connection && global.connection.state != 'disconnect'){
        return global.connection;
    }
    const mysql = require("mysql2/promise");
    const connection = await mysql.createConnection(
        {
            host: '127.0.0.1', user: 'root', password: 'root', database: 'mysql'
        }
    );
    global.connection = connection;
    return connection;
}

exports.post = async (req, res, next) => {
    const conn = await connect();
    const sql = "INSERT INTO cidades " + "(nomeAnimal, reino, especie, classificacao, biomas) " + "VALUES (?,?,?,?,?)";
    const values = [req.body.nomeCidade, req.body.uf, req.body.populacao, req.body.anoFundacao, req.body.area];
    await conn.query(sql, values);
    res.status(201).send("ok");
}
exports.put = async (req, res, next) => {
    let id = req.params.id;
    const conn = await connect();
    const sql = "UPDATE animais " + "SET nomeAnimal = ?, reino = ?, especie = ?, classificacao = ?, biomas = ? " + "WHERE idAnimal = ?" ;
    const values = [req.body.nomeAnimal, req.body.reino, req.body.especie, req.body.classificacao, req.body.biomas, id];
    await conn.query(sql, values);
    res.status(201).send("ok");
}
exports.delete = async (req, res, next) => {
    let id = req.params.id;
    const conn = await connect();
    const sql = "DELETE FROM animais WHERE idAnimal = ? ";
    const values = [id];
    await conn.query(sql, values);
    res.status(200).send("ok");
}
exports.get = async (req, res, next) => {
    const conn = await connect();
    const [row] = await conn.query("select * from animais");
    res.status(200).send(row);
}
exports.getById = async (req, res, next) => {
    let id = req.params.id;
    const conn = await connect();
    const sql = ("SELECT * FROM animais WHERE idAnimal = ?");
    const values = [id];
    let [row] = await conn.query(sql, values); 
    if(row.length == 0){
        res.status(404).send("ERROR 404 NOT FOUND");
    } else{     
        res.status(200).send(row[0]);
    }
}