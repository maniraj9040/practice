import time
from smb.SMBConnection import SMBConnection
from six.moves import urllib
from urllib.request import urlopen


userID = "PreetiprS"
password = "Seth#6543!"
client_machine_name = "waterlabs-Latitude-5490"
server_name = "WATERLABSRT01"
server_ip = "10.1.240.54"
domain_name = "RainTree"

conn = SMBConnection(
    userID,
    password,
    client_machine_name,
    server_name,
    domain=domain_name,
    use_ntlm_v2=False,
    is_direct_tcp=True,
)

conn.connect(server_ip, 445)

# shares = conn.listShares()
excel_file = urlopen(
    "http://127.0.0.1:8000/media/documents/2021-02-11/10-02-55/empty.xlsx"
)
with open("input.xlsx", "wb") as output:
    output.write(excel_file.read())
time.sleep(2)
with open("input.xlsx", "rb") as file:
    conn.storeFile("RainTree", "input/input.xlsx", file)

with open("runfile.bat", "w") as output:

    output.write(
        '"c:\\Program Files\\Java\\jdk-18.0.2\\bin\\java" -cp "c:\\Users\\PreetiprS\\Documents\\Raintree1\\lib\\*" waterlabs.Raintree '
        + "asfdasdf"
        + " "
        + "asdfads"
        + " "
        + "asddf"
        + " "
        + "adfsadf"
        + " "
        + "true"
    )
time.sleep(2)
with open("runfile.bat", "rb") as file:
    conn.storeFile("RainTree", "script/runfile.bat", file)

conn.close()
