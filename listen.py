import socket
import struct
import sys

receive = ('', 4002)
receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

group = socket.inet_aton('239.255.255.250')
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
receiver_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

receiver_sock.bind(receive)


while True:
    print(receiver_sock.recv(10240))
