import json
import socket

#Reading From JSON File and Converting to Dictionary------------------------------------------------------------------
database=open("DNS_Database.json", "r+")
dns_data=database.read()
database.close()
dns_dict = json.loads(dns_data)
DNS_Data = dns_dict["root"]

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
ip = socket.gethostbyname(socket.gethostname())
s.bind((ip,13345))

#Listening To The Port and Responding----------------------------------------------------------------------------------
while True:
    data,addr = s.recvfrom(512)
    print("["+str(addr)+"]"+str(data.decode("utf-8")))
    data = data.decode("utf-8")
    print(data)
    try:
        msg = search(data,DNS_Data)
        msg = msg[0]+"  "+msg[1]
    except:
        msg = "Error!!!"
    s.sendto(msg.encode("utf-8"),addr)