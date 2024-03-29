import socket
import threading

HEADER = 512
PORT = 8080
#SERVER = "127.0.0.1"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

#AF_INET should change to file
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION]{addr} connected." )
    connected =True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = (msg_length.split("Content-Length:"))[1]
        msg_length = msg_length.strip()
        msg_length = int(msg_length)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("[MESSAGE RECEIVED]")
    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count()-1}")

print("[STARTING SERVER]")
start()

