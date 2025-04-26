+++
title = "Forensics - Obfuscation Station"
date = '2025-04-26T17:51:33+05:30'
author = "Monish Kumar"
description = "A simple obfuscated powershell script"
tags = ["Forensics","Powershell"]
categories = ['Writeup', "Huntress CTF 2024"]
keywords = ['Huntress CTF writeups']
summary = "A simple obfuscated powershell script"
+++
# Obfuscation Station
## Challenge Statement:
Author: @resume

You've reached the Obfuscation Station!  

Can you decode this PowerShell to find the flag?  

**Archive password: `infected-station`**

Attachment: [challenge.zip](/others/huntressctf-2024/obfuscation-station/challenge.zip)

## Solution:
Extracting the archive, we have a powershell script with the following contents:

![chal.ps1](/images/huntressctf-2024/obfuscation-station/1.png)

The script seems to decode a base64 data, decompresses it to a stream and converts it to a string and then extracts some characters from an environment variable and joins them. I thought 'iex' and I was right.

![iex](/images/huntressctf-2024/obfuscation-station/2.png)

So I tried to put the string into a variable and output it. But the script kept throwing errors at me. So I wrote another script mimicking the same logic, but cleaner. Putting them at [solve.ps1](/others/huntressctf-2024/obfuscation-station/solve.ps1), and executing it, gave the flag.

![flag](/images/huntressctf-2024/obfuscation-station/3.png)


