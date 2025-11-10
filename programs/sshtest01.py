import paramiko
HOST = "test.rebex.net"   
USER = "demo"             
PASS = "password"       
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=HOST,port=22,username=USER,password=PASS )
    print("Connected successfully")
    # Run the "date" command on remote machine
    stdin, stdout, stderr = client.exec_command("ls")
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()
    if output:
        print("current working directory:", output)
    if error:
        print("Error:", error)
except Exception as e:
    print("Connection or command failed")
    print("Reason:", e)
finally:
    client.close()
