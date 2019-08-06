
#This script works assuming you set up your SSH Keys with all remote computers in master list
#If you are not sure run SSHKey.py 
#This script uploads 

import os
from ssh import ssh


def upload(ip,username,password,source,destination):
	print(f"Uploading files on to {ip}'s to {destination}.......")
	f = open("Upload.log","a+")	#used opening Upload.log file. If file does not exist it creates one
	f.write(f"NewPRUpload.py\n")#Writes a pass on logs

	#syncs 2 locations to ensure the source is in the destination
	#In this application it is just making sure that the IPSW files are on the Remote Desktop
	try:
		for i in range(0,10):#loops 10 times to make sure nothing was missed
			os.system(f"rsync -zavP -r {source} {username}@{ip}:{destination}")#Syncs Source Desktop with remote desktop(downloads files onto remote Desktop)
		print(f"************{ip} PASS********************")
		f.write(f"************{ip} PASS********************\n")#Writes a pass on logs
	except:
		print(f"IPSW files did not upload, was not able to connect to {ip}")
		f.write(f"************{ip} FAIL********************\n")#writes to log
		f.write(f"IPSW Files were not Uploaded to {ip}")#writes to log


	f.close()#closes log


if __name__ == "__main__":
	#These are only parameters that need to be changed
	filename = ""#Host IP file
	username = ""#User Name of Mac Mini
	password = ""#password of Mac Mini

	source = ""#Path of IPSW files that will be transferred
	destination = f""#Path of remote mac mini where files will be transferred too

	#Opens file and iterates through file
	with open(filename) as openfileobject:
		for line in openfileobject:
			upload(line.replace('\n',''),username,password,source,destination)
