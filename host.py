#===== TO DOs ======
#function to change status to online
#funciton to send client list of whos online
#make sure client doesnt sent more than 1024 bytes to host



from Tkinter import*
import socket
import threading

#if user is new, add them to the file
def newUser(user, passw):
	file = open('hostUserInfo.txt', 'w+')
	f.write(user . '\n' . passw . '\n')
	f.close

#check if user exists
def userExists(userlist):
	found = 0
	for line in userlist:
		if 

#authenticate user and change online status
def authenticate(user, passw):
	if user in open('hostUserInfo.txt').read(): #if user is already in file
		#authenticate
		#log them in
	else:
		#add them to file
		#log them in
	

#create a thread to handle recieved client data
#should take data, send data, and close connection
def clientThread(conn):
	open = 1
	while open==1:
		dest = conn.recv(1024)
		data = conn.recv(1024)
		
		if dest=="login":
			passw = conn.recv(1024)
			authenticate(data, passw)
		else:
			

#socket stuff
s = socket.socket()
host = socket.gethostname()
port = 22222
s.bind((host, port))
s.listen(5)

while True:
	conn, addr = s.accept()
	start_new_thread(clientThread, (conn,))
	

#GUI stuff
root = Tk()
root.title("hostess cakes")
activity = Text (root, width=50)
activity.insert(END, "host is running..\n")
activity.config(state=DISABLED)
activity.pack()
closesock = Button(root, text="close socket", command=s.close())
root.mainloop()

