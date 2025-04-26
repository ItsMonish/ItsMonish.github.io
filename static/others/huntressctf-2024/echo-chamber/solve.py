import subprocess
import shlex
import binascii

if __name__=="__main__":
    cmd = 'tshark -r echo_chamber.pcap -Y "frame.number >= 31773  && frame.number <= 31847 && icmp.type==8" -T "fields" -e "data.data"'
    content = subprocess.check_output(
            shlex.split(shlex.quote(cmd)), shell=True, stderr=subprocess.STDOUT
        ).decode()
    content = content.split("\n")
    hexvals = "".join([con[:2] for con in content])
    print(binascii.unhexlify(hexvals).decode())
