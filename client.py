import socket

HEADER = 64
PORT = 8080
#SERVER = "127.0.0.1"
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP,PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
#DNS_IP = "127.0.0.1"
DNS_IP = socket.gethostbyname(socket.gethostname())
DNS_PORT = 5353

msg = "GET / HTTP/1.1"+"\n\r"
msg += "Host: "+IP+":"+str(PORT)+"\n\r" 
msg += "Accept: text/html "+"\n\r"
msg += "Accept-Language: en-US,en;q=0.5 "+"\n\r"
msg += "Accept-Encoding: gzip, deflate "+"\n\r"
msg += "Connection: keep-alive"+"\n\r"
msg += "Content-Length: "

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client.connect(ADDR)
except:
	print("Couldn't connect to the server!")

def DNS(name):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(name.encode("utf-8"),(DNS_IP,DNS_PORT))
	data, addr = s.recvfrom(512)
	print("[SERVER MESSAGE]", data.decode())
	data = data.split("%!@")
	try:
		data = (data(0),int(data(1)))
	except:
		print("Not Valid Address From DNS!")
	s.close()
	return data


def HTTP(name,file_add):
	address = DNS(name)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect(address)
	except:
		print("Couldn't connect to the server!")
	message = file_add.encode(FORMAT)
	msg_length = len(message)
	message = msg+str(msg_length)+"\n\r"
	send_length = str(message).encode(FORMAT)
	client.send(message)
	client.send(file_add.encode())

while True:
	command = input("[ENTER COMMAND]  ")
	if (command.split(" "))[0] == "dns":
		DNS((command.split(" "))[1])
	elif (command.split(" "))[0] == "http":
		command = (command.split(" "))[1]
		HTTP((command.split("?"))[0],(command.split("?"))[1])
	elif command == "exit":
		break
	
