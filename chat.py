from Tkinter import*
import socket

contactsName = [] #create empty list for contact names
contactsInfo = [] #create empty list for contacts connection info

#socket set up stuff
sock = socket.socket()
host = socket.gethostname()
port = 2224
sock.connect((host, port))

#sends request to start a new conversation
def sendRequest(contactinfo):
	global conactsinfo

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
	request = Button (newframe, text="Request", command=sendRequest(contactinfo.get()))
	request.grid(row=3)
	newframe.pack()
	startnew.mainloop()
	
#event to send message and clear entry field
#check for nothing in entry field
def send(event):
	convo.config(state=NORMAL)
	data = entry.get() #get data from entry field
	convo.insert(END, data) #add data to convo
	convo.insert(END, '\n')
	convo.config(state=DISABLED)
	sock.send(data) #send data to server
	entry.delete(0, END) #clear entry
	
#upon startup, check for any contacts currently hosting, connect to any online
def checkWhosOnline():
	global conactsInfo

#sends user info to host to go online
def login():
	global contactsInfo

def newUser(user, passw):
	file = open('userInfo.txt', 'w+')	

#window for user to login, stores data in userInfo.txt
def loginPrompt():
	login = Toplevel()
	login.title ("Log in")
	loginframe = Frame(login, padx=10, pady=10)
	username = Label (loginframe, text="Username:", pady=5)
	username.grid (row=0, column=0)
	user = Entry (loginframe, width=20)
	user.grid (row=0, column=1)
	password = Label (loginframe, text="Password:", pady=5)
	password.grid (row=1, column=0)
	passw = Entry (loginframe, width=20)
	passw.grid (row=1, column=1)
	logbutton = Button (loginframe, text="Log in", command=login)
	logbutton.grid(row=3, column=0)
	newbutton = Button (loginframe, text="New user")
	newbutton.grid(row=3, column=1)
	loginframe.pack()
	login.mainloop()

#----------------------------------------------------END OF FUNCTIONS-------------------------------------------




#STARTING GUI
root = Tk()
root.title("Main window")
#menubar stuff
menubar= Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="Log in", command=loginPrompt)
file.add_command(label="New", command=newconvo)
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)
root.config(menu=menubar)
#left frame to hold list of contacts
leftframe = Frame(root, width=100)
leftframe.pack(side=LEFT)
#right frame to hold conversation and input
rightframe = Frame(root)
entry = Entry(rightframe, width=40)
entry.pack(side=BOTTOM, fill=X)
entry.bind("<Return>", send)
convo = Text(rightframe, state=DISABLED, width=50, height=15)
convo.pack(side=LEFT, fill=X, expand=1)
scroll = Scrollbar(rightframe, command=convo.yview)
scroll.pack(side=LEFT, fill=Y, expand=1)
convo.config(yscrollcommand=scroll.set)
rightframe.pack(side=RIGHT, fill=BOTH, expand=1)
root.mainloop()


