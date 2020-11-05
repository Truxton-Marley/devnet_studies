from netmiko import ConnectHandler

# TODO: See below:
# https://pynet.twb-tech.com/blog/automation/netmiko.html

iosv_l2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.12.201",
    "username": "generic",
    "password": "generic",
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command("show ip int brief")
print(output, "\n\n")
print(type(output), "\n\n")


show_commands = ["terminal length 0", "show run"]
output = ""
for command in show_commands:
    output += net_connect.send_command(command)
print(output)

# config_commands = ["int loop8", "ip address 1.1.1.1 255.255.255.255"]
# output = net_connect.send_config_set(config_commands)
# print(output)

