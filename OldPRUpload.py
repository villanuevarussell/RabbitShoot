
#This script works assuming you set up your SSH Keys with all remote computers in master list
#If you are not sure run SSHKey.py 
#This script uploads 

import os
from ssh import ssh


def upload(ip,username,password,source,destination):
	print(f"Uploading files on to {ip}'s to {destination}.......")
	#used for creating a log
	f = open("Upload.log","w+")
	#loops 10 times to ensure all files are downloaded
	try:
		for i in range(0,10):
			os.system(f"rsync -zavP -r {source} {username}@{ip}:{destination}")#syncs host Desktop to remote Desktop(Downloads IPSW Files onto user desktop)
		print(f"************{ip} PASS********************")
		f.write(f"************{ip} PASS********************")#Log Write
	except:
		print("File did not upload!")
		f.write(f"************{ip} FAIL********************")#Log Write
		f.write(f"Files were not Uploaded to {ip}")


	f.close()


if __name__ == "__main__":
	#These are only parameters that need to be changed
	filename = ""#List of IP addresses
	username = ""#Username of Remote Mac Mini
	password = ""#Password of Remote Mac Mini
	source = ""#Location of files taht will be transferred to remote Mac Mini
	destination = ""#Location where files will be downloaded too

	#Opens file and iterates through file (Iterates through host list)
	with open(filename) as openfileobject:
		for line in openfileobject:
			upload(line.replace('\n',''),username,password,source,destination)
