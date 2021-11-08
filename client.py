import socket

HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"
#SERVER = socket.gethostbyname(socket.gethostname)
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def DNS():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msg = input("[ENTER WEBSITE NAME]: ")
	ip = socket.gethostbyname(socket.gethostname())
	s.sendto(msg.encode("utf-8"),(ip,13345))
	data, addr = s.recvfrom(512)
	print("[SERVER MESSAGE]", data.decode())
	s.close()


def HTTP(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	client.send(send_length)
	client.send(message)


HTTP("Hello")