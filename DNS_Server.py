import json
import socket
import threading

#Reading From JSON File and Converting to Dictionary------------------------------------------------------------------
def read():
    database=open("DNS_Database.json", "r+")
    dns_data=database.read()
    database.close()
    dns_dict = json.loads(dns_data)
    DNS_Data = dns_dict["root"]
    return DNS_Data

#Searching For Main Domain--------------------------------------------------------------------------------------------
def search(name, DNS):
    splited = name.split(".")
    current = splited[-1]
    for i in range(len(splited)-1):
        DNS = DNS.get("domains","NoData")
        current = splited[-2-i] + "." + current
        DNS = DNS.get(current,"NoData")
        IP = DNS.get("ip", "NoData")
        PORT = DNS.get("port", "NoData")
    return IP,PORT

#Creating Socket-------------------------------------------------------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.gethostbyname('localhost')
port = 15353
s.bind((ip,port))


def respond(data,addr):
    print("["+str(addr)+"]"+str(data.decode("utf-8")))
    data = data.decode("utf-8")
    print(data)
    try:
        msg = search(data,read())
        msg = msg[0]+"  "+msg[1]
    except:
        msg = "Error!!!"
    s.sendto(msg.encode("utf-8"),addr)


#Listening To The Port and Responding----------------------------------------------------------------------------------
while True:
    data,addr = s.recvfrom(512)
    thread = threading.Thread(target=respond , args= (data ,addr))