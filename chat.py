from Tkinter import*
import socket

contactsName = [] #create empty list for contact names
contactsInfo = [] #create empty list for contacts connection info

#client thingy
def thing():
	s = socket.socket()
	host = socket.gethostname()
	port = 2328
	s.connect((host, port))
	print s.recv(1024)

#host thingty
def thingy():
	s = socket.socket()
	host = socket.gethostname()
	port = 2328
	s.bind((host, port))
	s.listen(1)
	addr = ""
	c = ""
	while (addr==""):
		c, addr = s.accept()
		print "Host got a connection woo"
		c.send("message sent to client")
		
#set up a new connection/contact/converation
def newconvo():
	startnew = Toplevel()
	startnew.title("New contact info")
	newframe = Frame(startnew, padx=10, pady=10)
	displayname = Label (newframe, text="Display name:", pady=5)
	displayname.grid (row=0, column=0)
	name = Entry (newframe, width=20)
	name.grid (row=0, column=1)
	contactinfo = Label (newframe, text="Contact info:", pady=5)
	contactinfo.grid (row=1, column=0)
	info = Entry (newframe, width=20)
	info.grid (row=1, column=1)
	newframe.pack()
	startnew.mainloop()
	
	

#event to send message and clear entry field
def send(event):
	convo.config(state=NORMAL)
	convo.insert(END, entry.get()) #add entry to convo
	convo.insert(END, '\n')
	convo.config(state=DISABLED)
	entry.delete(0, END) #clear entry
	
#upon startup, check for any contacts currently hosting, connect to any online
def checkWhosOnline():
	global conactsInfo


#start GUI
root = Tk()
root.title("CHAT")

#menubar stuff
menubar= Menu(root)

file = Menu(menubar, tearoff=0)
file.add_command(label="New", command=newconvo)
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)

root.config(menu=menubar)

#left frame to hold list of contacts
leftframe = Frame(root, width=100)
leftframe.pack(side=LEFT)

#right frame to hold conversation and input
rightframe = Frame(root)

convo = Text(rightframe, state=DISABLED, width=50, height=15)
convo.pack(side=LEFT)
scroll = Scrollbar(rightframe, command=convo.yview)
scroll.pack (side=LEFT, fill=Y)
convo.config(yscrollcommand=scroll.set)

entry = Entry(rightframe, width=40)
entry.pack(side=BOTTOM)
entry.bind("<Return>", send)

rightframe.pack()

root.mainloop()

