
from ftplib import FTP

HOST = "test.rebex.net"
USER = "demo"
PASS = "password"

with FTP(HOST, timeout=15) as ftp:
    ftp.login(USER, PASS)
    print("PWD:", ftp.pwd())
    ftp.cwd("/pub/example")
    with open("readme_ftp.txt", "wb") as out:
        ftp.retrbinary("RETR readme.txt", out.write)
    print("Downloaded readme_ftp.txt")