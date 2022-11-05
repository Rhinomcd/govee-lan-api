import socket
import struct
import sys

message = b'{"msg":{"cmd":"scan","data":{"account_topic":"reserve"}}}'
multicast_group_scan = ('239.255.255.250', 4001)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(1)

ttl = struct.pack('b', 2)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
sock.sendto(message, multicast_group_scan)