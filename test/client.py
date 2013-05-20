#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12352                # Reserve a port for your service.

s.connect((host, port))
data = sys.stdin.read()
s.send(data)

s.close                     # Close the socket when done
