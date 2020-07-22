const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/tcc";

app.use(bodyParser.urlencoded({extended:true}))
app.use(express.static(__dirname+ '/views'));
app.use(express.static(__dirname+ '/public'))
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


app.get('/', function(req, res, next){

    //res.render('teste2', {mensagem3: "'Teste de mensagem 3.'"}); 
    res.sendFile(path.join(__dirname+ '/views/index.html'))
});

app.get('/get-data', function(req, res, next){
    var resultadoArray = [];
    mongo.connect(url, function(err, db){
        var ponteiro = db.collection('Animal').find();
        ponteiro.forEach(function(doc, err){
            resultadoArray.push(doc);
        }, function(){
            db.close();
            res.render('animal', {nome: resultadoArray.nomeAnimal});
        });
    });
});

app.post('/cadastrar_adotante', function(req, res, next){
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
            var dbo = db.db("TCC");
            var myobj = 
            {   
                nome: req.body.nomeAdotante, 
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

            var sucess = null;
            var message = null;
            var id = null;
            var error = null;

            dbo.collection("Adotante").countDocuments({CPF: req.body.cpfAdotante}, function (err, countDocuments){
                if(countDocuments>0){
                    sucess = false;
                    message = "Cadastro não realizado!";
                    id = null;
                    error = "CPF já cadastrado.";

                    res.render('dbMessage', {sucess: sucess, message: message, error: error, id: id})

                    console.log("CPF já cadastrado!");
                }else
                {
                    dbo.collection("Adotante").insertOne(myobj, function(err, insertOne) {
                        if (err) throw err;
                        sucess = true;
                        message = "Cadastro realizado!";
                        id = myobj.CPF;
                        error = null;

                        console.log("Um novo adotante foi cadastrado!");
                        res.render('dbMessage', {sucess: sucess, message: message, error: error, id: id})
                        db.close();
                    });
                }
            });
    });
});

app.post('/cadastrar_animal', function(req, res, next){
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
            var dbo = db.db("TCC");
            var myobj = 
            {   
                nome: req.body.nomeAnimal, 
                voluntario: req.body.voluntarioAnimal,
                chip: req.body.chipAnimal,
                raça: req.body.racaAnimal,
                cor: req.body.corAnimal,
                nascimento: req.body.nascimentoAnimal,
                tipo: req.body.tipoAnimal,
                sexo: req.body.sexoAnimal,
                castrado: req.body.castradoAnimal,
                vermifugo: req.body.vermifugoAnimal,
                numero: req.body.numeroAnimal,
                adotado: false
            }

            var sucess = null;
            var message = null;
            var id = null;
            var error = null;

            if(myobj.chip != ""){
                dbo.collection("Animal").countDocuments({chip: req.body.chipAnimal}, function (err, countDocuments){
                    if(countDocuments>0){
    
                        sucess = false;
                        message = "Cadastro não realizado!";
                        id = null;
                        error = "Chip já cadastrado.";
    
                        res.render('dbMessage', {sucess: sucess, message: message, error: error, id: id})
    
                        console.log("Chip já cadastrado!");
                    }
                    else
                    {
                        sucess = true;
                        message = "Cadastro realizado!";
                        id = myobj.numero;
                        error = null;

                        dbo.collection("Animal").insertOne(myobj, function(err, insertOne) {
                            if (err) throw err;
                            console.log("Um novo animal foi cadastrado!");
                            res.render('dbMessage', {sucess: sucess, message: message, error: error, id: id})
                        });
                    }
                });
            }
            else 
            {
                sucess = true;
                message = "Cadastro realizado!";
                id = myobj.numero;
                error = null;

                dbo.collection("Animal").insertOne(myobj, function(err, insertOne) {
                if (err) throw err;
                console.log("Um novo animal foi cadastrado!");
                res.render('dbMessage', {sucess: sucess, message: message, error: error, id: id})
                db.close();
            });
        }
    });
});

app.post('/cadastrar_adocao', function(req, res, next){
    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
            var dbo = db.db("TCC");
            var myobj = 
            {   
                id: req.body.idAnimalAdocao,
                cpf: req.body.cpdAdotanteAdocao,
                local: req.body.localAdocao,
                data: req.body.dataAdocao,
                entrevistado: req.body.entrevistador
            }
  
        dbo.collection("Adocao").countDocuments({id: req.body.idAnimalAdocao}, function (err, countDocuments){
            if(countDocuments>0){
                console.log("Adoção já realizada!");
            }else
            {
                dbo.collection("Adocao").insertOne(myobj, function(err, res) {
                    if (err) throw err;
                    console.log("Uma nova adoção foi cadastrada!");
                    db.close();
                });
            }
        });
    res.redirect('/');
});
})

//app.post('cadastrar_devolucao', function(req, res, next){

app.listen(8081);