/**
 *Server side for elegantr software
 *User: mencent
 *Date: 2014-7-4
 */

var net = require('net')
var port = 7000

var server = net.createServer(function(socket){
	console.log('connect: ' + socket.remoteAddress + ':' + socket.remotePort);
	socket.setEncoding('binary');

	//timeout event
	socket.setTimeout(200000, function(){
		console.log('Timeout');
		socket.end();
	});

	//when connect
	socket.on('connect', function(socket){
		socket.write
	});

	//accept data event
	socket.on('data', function(data){
		console.log('recv: ' + data);
	});

	//error event
	socket.on('error', function(exception){
		console.log('socket error: ' + exception);
		socket.end();
	});

	//client close conncet event
	socket.on('close', function(data){
		console.log('close: ' + socket.remoteAddress + ":" + socket.remotePort);
	});

});

server.listen(port);

//sever listen event
server.on('listening', function(){
	console.log('server listening: ' + server.address().port);
});

//server error event
server.on('error', function(exception){
	console.log('server error: ' + exception)
});