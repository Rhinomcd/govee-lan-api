import asyncio
import socket
import struct
import logging
import json

MULTICAST_GROUP_ADDRESS = '239.255.255.250'


class GoveeScanListener:

    def __init__(self):
        self.devices = {}

    def handleResponse(self, response):
        if response['msg']['cmd'] == 'scan':
            device_data = response['msg']['data']
            self.devices.update({device_data['device']: device_data})

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        response = json.loads(data.decode())
        self.handleResponse(response)

    def connection_lost(self, e):
        pass


def get_bound_multicast_socket():
    receive = ('', 4002)
    receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    group = socket.inet_aton(MULTICAST_GROUP_ADDRESS)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    receiver_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    receiver_sock.bind(receive)
    return receiver_sock


async def send_request(message, ip, port):
    transport, protocol = await loop.create_datagram_endpoint()


def get_send_socket():

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(1)

    ttl = struct.pack('b', 2)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    return sock


async def start_listener(command, device_scan_timeout_seconds=2):
    logging.debug("Starting Listener")
    loop = asyncio.get_running_loop()

    receiver_socket = get_bound_multicast_socket()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: GoveeScanListener(), sock=receiver_socket)

    send_sock = get_send_socket()
    try:
        if "device" in command:
            "sending device command"
            send_sock.sendto(command["message"].encode(),
                             (command["ip"], 4003))
        else:
            send_sock.sendto(command["message"].encode(),
                             (command["ip"], 4001))
            await asyncio.sleep(device_scan_timeout_seconds)

    except Exception as e:
        logging.exception(e)
    finally:
        logging.debug("Shutting down Listener")
        logging.debug("Found devices: [%s]",
                      [(k, v.get("ip")) for k, v in protocol.devices.items()])

        receiver_socket.close()
        transport.close()
        return protocol.devices
