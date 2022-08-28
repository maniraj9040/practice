import wmi


ip = "10.1.240.54"
username = "PreetiprS"
password = "Seth#6543!"
from socket import *

try:
    print("Establishing connection to %s" % ip)
    connection = wmi.WMI(ip, user=username, password=password, port=22)
    print("Connection established")
except wmi.x_wmi:
    print("Your Username and Password of " + getfqdn(ip) + " are wrong.")


#!/usr/bin/env python
# import winrm

# # Create winrm connection.
# sess = winrm.Session(
#     "10.1.240.54", auth=("PreetiprS", "Seth#6543!"), transport="kerberos"
# )
# result = sess.run_cmd("ipconfig", ["/all"])
