#!/usr/bin/python3
from scapy.all import ARP, Ether, srp

#Scanner that neatly outputs all online devices
#don't forget to install scapy. For ubuntu: sudo apt install python3-scapy

target = "192.168.2.254/24"
arp = ARP(pdst=target)
#Creates ARP packet

ether = Ether(dst="ff:ff:ff:ff:ff:ff")
#Create ether broadcast packet

packet = ether/arp
result = srp(packet, timeout=3)[0]

clients = []
for send, recieved in result:
    #append IP and mac address to clients list per response
    clients.append({"ip": recieved.psrc, "mac": recieved.hwsrc})

print(f"Found {len(clients)} devices:")
print("IP" + " "*18+"MAC")


for client in clients:
    print(f"{client['ip']} : {client['mac']}")
