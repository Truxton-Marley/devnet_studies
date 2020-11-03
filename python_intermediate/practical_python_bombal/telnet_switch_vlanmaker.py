import getpass
import telnetlib

switches = []
user = input("Enter your remote account: ")
password = getpass.getpass()

with open("switches.txt") as file:
    for IP in file:
        switches.append(IP.strip())

count = 0
for switch in switches:

    count += 1
    #use "debug telnet" to watch along
    print("Switch {count} Configuring switch at IP: {switch}.".format(count=count, switch=switch))
    tn = telnetlib.Telnet(switch)

    print("about to grab username")
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    for n in range(2,11):
        vlan = "vlan " + str(n)
        tn.write(vlan.encode("ascii") + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    

    print(tn.read_all().decode('ascii'))
