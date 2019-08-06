
#Moves files from the Desktop into necessary folders
from ssh import ssh
import time

def deploy(ip, username, password, source, destination):
	f = open("Deploy.log", "a+")
	f.write(f"OldPRDeploy.py")
	
	try:
		print(f"Connecting to {ip}")
		f.write(f"Connecting to {ip}")

		connection = ssh(ip, username, password)#connects to remote desktop
		connection.openShell()#makes connection to remote 
		connection.sendShell(f"rm -rf {destination}/*")#removes all files and directories currently in folder
		print(f"Moving files from {source} to {destination}")
		connection.sendShell(f"mv {source} {destination}")#moves all contents from source directory to destination directory
		time.sleep(1)#gives time for command to execute

		tempfolder = source[:-1]#removes last character from source variable, removes the * so the directory can be deleted
		time.sleep(1)
		connection.sendShell(f"rm -rf {tempfolder}")#removes temp folder from Desktop
		connection.closeConnection()#closes Connection between host and remote desktop
	except:
			print(f"Could not deploy, was not able to connect to {ip}")
		f.write(f"************{ip} FAIL********************\n")#writes to log
		f.write(f"IPSW Files were not Deployed to {ip}")#writes to log

if __name__ == "__main__":
	#These are only parameters that need to be changed
	filename = ""#IP Host list
	username = ""#Username of remote mac mini
	password = ""#Password of remote mac mini
	source = ""#location of IPSW files
	destination = ""#Location where IPSW files will be moved too

	#Opens file and iterates through file
	with open(filename) as openfileobject:
		for line in openfileobject:
			deploy(line.replace('\n',''),username,password,source, destination)
