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

if len(a) == 4 and int(a[0]) == 144 and int(a[1]) == 174 and int(a[2]) == 3 and int(a[3]) <= 212:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
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
        print "\This IP is not configured for SSH. Please retry\n"


                                      
