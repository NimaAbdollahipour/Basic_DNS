import socket

HEADER = 64
PORT = 18080
SERVER = "127.0.0.1"
#SERVER = socket.gethostbyname('localhost')
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
DNS_IP = "127.0.0.1"
DNS_PORT = 15353

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def DNS(name):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(name.encode("utf-8"),(DNS_IP,DNS_PORT))
	data, addr = s.recvfrom(512)
	print("[SERVER MESSAGE]", data.decode())
	s.close()


def HTTP(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	client.send(send_length)
	client.send(message)

DNS()
HTTP("Hello")