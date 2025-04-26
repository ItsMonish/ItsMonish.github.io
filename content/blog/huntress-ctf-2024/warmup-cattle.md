+++
title = "Warmup - Cattle"
date = '2025-04-26T17:51:33+05:30'
author = "Monish Kumar"
description = "A esoteric language based challenge"
categories = ['Writeup', "Huntress CTF 2024"]
keywords = ['Huntress CTF writeups']
summary = "A esoteric language based challenge"
+++
# Cattle
## Challenge Statement:
Author: @JohnHammond

I know it's an esoteric challenge for a Capture the Flag, but could you herd these cows for me?

Attachment: [cattle](/others/huntressctf-2024/cattle/cattle)

## Solution:
After downloading the file given and reading it, I found it filled with variations of moo, ooo, mmo and so on.

![Contents of cattle file](/images/huntressctf-2024/cattle/1.png)

Since I spend some time with esoteric languages I recognized this as a programming language called [COW](https://esolangs.org/wiki/COW).
So all I did was find an online code execution environment and ran it. I used [this](https://www.jdoodle.com/execute-cow-online) from JDoodle and got the flag.

![Output of COW code](/images/huntressctf-2024/cattle/2.png)

