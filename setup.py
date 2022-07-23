import sys
import os

print("Please run as sudo!")

print("Welcome to the Rat-Toolkit setup process!")
print("Select an option below to get started!")
print("[1] = Install dependecies")
print("[2] = Update the script")
print("[0] = exit")

while True:
	opt = input(">")
	if "1" in opt:
		print("Installing dependencies, this might take a while!")
		os.system("sudo apt-get install netcat -y")
		os.system("sudo pip install random")
		os.system("sudo pip install signal")
		os.system("sudo pip install glob")
		os.system("sudo pip install requests")
		os.system("sudo pip install base64")
		os.system("sudo pip install string")
		print("Sucessfully installed dependencies, You can now run ratkit.py!")
	elif "2" in opt:
		os.system("git clone --quiet https://github.com/KuriWasTaken/RAT-Toolkit.git")
		os.system("rm ratkit.py")
		os.system("mv RAT-Toolkit/ratkit.py UPDATE/ratkit.py")
		os.system("rm -rf RAT-Toolkit")
		os.system("mv UPDATE/ratkit.py " + str(os.getcwd()))
	elif "0" in opt:
		sys.exit()