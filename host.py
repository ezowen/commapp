from Tkinter import*
import socket


	

#GUI stuff
root = Tk()
root.title("hostess cakes")

activity = Text (root, width=50)
activity.insert(END, "host is running..\n")
activity.config(state=DISABLED)
activity.pack()

root.mainloop()


