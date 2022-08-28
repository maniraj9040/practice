import os
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(
    "10.1.240.54",
    username="PreetiprS",
    password="Seth#6543!",
    allow_agent=False,
    look_for_keys=False,
)
sftp = ssh.open_sftp()
# sftp.get()
# sftp.chdir("\\10.1.240.54\\RainTree")
sftp.put(
    "/home/waterlabs/Desktop/mindtree/input.xlsx",
    "\\WATERLABSRT01\RainTree\input.xlsx",
)
sftp.close()
ssh.close()

# import base64
# import paramiko

# key = "AAAAB3NzaC1yc2EAAAADAQABAAABAQCGmBc/FIGP64iqTtGCijOvGnmWSA0zRCUUgy0CDNlwN1KL0HmrnTWkPjv1VM7WYTSrOK2yD+qxhGEgnZBNZSn+q02mHZ7dZMW1Dzntao3vSp8AIxC/O0kHOw2ZJ4MGWhiXhk0sJidr++z7Sby0hirhHgzKjD9pEwfFtBxMCtG8jbax7VvvrtoSJOv93OITxKuFquMNjzx6pF9s00CY3mrGP"
# client = paramiko.SSHClient()
# client.get_host_keys().add("10.1.240.54", "ssh-rsa", key)
# client.connect("10.1.240.54", username="waterlabs/PreetiprS", password="Seth#6543!")
# stdin, stdout, stderr = client.exec_command("ls")
# for line in stdout:
#     print("... " + line.strip("\n"))
# client.close()