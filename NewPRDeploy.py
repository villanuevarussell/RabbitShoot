
#Moves files from the Desktop into necessary folders
from ssh import ssh
import time

def deploy(ip, username, password, source, destination):
	f = open("Deploy.log", "a+")
	f.write(f"NewPRDeploy.py")

	try:
		print(f"Connecting to {ip}")
		f.write(f"Connecting to {ip}")

		connection = ssh(ip, username, password)#connects to remote desktop
		connection.openShell()#makes connection to remote 
		connection.sendShell(f"rm -rf ~/Desktop/firmware")#removes all files and directories currently in folder
		print(f"Moving files from {source} to {destination}")
		connection.sendShell(f"mv {source} {destination}")#moves all contents from source directory to destination directory
		time.sleep(1)#gives time for command to execute

		tempfolder = source[:-1]#removes last character from source variable, removes the * so the directory can be deleted
		connection.sendShell(f"rm -rf {tempfolder}")#removes temp folder from Desktop
		time.sleep(1)
		connection.closeConnection()#closes Connection between host and remote desktop
		print(f"************{ip} PASS********************\n")
		f.write(f"************{ip} PASS********************\n")#Writes a pass on logs
	except:
		print(f"Could not deploy, was not able to connect to {ip}")
		f.write(f"************{ip} FAIL********************\n")#writes to log
		f.write(f"IPSW Files were not Deployed to {ip}")#writes to log

	f.close()

if __name__ == "__main__":
	#These are only parameters that need to be changed
	filename = ""#Name of the IP host files
	username = ""#Username of Remote Mac Mini
	password = ""#Password of Remote Mac Mini
	source = ""#Location of IPSW files
	destination = ""#Location where IPSW files will be moved too

	

	#Opens file and iterates through file
	with open(filename) as openfileobject:
		for line in openfileobject:
			deploy(line.replace('\n',''),username,password,source, destination)
