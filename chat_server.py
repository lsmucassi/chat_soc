import socket
import select
import sys
from thread import *

#AF_INET - Address Domain of the socket
sever = socket.socket(socket.AF_INET)
