import random
import os
import signal
import sys
import requests
import glob
import base64
import string

currentUpdate = open("Version", "r").readlines()[0]


commandlineArguments = """

-h  :  Shows this help message
-c  :  Clears the screen then runs the Rat-Toolkit
-nB :  Start and do not show banner
-y  :  Accept TOS
-L  :  Listen, Accepts a port!
"""


def handler(signum, frame):
    print('To exit please write: exit')
signal.signal(signal.SIGINT, handler)
def startUp(xA):
	acceptedTOS = False
	clearScreen = False
	
	banners = glob.glob("Banners/*")
	image = random.randint(0,len(banners)-1)
	counter = 1
	for i in sys.argv:
		if i == "-c":
			os.system("clear")
			clearScreen = True
		elif i == "-h":
			print("Rat-Toolkit\n" + commandlineArguments)
			sys.exit()
		elif i == "-nB":
			image = 9999
		elif i == "-y":
			acceptedTOS = True
		elif i == "-L":
			if counter+1 == len(sys.argv):
				os.system("stty raw -echo; (stty size; cat) | nc -lvnp " + sys.argv[counter])
			else:
				port = input("Please enter the port you would like to listen to: ")
				os.system("stty raw -echo; (stty size; cat) | nc -lvnp " + port)
		counter += 1
	if acceptedTOS == False:
		print("\n\033[91m\033[4mBy accepting to the TOS you aggree that the developers of Rat-Toolkit is in no way liable for any damage or missuse caused by Rat-Toolkit\033[0m\n")
		yInput = input("(y/n)Please enter a answear: ")
		if yInput == "y" or yInput == "Y":
			acceptedTOS = True
			if clearScreen == True:
				os.system("clear")
	if acceptedTOS == False:
		print("To use the Rat-Toolkit please accept the TOS")
		sys.exit()
	if xA == 1:
		image = random.randint(1,3)
	if image != 9999:
		banner = open(banners[image-1], "r")
		print(banner.read())
		banner.close()
		print("To get started type 'help'")

startUp(0)

helpCommand = """

info : Show a info messeage

exit : Exit Rat-ToolKit
update : Get any new updates
ReloadDB : Reload exploit database, Not CAP-Scensitive
AutoUpdate : Automatically update on startup, toggleable!

listen : Listen for incoming reverse shells
search [STRING] : Search for exploit name or operating system, CAP-Scensitive, Blank search quote : search all exploits
use [STRING] : Use exploit, it needs to be full path
options : Show options for current exploit
set [OPTION] [New Value] : Allows you to set value of option
generate : Generate a payload if selected exploit supports it!
exploit : Start the exploit
clear : Clear the screen
banner : Show banner
"""

infoMesseage = """

Copyright(c) Kuri 2022

Rat-Toolkit is a toolkit similar to MetaSploit.
Rat-Toolkit is developed in python3 and is lightweight and designed as a easy to use toolkit for generating payloads for various operating system such as "Mac", "Windows" and "OSX"̈́
It is easy to add payloads onto the Rat-Toolkit by adding a payload into the CustomExploits folder.

Rat-Toolkit uses many payloads from the PayloadAllTheThings github repository: https://github.com/swisskyrepo/PayloadsAllTheThings
If a exploit/rat has the exploit option set to false it uses the generate command otherwise it exploits onto a remote host.

I am not the creator of any of the ascii art. All ascii art comes from: https://www.asciiart.eu/

Command line arguments:
""" + commandlineArguments

currentDirectory = "Rat-ToolKit"
selectedExploit = "none"

exploits = []

