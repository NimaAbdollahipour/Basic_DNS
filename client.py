import socket
def DNS():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msg = input("[ENTER WEBSITE NAME]: ")
	ip = socket.gethostbyname(socket.gethostname())
	s.sendto(msg.encode("utf-8"),(ip,13345))
	data, addr = s.recvfrom(512)
	print("[SERVER MESSAGE]", data.decode())
	s.close()

while True:
	DNS()