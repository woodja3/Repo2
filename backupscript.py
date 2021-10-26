import os
from netmiko import ConnectHandler
from getpass import getpass

USERNAME= input("Please enter your ssh Username: ")
PASS= getpass("Please enter your ssh Password: ")

device = {
    'ip': '192.168.1.10',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_iso'
}

c = ConnectHandler(**device)

output - c.send_command('show run')

f=open('backup.conf', 'x')

f.write(output)
    
f.close()