import os
import netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
from getpass import getpass

USERNAME= input("Please enter your ssh Username: ")
PASS= getpass("Please enter your ssh Password: ")

device = {
    'ip': '192.168.108.1',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}


try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    f = open(f'backup_config','x')
    f.write(output)
    f.close
except (NetMikoTimeoutException):
    print ("This device has timed out: " + device['ip'])
except (AuthenticationException):
    print ("Authentication failure by: " + device['ip'])
except (SSHException):
    print("Could not establish connection via SSH. Check SSH configuration on: " + device['ip'])

print("This task has been completed...")
