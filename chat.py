
from Tkinter import*
root = Tk()
root.title("Chat")

#event to send message and clear entry field
def send(event):
	convo.config(state=NORMAL)
	convo.insert(END, entry.get()) #add entry to convo
	convo.insert(END, '\n')
	convo.config(state=DISABLED)
	entry.delete(0, END) #clear entry


#menubar stuff
menubar= Menu(root)
menubar.add_command(label="file")
menubar.add_command(label="contacts")
menubar.add_command(label="conversation")
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
