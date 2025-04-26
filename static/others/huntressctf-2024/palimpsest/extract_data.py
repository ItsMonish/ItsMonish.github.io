import csv
import binascii

file = "./converted_csv_files/Application.csv"
firstLine = True
data = b""

with open(file) as f:
    csv_rec = csv.reader(f,delimiter="|")
    for row in csv_rec:
        if firstLine:
            firstLine = False
            continue
        if row[0] == "Mslnstaller" and int(row[4][:-2]) in range(40000,65000):
            data += binascii.unhexlify(row[17])

with open('from_evtx_data','wb') as f:
    f.write(data)
