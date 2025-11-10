

import ipaddress
#Create an IPv4 network and show details
net = ipaddress.ip_network("192.168.1.0/24", strict=False)
print("Network:", net)
print("Network address:", net.network_address)
print("Broadcast address:", net.broadcast_address)
print("Netmask:", net.netmask)
print("Number of addresses:", net.num_addresses)
