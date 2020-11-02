import getpass
import telnetlib

HOST = "192.168.8.200"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

print("about to grab username")
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"show ip int brief\n")
tn.write(b"show cdp neighbors\n")
tn.write(b"conf t\n")
print("Creating loopback 8")
tn.write(b'int loop 8\n')
tn.write(b'ip address 10.8.8.8 255.255.255.255\n')
tn.write(b'end\n')
tn.write(b'show ip int br\n')
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
