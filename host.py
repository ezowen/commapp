#===== TO DOs ======
#function to change status to online
#funciton to send client list of whos online
#make sure client doesnt sent more than 1024 bytes to host



from Tkinter import*
import socket
import select


#if user is new, add them to the file
def newUser(user, passw):
	file = open('hostUserInfo.txt', 'w+')
	f.write(user +'\n' + passw + '\n')
	f.close

#sets user status to online
def login():
	deleteme=1
	#change online status
	#fetch any awaiting messages

#checks user vs password
def authenticate(user, passw):
	info = open('hostUserInfo.txt').readlines()
	if user in info:
		if info[info.index(user)+1]==passw:
			login(user, passw)
		else:
			deleteme=1
	else:
		deleteme=1

#create a thread to handle recieved client data
#should take data, send data, and close connection
def clientThread(conn):
	open = 1
	while open==1:
		dest = conn.recv(1024) #username or "login"
		data = conn.recv(1024) #message or username
		
		if dest=="login":
			passw = conn.recv(1024)
			authenticate(data, passw)
			activity.insert(END, data+" connecting with password: "+passw)
		else:
			deleteme=1

#recieve connections
def recieveConnections(servsoc):
	while 1:
		conn, addr = servsoc.accept()
	

print "HOST STARTED..."

#socket stuff
servsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2224
servsoc.bind((host, port))
servsoc.listen(5)

connections = [] #list of sockets to read from

while 1:
	rlist, wlist, xlist = select.select(connections + [servsoc], [], [])
	for r in rlist:
		if r == servsoc:
			conn, addr = r.accept()
			connections.append(conn)
			continue
		try:
			data = r.recv(1024)
		except socket.error:
			print "no data recieved from" + conn
		if data:
			print data
	

#~ #GUI stuff
#~ root = Tk()
#~ root.title("server")
#~ activity = Text (root, width=50)
#~ activity.insert(END, "host is running: "+host+" on port "+str(port)+"\n")
#~ activity.config(state=DISABLED)
#~ activity.pack()
#~ closesock = Button(root, text="close socket", command=s.close())
#~ closesock.pack()

#~ root.mainloop()

	
	
	
	