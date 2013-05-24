#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import select

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12352                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
i = 0
connections = []
while True:
   print 'loop iteration: ', i
   rlist, wlist, xlist = select.select(connections + [s], [], [])
   c, addr = s.accept()     # Establish connection with client.
   
   
   print c.recv(1024)
   
   c.close()                # Close the connection
   i = i+1
