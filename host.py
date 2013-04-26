from Tkinter import*
import socket

#socket stuff
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
	

root = Tk()
root.title("CHAT")

#event to send message and clear entry field
def send(event):
	convo.config(state=NORMAL)
	convo.insert(END, entry.get()) #add entry to convo
	convo.insert(END, '\n')
	convo.config(state=DISABLED)
	#c.send(entry.get()) # send message to client
	entry.delete(0, END) #clear entry

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
convo.pack(side=TOP)
entry = Entry(rightframe, width=40)
entry.pack(side=BOTTOM)
entry.bind("<Return>", send)
rightframe.pack()

root.mainloop()


