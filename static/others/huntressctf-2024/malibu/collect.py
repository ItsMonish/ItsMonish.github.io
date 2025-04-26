# type: ignore

import requests
import sys

with open('xmlCon.xml') as f:
    cons = f.read()

content = cons.split('\n')
keys = []


for line in content:
    line = line.strip()
    if line[:5] == "<Key>":
        keys.append(line[5:-6])

port = int(sys.argv[1])
with open('out.txt', 'w') as f:
    f.write(keys)
    for key in keys:
        con = requests.get("http://challenge.ctf.games:{}/bucket/{}".format(port,key)).content.decode()
            f.write(key+'\n')
            f.write(con+'\n')
