/**
 *Server side for elegantr software
 *User: mencent
 *Date: 2014-7-4
 */

var net = require('net');
var http = require('http');
var clients = [];

var server = net.createServer(function(socket){
	//when connect
	socket.setEncoding('utf-8');
	clients.push(socket);
	
	/*timeout event
	socket.setTimeout(200000, function(){
		socket.end();
	});
	*/

	//accept data event
	socket.on('data', function(data){
		try{
			data = JSON.parse(data);
			runCommand(socket, data);
		}catch(err){
			socket.write(data + "\n" + err);
		}
	});

	//end
	socket.on('end', function(){
		console.log('end');
	});

	//client close conncet event
	socket.on('close', function(data){
		var idx = clients.indexOf(socket);
		delete clients[idx];
		console.log('closed');
	});

	//error event
	socket.on('error', function(exception){
		console.log('socket error: ' + exception);
		socket.end();
	});

});

server.on('listening', function(){
	console.log('server listening: ' + server.address().port);
});

server.on('connection', function(socket){
	console.log('connect: ' + socket.remoteAddress + ':' + socket.remotePort);
});

//server error event
server.on('error', function(exception){
	console.log('server error: ' + exception);
});

server.listen(7000);

function runCommand(socket, data){
	switch(data.cmd){
		case "LOGIN":
			socket.write("Login command");
			break;
		case "DETAIL":
			socket.write("Detail command");
			break;
		default:
			socket.write("No command");
	}
}

function doiDetails(doi){
	BASE_URL = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?'

}