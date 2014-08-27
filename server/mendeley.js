/*
Get access token from mendeley and refresh access token timely.
According to the access token and the doi of article, get the
article details from the mendeley server.
*/

var events = require('events');
var config = require('./config');
var request = require('request');

var ACCESS_TOKEN = null;
var options = {
	headers: {
		'Authorization': 'Basic ' + new Buffer(config.clientID + ':' + config.clientSecret).toString('base64'),
		'Content-type': 'application/json'
	},
	url: config.tokenUrl,
	form: {grant_type: 'client_credentials'},
	json: true
};

//egister accessing token event
var emitter = new events.EventEmitter()
emitter.on('token', getMendeleyAccessToken);
emitter.emit('token');

//every 3000 seconds refresh the access token
setInterval(function(){
	emitter.emit('token');
}, 1000 * 3000);

//get the mendeley access token
function getMendeleyAccessToken() {
	request.post(options, function(error, response, data){
		if (!error && response.statusCode == 200) {
			ACCESS_TOKEN = data.access_token
			console.log(ACCESS_TOKEN);
		} else {
			console.log(error);
			emitter.emit('token');
		}
	});
}

//get article details from mendeley by doi, pubmed id or arix
exports.getDetailsFromMenendely = function (data, socket){
	data.access_token = ACCESS_TOKEN
	options = {
		url: 'https://api.mendeley.com/catalog',
		qs: data,
		//json: true
	};
	request(options, function(error, response, data){
		if (!error && response.statusCode == 200) {
			socket.write(data);
			console.log(data);
		} else {
			//socket.write(error);
			console.log(error);
		}
	});
}