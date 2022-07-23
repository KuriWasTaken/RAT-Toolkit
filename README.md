# RAT-Toolkit
Rat-ToolKit is a tool developed for ease of use. It is very similar to metasploit. It comes preloaded with a few exploits and backdoors but we are working on adding more! You can also write your own exploits for Rat-ToolKit in languages such as:
```
Python
Lua
C
Bash
etc etc.
```
# Installation
```
git clone https://github.com/KuriWasTaken/RAT-Toolkit.git
cd RAT-Toolkit
python3 setup.py

python3 ratkit.py -h
```

# Info
Rat-Toolkit is not a replacement for MetaSploit but rather a tool I developed for fun

As I am a full time student and am only working on this in my freetime consider donating here:

[Donations.](https://www.paypal.com/paypalme/ElysiaCoffe)

If you have any questions about Rat-ToolKit do not hesitate to ask me over on Discord:
```
Kuri#1686
```
Also if you do write any cool exploits for Rat-ToolKit, hit me up over on discord and I can add them into the tool!
Please also report bugs/errors to me on discord and I will get to fixing them!

# Tutorials
Writing exploits for Rat-Toolkit is simple!

Make a empty document with no extension and place it into CustomExploits.

On the first line we define 2 pieces of information: If it is generated or Exploited and the extension. A generated exploit would be something like a rat/virus. Meanwhile a exploited exploit does something without having to be generated, for example run nmap on a ip etc etc. To do this you do: 
```
Exploit:.extension 
```
Exploit can be changed for Generate!

There are 4 keywords. I will make it so you can add your own in the future. Anyways the key words are:
```
LISTENADDR
LISTENPORT
REMOTEADDR
REMOTEPORT
```
Every keyword has a corresponding Variable:
```
LISTENADDR = LHost
LISTENPORT = LPort
REMOTEADDR = RHost
REMOTEPORT = RPort
```
So lets say that you need to get acces to the RHost variable inside of the exploit(All variable values are entered by the user if the selected exploit uses it!)
You would just replace what ever string with "REMOTEADDR" etc etc.
So a exploit that prints the RHost written in python would look like this:
```
Exploit:.py
print("REMOTEADDR")
```