def loadExploits():
	exploits = []
	windowsFiles = glob.glob("PB/Windows/*")
	linuxFiles = glob.glob("PB/Linux/*")
	macFiles = glob.glob("PB/Mac/*")
	httpFiles = glob.glob("PB/HTTP/*")
	customFiles = glob.glob("CustomExploits/*")
	
	#Import Windows exploits
	for i in windowsFiles:
		xY = str(i).replace("PB/Windows/", "")
		fileLoc = open(i, "r")
		fileContent = fileLoc.readline()
		exploit = [xY, "Windows"]
		if "Generate" in fileContent:
			exploit.append(["exploit", False])
		elif "Exploit" in fileContent:
			exploit.append(["exploit", True])
		else:
			exploit = ["Bad Type"]
			exploits.append(exploit)
			break
		extension = fileContent.split(":")[1].replace("\n", "")
		exploit.append(["Extension", extension])
		LHost = False
		LPort = False
		for i in fileLoc:
			if "LISTENADDR" in i:
				LHost = True
			if "LISTENPORT" in i:
				LPort = True
		if LHost == True:
			exploit.append(["LHost", "10.10.12.3"])
		if LPort == True:
			exploit.append(["LPort", "80"])
		exploits.append(exploit)
	#Import Linux exploits
	for i in linuxFiles:
		xY = str(i).replace("PB/Linux/", "")
		fileLoc = open(i, "r")
		fileContent = fileLoc.readline()
		exploit = [xY, "Linux"]
		if "Generate" in fileContent:
			exploit.append(["exploit", False])
		elif "Exploit" in fileContent:
			exploit.append(["exploit", True])
		else:
			exploit = ["Bad Type"]
			exploits.append(exploit)
			break
		extension = fileContent.split(":")[1].replace("\n", "")
		exploit.append(["Extension", extension])
		LHost = False
		LPort = False
		for i in fileLoc:
			if "LISTENADDR" in i:
				LHost = True
			if "LISTENPORT" in i:
				LPort = True
		if LHost == True:
			exploit.append(["LHost", "10.10.12.3"])
		if LPort == True:
			exploit.append(["LPort", "80"])
		exploits.append(exploit)
	#Import Mac exploits
	for i in macFiles:
		xY = str(i).replace("PB/Mac/", "")
		fileLoc = open(i, "r")
		fileContent = fileLoc.readline()
		exploit = [xY, "Mac"]
		if "Generate" in fileContent:
			exploit.append(["exploit", False])
		elif "Exploit" in fileContent:
			exploit.append(["exploit", True])
		else:
			exploit = ["Bad Type"]
			exploits.append(exploit)
			break
		extension = fileContent.split(":")[1].replace("\n", "")
		exploit.append(["Extension", extension])
		LHost = False
		LPort = False
		for i in fileLoc:
			if "LISTENADDR" in i:
				LHost = True
			if "LISTENPORT" in i:
				LPort = True
		if LHost == True:
			exploit.append(["LHost", "10.10.12.3"])
		if LPort == True:
			exploit.append(["LPort", "80"])
		exploits.append(exploit)
	#Import HTTP exploits
	for i in httpFiles:
		xY = str(i).replace("PB/HTTP/", "")
		fileLoc = open(i, "r")
		fileContent = fileLoc.readline()
		exploit = [xY, "HTTP"]
		if "Generate" in fileContent:
			exploit.append(["exploit", False])
		elif "Exploit" in fileContent:
			exploit.append(["exploit", True])
		else:
			exploit = ["Bad Type"]
			exploits.append(exploit)
			break
		extension = fileContent.split(":")[1].replace("\n", "")
		exploit.append(["Extension", extension])
		LHost = False
		LPort = False
		RHost = False
		RPort = False
		for i in fileLoc:
			if "LISTENADDR" in i:
				LHost = True
			if "LISTENPORT" in i:
				LPort = True
			if "REMOTEADDR" in i:
				RHost = True
			if "REMOTEPORT" in i:
				RPort = True	
		if LHost == True:
			exploit.append(["LHost", "10.10.12.3"])
		if LPort == True:
			exploit.append(["LPort", "80"])
		if RHost == True:
			exploit.append(["RHost", "10.10.12.3"])
		if RPort == True:
			exploit.append(["RPort", "80"])	
		exploits.append(exploit)
	#Import custom exploits
	for i in customFiles:
		xY = str(i).replace("CustomExploits/", "")
		fileLoc = open(i, "r")
		fileContent = fileLoc.readline()
		exploit = [xY, "CUSTOM"]
		if "Generate" in fileContent:
			exploit.append(["exploit", False])
		elif "Exploit" in fileContent:
			exploit.append(["exploit", True])
		else:
			exploit = ["Bad Type"]
			exploits.append(exploit)
			break
		extension = fileContent.split(":")[1].replace("\n", "")
		exploit.append(["Extension", extension])
		LHost = False
		LPort = False
		RHost = False
		RPort = False
		for i in fileLoc:
			if "LISTENADDR" in i:
				LHost = True
			if "LISTENPORT" in i:
				LPort = True
			if "REMOTEADDR" in i:
				RHost = True
			if "REMOTEPORT" in i:
				RPort = True	
		if LHost == True:
			exploit.append(["LHost", "10.10.12.3"])
		if LPort == True:
			exploit.append(["LPort", "80"])
		if RHost == True:
			exploit.append(["RHost", "10.10.12.3"])
		if RPort == True:
			exploit.append(["RPort", "80"])	
		exploits.append(exploit)
	return exploits
