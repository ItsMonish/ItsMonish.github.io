+++
title = "Miscellaneous - Base-p-"
date = '2025-04-26T17:51:33+05:30'
author = "Monish Kumar"
description = "One obscure encoding, and an entirely novel encoding of data"
categories = ['Writeup', "Huntress CTF 2024"]
keywords = ['Huntress CTF writeups']
summary = "One obscure encoding, and an entirely novel encoding of data"
+++
# Base-p-
## Challenge Statement:
Author: Izzy Spering

That looks like a weird encoding, I wonder what it's based on.

Attachment: [based.txt](/others/huntressctf-2024/base-p/based.txt)

## Solution:
The attachment is a text file. Opening it, the contents were in a language I didn't know. 

![contents of based](/images/huntressctf-2024/base-p/1.png)

I tried to translate the contents using google translate which detected it to be Cantonese. The title suggest some sort of base encoding so does the challenge description.

I was looking for encodings specifically base encodings that outputs such characters. Incidentally, I stumbled upon several writeups from Huntress 2023 challenge baseffff+1 such as this [one](https://github.com/ThisGuyNeedsABeer/Huntress-CTF-2023/tree/main/baseffff+1_COMPLETED) . And it seems the challenge text followed a encoding base65536. It seemed similar to the one I have now. 

I found a [online decoder](https://www.better-converter.com/Encoders-Decoders/Base65536-Decode) that decodes base65536. So I tried it.

![online decoder](/images/huntressctf-2024/base-p/2.png)

It seems that now we just have a plain base64 encoded data. I put the contents in a file [unbased.txt](/others/huntressctf-2024/base-p/unbased.txt). So decoding base64 data, we have some more data.

![decoded base64](/images/huntressctf-2024/base-p/3.png)

At first I couldn't make sense of what this is. But the 'mg' at the start of the file made me think it must be a file signature. So I ran the output through file utility.

![detect file](/images/huntressctf-2024/base-p/4.png)

So this is a gunzip archive. I put the output contents in a gunzip archive [compressed.gz](/others/huntressctf-2024/base-p/compressed.gz)  and extracted it using the `gzip` utility.  Extracting the contents gave a single file. Running file utility reveals it to be a PNG image.

![decompressing](/images/huntressctf-2024/base-p/5.png)
![detecting file](/images/huntressctf-2024/base-p/6.png)

Since it is a PNG file, I opened it to view it's contents. It seems to be a strip of colors. What it was? I had no idea.

![file color strip](/images/huntressctf-2024/base-p/7.png)

I examined EXIF data, ran the strings utility, viewed the hex code of the image. After hours of scratching my head and searching for encodings in images and may more, nothing came up. Then I showed it to my friend, who jokingly told me what if the data is the hex codes of color of the images. But guess what, it made sense. There are 13 colors. 3 bytes for one color. 39 bytes of data. 39 characters. The flag usually contains 38 characters.

So I used a color picker to read the hex color code of each color and put them in the file [color_codes](/others/huntressctf-2024/base-p/color_codes).  

![color codes](/images/huntressctf-2024/base-p/8.png)

Now this makes a lot of sense if you know your hex codes. So we just need to convert this to string. That can be achieved by: 

```bash
cat color_codes | tr -d ' ' | xxd -p -r
```

![flag](/images/huntressctf-2024/base-p/9.png)

There it was. Sometimes we just need a fresh perspective to look at things.
