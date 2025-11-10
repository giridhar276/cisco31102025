
# pip install paramiko
import paramiko
HOST, USER, PASS = "test.rebex.net", "demo", "password"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, 22, USER, PASS)

# SFTP: list and download
sftp = client.open_sftp()
print("Root:", sftp.listdir("."))
print("/pub/example:", sftp.listdir("/pub/example"))
#sftp.get(source,destination)
# source is the remote path  # desination is the local file or path
sftp.get("/pub/example/readme.txt", "readmefile.txt")
sftp.close()
client.close()
print("Downloaded readmefile.txt")