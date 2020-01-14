import socket
import select
import sys
from thread import *

# AF_INET - Address Domain of the socket
# SOCK_STREAM - TYpe of socket (continuos flow of data read)
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks if sufficient arguments were provided
if len(sys.argv) != 3:
    print "Crrect usage: script, IP Address,, Port Number"
    exit()

# takes the first argument from cmd prompt
IP_address = str(sys,argv[1])

# takes seconf argument from cmd prompt
Port = int(sys.argv[2])

""" Binds theserver to an entered IP  address and at the specified port number
The client must be aware of thuis parameters
"""

srever,bind((IP_address, Port))

"""
listen for 100 actiove connections. this number can be increased as per convinient

"""
sever.listen(100)

list_of_clients = []

def clientThread(conn, addr):
    #seeds a message to the client whose user object is conn
    conn.send("welcome to this chatroom!")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                """prints the message and address of the user"""
                print "<" + addr [0] + "> " + message
                # calls broadcast function to send message
                mess_to_send = "<" + addr[0] + "> " + message
                broadcast(mess_to_send, conn)

            else:
                """message may not have content if the connection is broken,
                in this case remove connectiopn"""

