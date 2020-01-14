import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, Port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

    socket_list - [sys.stdin, server]

    read_sockets, write_sockets, err_sockets = select.select(sockets_list, [], [])

    for socks in read_socket:
        if sockks == server:
            message = socks.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sysy.stdout.flush()
server.close()