exploits = loadExploits()

autoUpdate = open("AutoUpdate", "r")
if "1" in autoUpdate.read():
	f = requests.get("https://raw.githubusercontent.com/KuriWasTaken/RAT-Toolkit/main/Version")
	if str(f.text) != currentUpdate:
		print("Updating")
		os.system("git clone --quiet https://github.com/KuriWasTaken/RAT-Toolkit.git")
		versionFile = open("Version", "w")
		versionFile.write(f.text)
		versionFile.close()
		currentUpdate = f.text
		
		os.system("mv RAT-Toolkit/PB UPDATE")
		os.system("rm -rf RAT-Toolkit")
		os.system("rm -rf PB")
		os.system("mv UPDATE/PB " + str(os.getcwd()))
		exploits = loadExploits()
		print("Successfully updated exploit database, to turn AutoUpdate off run 'AutoUpdate'")
	else:
		print("Your'e all up to date, to turn AutoUpdate off run 'AutoUpdate'")
autoUpdate.close()


while True:
	x = input(currentDirectory + ">")
	if x == "Help" or x == "help":
		print(helpCommand)
	elif "search" in x or "Search" in x:
		y = x.split(" ")
		print("\n")
		if len(y) == 2:
			for i in exploits:
				if i[0] == y[1] or i[1] == y[1]:
					print("Exploit found: " + i[0] + " For: " + i[1])
		else:
			if exploits != None:
				for i in exploits:
					print("Exploit found: " + i[0] + " For: " + i[1])
		print("\n")
	elif "use" in x or "Use" in x:
		y = x.split(" ")
		for i in exploits:
			if len(y) >= 2:
				if i[0] == y[1]:
					currentDirectory = "Rat-ToolKit\\Exploits\\" + i[1] + "\\" + i[0]
					selectedExploit = i[0]
			else:
				currentDirectory = "Rat-ToolKit"
				selectedExploit = "none"
	elif x == "clear" or x == "Clear":
		os.system("clear")
	elif x == "listen" or x == "Listen":
		port = input("Please enter the port you would like to listen to: ")
		os.system("stty raw -echo; (stty size; cat) | nc -lvnp " + port)
	elif x == "exit" or x == "Exit":
		sys.exit()
	elif selectedExploit != "none":
		if "set" in x or "Set" in x:
			y = x.split(" ")
			for i in exploits:
				if i[0] == selectedExploit:
					for a in i:
						if a[0] == y[1] and a[0] != "Extension" and a[0] != "exploit":
							if len(y) != 3:
								data = input("Please enter new value: ")
								a[1] = data
							else:
								a[1] = y[2]
							break
			
		elif x == "exploit" or x == "Exploit":
			for i in exploits:
				if i[0] == selectedExploit:
					if i[2][1] == True:
						fileI = None
						if i[1] != "CUSTOM":
							fileI = open("PB/" + i[1] + "/"+selectedExploit, "r")
						else:
							fileI = open("CustomExploits/"+selectedExploit, "r")
						LPORT = ""
						LHOST = ""
						RHOST = ""
						RPORT = ""
						for a in exploits:
							if a[0] == selectedExploit:
								for b in a:
									if b[0] == "LPort":
										LPORT = b[1]
									elif b[0] == "LHost":
										LHOST = b[1]
									elif b[0] == "RHost":
										RHOST = b[1]
									elif b[0] == "RPort":
										RPORT = b[1]
						data = fileI.read().replace("LISTENADDR", LHOST).replace("LISTENPORT", LPORT).replace("REMOTEADDR", RHOST).replace("REMOTEPORT", RPORT)
						N = 10
						tempExploitName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N)) + i[3][1]
						
						tempExploit = open("tempExploits/"+tempExploitName, "w")
						tempExploit.write(data)
						tempExploit.close()
						
						#Lazy fix
						xX = open("tempExploits/"+tempExploitName, "r")
						lines = xX.readlines()
						xX.close()
						lines[0] = ""
						xX = open("tempExploits/"+tempExploitName, "w")
						xX.writelines(lines)
						xX.close()
						#End of lazy fix
						if i[3][1] == ".py": #py is defaulted to python 3
							os.system("python3 tempExploits/"+tempExploitName)
							os.system("rm tempExploits/"+tempExploitName)
						break
					else:
						print("This exploit is generated, to generate use the command : generate")
						break
		elif "show" in x or "Show" in x:
			yY = x.split(" ")
			if yY[1] == "Options" or yY[1] == "options":
				for i in exploits:
					if i[0] == selectedExploit:
						print("\n")
						for b in i:
							if len(str(b[0])) > 1 and len(str(b[1])) > 1 and b[0] != "Extension":
								print(str(b[0]) + " : " + str(b[1]))
						print("\n")
		elif x == "generate" or x == "Generate":
			for i in exploits:
				if i[0] == selectedExploit:
					if i[2][1] == False:
						fileI = None
						if i[1] != "CUSTOM":
							fileI = open("PB/" + i[1] + "/"+selectedExploit, "r")
						else:
							fileI = open("CustomExploits/"+selectedExploit, "r")
						
						LPORT = ""
						LHOST = ""
						for a in exploits:
							if a[0] == selectedExploit:
								for b in a:
									if b[0] == "LPort":
										LPORT = b[1]
									elif b[0] == "LHost":
										LHOST = b[1]
						data = fileI.read().replace("LISTENADDR", LHOST).replace("LISTENPORT", LPORT)
						if "IPLENGTH" in data:
							data = data.replace("IPLENGTH", str(len(LHOST)))
						if "PORTLENGTH" in data:
							data = data.replace("PORTLENGTH", str(len(LPORT)))
						if "(B64)" in data:
							splitted = data.split("(B64)")
							encoded = splitted[1].encode("ascii")
							b64str = base64.b64encode(encoded)
							data = data.replace("(B64)"+str(splitted[1]), str(" "+b64str.decode("ascii")))
						payloadName = input("Please enter a payload name: ")
						xX = open("payloads/"+payloadName+i[3][1], "w")
						xX.write(data)
						xX.close()
						
						#Lazy fix
						xX = open("payloads/"+payloadName+i[3][1], "r")
						lines = xX.readlines()
						xX.close()
						lines[0] = ""
						xX = open("payloads/"+payloadName+i[3][1], "w")
						xX.writelines(lines)
						xX.close()
						#End of lazy fix
						if i[3][1] == ".c":
							os.system("gcc payloads/"+payloadName+i[3][1])
							os.system("mv a.out payloads/" + payloadName + ".out")
							os.system("rm payloads/"+payloadName+i[3][1])
						print("Successfully generated payload!")
						print("To listen for reverse shells, use the command listen")
						break
					else:
						print("This exploit uses exploit, to exploit use the command : exploit")
						break
	elif "show" in x or "Show" in x:
		print("No exploit selected!")
	elif x == "banner" or x == "Banner":
		startUp(1)
	elif x == "update" or x == "Update":
		f = requests.get("https://raw.githubusercontent.com/KuriWasTaken/RAT-Toolkit/main/Version")
		if str(f.text) != currentUpdate:
			print("Updating")
			os.system("git clone --quiet https://github.com/KuriWasTaken/RAT-Toolkit.git")
			versionFile = open("Version", "w")
			versionFile.write(f.text)
			versionFile.close()
			currentUpdate = f.text
			
			os.system("mv RAT-Toolkit/PB UPDATE")
			os.system("rm -rf RAT-Toolkit")
			os.system("rm -rf PB")
			os.system("mv UPDATE/PB " + str(os.getcwd()))
			exploits = loadExploits()
			print("Successfully updated exploit database")
		else:
			print("Your'e all up to date!")
	elif x.lower() == "reloaddb":
		exploits = loadExploits()
	elif x == "info" or x == "Info":
		print("\n"+infoMesseage+"\n")
	elif x.lower() == "autoupdate":
		autoUpdate = open("AutoUpdate", "r")
		if "0" in autoUpdate.read():
			autoUpdate.close()
			autoUpdate = open("AutoUpdate", "w")
			autoUpdate.write("1")
			autoUpdate.close()
			print("Auto Update is now on!")
		else:
			autoUpdate.close()
			autoUpdate = open("AutoUpdate", "w")
			autoUpdate.write("0")
			autoUpdate.close()
			print("Auto Update is now off!")
	elif x != "":
		print("Unrecognized command")
