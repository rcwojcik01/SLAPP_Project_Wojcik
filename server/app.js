// npm imports
var express   = require('express');
var bodyParser = require('body-parser');
var http      = require('http');
var socketio  = require('socket.io');

//web server app
var app       = express();
var server    = http.createServer(app);
var io        = socketio(server);

// web server meta
var webroot   = __dirname + '/../client/';
var port      = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : false }));

// static hosting
app.use('/', express.static(webroot));

// run the server
server.listen(port, function() {
    console.log('hosting from ' + webroot);
    //console.log('ready to serve http://10.10.90.78:' + port + '/');
});

app.post('/', function(req, res) {
//   console.log('post / = ' + JSON.stringify(req.body));
    io.sockets.emit('valuesReceived', req.body);
    res.status(200).send('received');
});