const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/tcc";

app.use(bodyParser.urlencoded({extended:true}))
app.use(express.static(__dirname+ '/views'));
app.use(express.static(__dirname+ '/public'))


app.get('/', function(req, res, next){
    res.sendFile(path.join(__dirname+ '/views/index.html'))
});

app.post('/cadastrar_adotante', function(req, res, next){
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
            var dbo = db.db("TCC");
            var myobj = 
            {   nome: req.body.nomeAdotante, 
                sobrenome: req.body.sobrenomeAdotante, 
                          RG: req.body.rgAdotante,
                          CPF: req.body.cpfAdotante,
                          nascimento: req.body.nascimentoAdotante,
                          CEP: req.body.cepAdotante,
                          rua: req.body.ruaAdotante,
                          numero: req.body.numeroAdotante,
                          complemento: req.body.complementoAdotante,
                          bairro: req.body.bairroAdotante,
                          cidade: req.body.cidadeAdotante,
                          telefone: req.body.telefoneAdotante,
                          email: req.body.emailAdotante,
            }

        dbo.collection("Adotantes").insertOne(myobj, function(err, res) {
        if (err) throw err;
        console.log("Um novo adotante inserido");
        db.close();
    });
    res.redirect('/');
});
});

app.post('/cadastrar_animal', function(req, res, next){
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
            var dbo = db.db("TCC");
            var myobj = 
            {   nome: req.body.nomeAnimal, 
                voluntario: req.body.voluntarioAnimal,
                chip: req.body.chipAnimal,
                raça: req.body.racaAnimal,
                cor: req.body.corAnimal,
                nascimento: req.body.nascimentoAnimal,
                tipo: req.body.tipoAnimal,
                sexo: req.body.sexoAnimal,
                castrado: req.body.castradoAnimal,
                vermifugo: req.body.vermifugoAnimal
            }

        dbo.collection("Animais").insertOne(myobj, function(err, res) {
        if (err) throw err;
        console.log("Um novo animal inserido");
        db.close();
    });
    res.redirect('/');
});
});

app.listen(8081);