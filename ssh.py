import threading, paramiko


class ssh:
	shell = None
	client = None
	transport = None

#initializes ssh Class
	def __init__(self, address, username, password):
		#Prints connecting to server
		print("Connecting to server on ip", str(address) + ".")
		#creates a client class
		self.client = paramiko.client.SSHClient()
		#if it is user's first time connecting to remote computer, it auto adds adding to host
		self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
		#connects to the host
		self.client.connect(address, username = username, password = password, look_for_keys=False)
		#creates a transport class, used to keep a connection to host
		self.transport = paramiko.Transport((address, 22))
		#holds connection with host
		self.transport.connect(username=username, password=password)

		#shows what data is being shown on remote terminal
		thread = threading.Thread(target=self.process)
		thread.daemon = True
		thread.start()

#closes connection between host and client
	def closeConnection(self):
		if(self.client != None):
			self.client.close()
			self.transport.close()

#creates an instance of connection between host and client
	def openShell(self):
		self.shell = self.client.invoke_shell()

#sends a command to hosts terminal
	def sendShell(self, command):

		if(self.shell):
			self.shell.send(command + "\n")
		else:
			print("Shell not opened.")

#shows data this is being processed
	def process(self):
		global connection
		while True:
		# Print data when available
			if self.shell != None and self.shell.recv_ready():
				alldata = self.shell.recv(1024)
				while self.shell.recv_ready():
					alldata += self.shell.recv(1024)
				strdata = str(alldata, "utf8")
				strdata.replace('\r', '')
				print(strdata, end = "")
				if(strdata.endswith("$ ")):
					print("\n$ ", end = "")


if __name__ == "__main__":
	ip = ''
	username = ''
	password = ''




	connection = ssh(ip, username, password)
	connection.openShell()
	
	#This mimics remote's terminal by waiting for input
	#if the command == logout it closes connection with remote
	while True:
		command = input('$ ')
		print('\n')
		if command == 'logout':
			connection.closeConnection()
			break
		connection.sendShell(command)
