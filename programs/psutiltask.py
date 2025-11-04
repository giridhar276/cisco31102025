'''
write a script to display the below information 

1. CPU percentage
2. Memory info ( total memory, available, used)
3. process info
4. disk partitions
5. network statistics
4. platform details ( like OS name , model , python version)
5. boot time of your system
6. IP Address of your system
7. hostname of the system


'''
import psutil 
import platform
import socket
print(psutil.cpu_percent())
print(psutil.virtual_memory())
print(psutil.pids())
print(psutil.disk_partitions())
print(psutil.disk_usage("C:\\"))
print(platform.platform())
print(platform.architecture())
print(platform.node())
print(platform.system())
print(platform.python_version())

print(socket.gethostname())
hostname = socket.gethostname()
#ipaddress = socket.gethostbyaddr(hostname)
#print(ipaddress)
