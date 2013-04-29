#===== TO DOs ======
#function to change status to online
#funciton to send client list of whos online
#make sure client doesnt sent more than 1024 bytes to host



from Tkinter import*
import socket
import thread

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

#socket stuff
s = socket.socket()
host = socket.gethostname()
port = 2224
s.bind((host, port))
s.listen(5)
conn=""
while conn=="":
	conn, addr = s.accept()
	print "Connection made from "+str(conn)+" at "+str(addr)
	thread.start_new_thread(clientThread, (conn,))

#GUI stuff
root = Tk()
root.title("server")
activity = Text (root, width=50)
activity.insert(END, "host is running: "+host+" on port "+str(port)+"\n")
activity.config(state=DISABLED)
activity.pack()
closesock = Button(root, text="close socket", command=s.close())
closesock.pack()

root.mainloop()

	
	
	
	