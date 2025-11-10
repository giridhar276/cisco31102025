
# pip install paramiko
import paramiko
HOST = "test.rebex.net"
USER = "demo"
PASS = "password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # try to connect
    client.connect(hostname=HOST,port=22,username=USER,password=PASS,timeout=10)
    print("Connection successful")
except Exception as e:
    print("Connection failed")
    print("Reason:", e)
finally:
    client.close()
