# sc-vlan-config
short vlan config


import paramiko
import time
import random
import sys
import getpass

ip_address = raw_input("Enter IP Address:\n")
username = raw_input("Enter username:\n")
password = getpass.getpass("Enter Password:\n")
interface = raw_input("Enter the interface you want configured:\n")
vlan = raw_input("Enter the vlan to be changed to:\n")


a = ip_address.split('.')

if len(a) == 4 and int(a[0]) == xxx and int(a[1]) == xxx and int(a[2]) == x and int(a[3]) <= xxx: # sub x for your IP
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password,look_for_keys=False,allow_agent=False)
        print "Successful connection", ip_address
        remote_connection = ssh_client.invoke_shell()
        remote_connection.send("configure terminal\n")
        remote_connection.send("int " +interface+ "\n")
        remote_connection.send("switchport access vlan " +vlan+"\n")
        remote_connection.send("end\n")
        time.sleep(1)
        output = remote_connection.recv(65535)
        print output
        ssh_client.close


else:
        print "\This IP is not configured to receive SSH connections. Please retry\n"

a
                                      
