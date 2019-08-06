'''
This adds SSH Keys to all IP addresses in specified file name
Only parameters that need to be changed are username and filename
Note:you must insert the password for each remote computer you need to connect to
This only needs to be done when first setting up a computer Mac with RabbitShoot
You can copy and paste password if all passwords are the same 


The purpose of this is so that it allows your computer to connect to remote computers without a password
'''
import pexpect

def updateKeys(ip,username,password):
	print(f"Update Public Key for {ip}")

	child = pexpect.spawn(f"ssh-copy-id -o ConnectTimeout=5 {username}@{ip}")
	option = child.expect(["Are you sure you want to continue connecting (yes/no)?","[P|p]assword","already exist"])
	if option == 0:
		child.sendline('yes')
		child.sendline(password)	
		child.expect(pexpect.EOF)
		print(child.before)
	if option == 1:
		child.sendline(password)	
		child.expect(pexpect.EOF)
		print(child.before)
	if option == 2:
		print(child.before)

	print(f"SSH Key added to IP:{ip}")



if __name__ == "__main__":

	username = ""
	password = ""
	filename = ""

	#Opens file and iterates through file
	with open(filename) as openfileobject:
		for line in openfileobject:
			updateKeys(line ,username,password)

