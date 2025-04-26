#!/bin/bash

tshark -r keyboard_junkie -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keystrokes.txt
python ./ctf-usb-keyboard-parser/usbkeyboard.py keystrokes.txt
