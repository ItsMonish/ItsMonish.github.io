+++
title = "Warmup - Whamazon"
date = '2025-04-26T17:51:33+05:30'
author = "Monish Kumar"
description = "A classic software logic bug based challenge"
categories = ['Writeup', "Huntress CTF 2024"]
keywords = ['Huntress CTF writeups']
summary = "A classic software logic bug based challenge"
+++
# Whamazon
## Challenge Statement:
Author: @JohnHammond

Wham! Bam! Amazon is entering the hacking business! Can you buy a flag?

**Note**: This challenge was accompanied with a per-user instance

## Solution:
Starting the instance, I was provisioned a URL to an page. It was a [GoTTY](https://github.com/yudai/gotty) application. I was greeted with a menu to begin with.

![Greeting](/images/huntressctf-2024/whamazon/1.png)

Examining the inventory, it tells that we have to buy something.

![examining inventory](/images/huntressctf-2024/whamazon/2.png)

So, I decided to look at what was for sale.

![sale menu](/images/huntressctf-2024/whamazon/3.png)

It appears we have 50 dollars in my account and among many items the flag was also listed. So I went ahead and tried to buy it.

![attempt to buy flag](/images/huntressctf-2024/whamazon/4.png)

So we need quite the sum of money to buy the flag. At this point I thought there would be some session variable or token that contains the available balance on my account. I even went to inspect the web socket traffic and decode it in attempts to find it. 

And then it hit me. I tried to buy -1 quantity of Apples. And it worked. 

![the trick](/images/huntressctf-2024/whamazon/5.png)

So it is one of the oldest tricks in the book, insufficient input validation. So we should be able to use this to add money to our account and buy the flag. And that's exactly what I did.

![exploiting](/images/huntressctf-2024/whamazon/6.png)

So now that I have the balance I went ahead and bought the flag. But that's not it. I was invited to a Rock, Paper, Scissors and the program said it won't choose scissors. So I chose rock. It was a tie.

![buying flag and game](/images/huntressctf-2024/whamazon/7.png)

It played rock everytime, so when I chose paper I won and it said the flag was added to my inventory.

![winning game](/images/huntressctf-2024/whamazon/8.png)

Then I quit the game and the buy menu and opened my inventory. The flag was right there.

![inventory and flag](/images/huntressctf-2024/whamazon/9.png)


