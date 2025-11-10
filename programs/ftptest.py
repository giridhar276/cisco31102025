
from ftplib import FTP

host = "test.rebex.net"  #app1.cisco.com  # myapp2.ftp.cisco.com
user = "demo"
password = "password"

with FTP(host, timeout=15) as ftp:
    ftp.login(user, password)
    print("PWD:", ftp.pwd()) # pwd: present working directly # / means root directory
    ftp.cwd("/pub/example")
    with open("myftp.txt", "wb") as out:
        ftp.retrbinary("RETR readme.txt", out.write)
    print("Downloaded readme_ftp.txt")


# write a program to display all the filenames that are present in /pub/example remote directory 
# and write the filenames to the outputfile