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