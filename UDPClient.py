# UDPClient.py
import socket
import time
from datetime import timedelta
from Dijkstra import short_path
from shortest_distance import g

HOST = '128.235.209.205'
# HOST = 'localhost'  # for testing purpose
PORT = 12346
MAX = 4096
# Creating UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
START = time.time()
ID = '128.235.208.201'
# ID = HOST

# myOwnId = ID
destId = '128.235.209.205'


def getMyOwnIP(a):
    ip = a.decode().split(' ', 1)
    return ip[0]


def printDistance(a, b):
    print('From %s, to %s' % (a, b))
    print('The cost is : %s and the the path is: %s' % short_path(g, a, b))


# Bind the socket to the port
server_address = (HOST, PORT)
message = bytes(str(1), "ascii")
header = bytes(str(2), "ascii")
my_header_info = g.distances
separator = ","
completed_header = separator.join("=".join((str(k), str(v))) for k, v in my_header_info.items())



try:
    print("================================================================")
    print('Sending request number: ', message.decode())
    print("================================================================")
    print('SOURCE_ROUTER', server_address)
    print('Here my nodes', g.nodes)
    print('Here my distances', g.distances)
    sent = s.sendto(message, server_address)
    end = time.time()
    elapsed_time = end - START
    # printDistance(ID, HOST)
    print("===============+++++==============+++++++++++===========++++====")

    # receive response
    data, address = s.recvfrom(MAX)
    print('from client      '.upper(), s.getsockname())
    print('from server:     {!r}'.format(data.decode()).upper(), address)
    print('Time Elapse      ', str(timedelta(seconds=elapsed_time)))
    # print(data.decode())
    # print(getMyOwnIP(data))
    # printDistance(ID, destId)
    # printDistance(ID, address[0])
    printDistance(getMyOwnIP(data), address[0])  # Use in the server for local access comment this line
    print("================================================================")
finally:
    print('Sending heading information')
    my_headers = s.sendto(header, server_address)
    s.sendto(completed_header.encode(), server_address)
    print('Source Router sending header: ', header.decode())
    modifiedMessage, serverAddress = s.recvfrom(MAX)
    print('From Router1 say          :   {!r}'.format(modifiedMessage.decode()).upper(), serverAddress)
    modifiedMessage_2, serverAddress_2 = s.recvfrom(MAX)
    print('From Router1 say you sent :  {!r}'.format(modifiedMessage_2.decode()).upper(), serverAddress_2)
    print('closing socket!'.upper())
    s.close()

