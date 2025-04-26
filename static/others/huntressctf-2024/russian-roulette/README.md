# Russian Roulette
## Challenge Statement:
Author: @JohnHammond

My PowerShell has been acting _really weird!!_ It takes a few seconds to start up, and sometimes it just crashes my computer!?!?! **:(**  
  
**WARNING: Please examine this challenge inside of a virtual machine for your own security. Upon invocation there is a real possibility that your VM may crash.**  
  
**NOTE: Archive password is `russian_roulette`**

Attachment: [russian_roulette.zip](russian_roulette.zip)

## Solution:
Extracting the archive outputs only a lnk file. [LNK](https://fileinfo.com/extension/lnk) files are basically shortcuts in windows. There are special files that open other files or execute commands. LNK files are a common threat vector as phishers can disguise anything as LNK file.

For this challenge we have a [Windows PowerShell.lnk](Windows\ PowerShell.lnk).  To see what it really opens we need a parser that can parse the LNK file contents. I found this tool called [LnkParse3](https://github.com/Matmaus/LnkParse3) that could do what I want. 

![target](assets/1.png)

So the target of the shortcut is not a file but a powershell command. The `-e` option allows encoded scripts or strings to execute. This is basically more powershell command but encoded in base64. 

![decoded base64](assets/2.png)

On decoding the argument, we can observe that it uses the `iwr` (`Invoke-WebRequest`) cmdlet to download the contents pointed by the link and save it to a file `.cmd` in the temp folder. Finally this `.cmd` file is executed.

Collecting the contents of the link downloaded a `powershell.zip` but it was in fact a batch script. So I renamed it to [raw_payload.bat](raw_payload.bat).

For some reason I don't know, this batch file when opened with text editors showed garbled text, but when I used `cat`  utility from the terminal it displayed the batch script. My theory was that it is because of the first two characters of the file where not recognizable. When I removed it and put the rest of the script in [payload.bat](payload.bat). 

There were a lot of Russian comments (or I should say quotes) in the file. So I put together [cleanse.py](cleanse.py) to remove those commands and write the contents to [payload cleaned.bat](payload\ cleaned.bat]. Now I had more visibility over the code.

![start of deobfuscation](assets/3.png)

I have seen this type of obfuscation before. So at the start of the script we can see a variable `ucbw` to getting set as `set`. Following it are lines that start with using the variable `ucbw`. If we replace `ucbw` as `set` everywhere in the script, it is one step deobfuscating the script.

![space in](assets/4.png)

The variable `qmy` is not empty actually. It has a white space. So replace `%qmy%` with a single whitespace in the script and replacing `%jxaa%` with `=`, we get:

![deob cont](assets/5.png)

Now we can keep on replacing variables with characters till we hit this:

![different thing](assets/6.png)

The expression `set /a rtoy=9161456 %% 9161359` mean set the variable `rtoy` with the resultant value of arithmetic expression `9161456 %% 9161359`. `%%` is the modulus operation. So rtoy will be assigned 97, in this case. Next up we have `cmd /c exit=%rtoy%`. `cmd \c` executes the command passed to it. And that command here is exit with the exit code specified by variable `rtoy`. Next up `set ztq=%=exitcodeAscii%`.  `%=exitcodeAscii%` is an undocumented dynamic variable in windows, that for some reason returns the exit code of the last program as an ascii character. 

Putting them together, the second line executes a cmd exit command with a exit code and the next command gets that exit code as ascii. In ascii 97 maps to the character 'a'.  Now the variable `%ztq%` can be used whenever you need a character 'a'. So essentially for the next many commands are just construction of alphabets, numericals and symbols. 

De-obfuscating all that yielded [payload deobfuscated.bat](payload\ deobfuscated.bat). In that you will find another encoded powershell payload. 

![base64 payload](assets/7.png)

I copied that payload and put it in [powershell base64.txt](powershell\ base64.txt) to decode the contents. 

![ps1 payload](assets/8.png)

I put the contents obtained in [powershell payload.ps1](powershell\ payload.ps1) and modified it to make it easy on the eyes.

![cs payload](assets/9.png)

Looking at the powershell script, we can see another sort of code in the variable `$s`. Since I spent some time with C#, I recognized it right away. So the code creates an compiler object, compiles the function `Shot` in the class `X` , then with a 1 out of 6 chance executes the function `Shot`. 

The function `Shot` contains some areas of interest. It imports two functions from the `ntdll.dll`. And does AES decrytion on some data. But after some time of research on the internet, I found out that `NtRaiseHardError` is an undocumented API from windows, that can be used to force BSOD (Blue Screen of Death) errors. Effectively this will restart you operating system. So even if function `Shot` is executed it crashes the OS before it reaches the decryption code. 

So I put [solve.cs](solve.cs)  removing the DLL imports and put a writeline to output the decrypted content.

![flag](assets/10.png)

And that indeed was the flag. Also if you don't want to dabble with C#, then you can just copy the decryption data on cyberchef and obtain the flag that way as well.

![flag again](assets/11.png)








