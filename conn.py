from fabric2 import Connection
from urllib.request import urlopen

c = Connection(
    host="10.1.240.54",
    user="PreetiprS",
    connect_kwargs={"password": "Seth#6543!"},
    port=22,
)
filepath = "http://127.0.0.1:8000/media/documents/2021-03-30/01-03-02/vm21.xlsx"
excel_file = urlopen(filepath)
with open("input.xlsx", "wb") as output:
    output.write(excel_file.read())

print(dir(c))
print(c.original_host)
print(c.port)
strin = "\\WATERLABSRT01\RainTree"

c.put(filepath, strin)
