import ipaddress
try:
    ip = ipaddress.ip_address("192.168.1.101")
    print(ip)
    print("Version:", ip.version)
    print("Is private:", ip.is_private)
except ValueError as err:
    print("Invalid IP address")
except Exception as err:
    print(err)


#Safely validate an IP address (valid / invalid)
user_input = "300.168.1.10"  # invalid

try:
    ip = ipaddress.ip_address(user_input)
    print("Valid IP:", ip)
except ValueError as e:
    print("Invalid IP address:", e)




#Create an IPv4 network and show details
net = ipaddress.ip_network("192.168.1.0/24", strict=False)
print("Network:", net)
print("Network address:", net.network_address)
print("Broadcast address:", net.broadcast_address)
print("Netmask:", net.netmask)
print("Number of addresses:", net.num_addresses)



#Iterate over all usable hosts in a network
net = ipaddress.ip_network("192.168.1.0/29")  # small network

print("Usable hosts:")
for host in net.hosts():
    print(host)


#Check if an IP address belongs to a network
net = ipaddress.ip_network("10.0.0.0/16")
ip1 = ipaddress.ip_address("10.0.5.20")
ip2 = ipaddress.ip_address("192.168.1.1")

print(ip1, "in", net, "?", ip1 in net)
print(ip2, "in", net, "?", ip2 in net)


#Simple IPv6 address usage
ipv6 = ipaddress.ip_address("2001:db8::1")
print(ipv6)
print("Version:", ipv6.version)
print("Is global:", ipv6.is_global)


#Split a network into smaller subnets
net = ipaddress.ip_network("192.168.0.0/24")

print("Splitting", net, "into /26 subnets:")
for subnet in net.subnets(new_prefix=26):
    print(subnet)