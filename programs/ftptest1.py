from ftplib import FTP
HOST = "test.rebex.net"
USER = "demo"
PASS = "password"
OUTPUT_FILE = "ftp_filenames.txt"   # output file to store filenames
with FTP(HOST, timeout=15) as ftp:
    # 1. Login
    ftp.login(USER, PASS)
    print("PWD before cwd():", ftp.pwd())
    # 2. Change to the required remote directory
    ftp.cwd("/pub/example")
    print("PWD after cwd():", ftp.pwd())
    # 3. Get list of filenames in the current directory
    filenames = ftp.nlst()      # nlst() returns a simple list of names  # ls
    print("Files in", "/pub/example")
    for name in filenames:
        print(name)
    # 4. Write filenames to an output file (one per line)
    with open("ftp_filenames1.txt" , "w") as out:
        for name in filenames:
            out.write(name + "\n")
    print("\nWroting  filenames to the file")
