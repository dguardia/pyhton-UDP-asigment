# UDPClient.py
import socket
import time
from datetime import timedelta

HOST = '128.235.208.225'
PORT = 12346
MAX = 4096



# Creating UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind the socket to the port
server_address = (HOST, PORT)
message = bytes(str(1), "ascii")
header = bytes(str(2), "ascii")
my_header_info = {'Source_Router': 0, 'Router0': 1, 'Router1': 3, 'Router2': 7}
separator = ","
completed_header = separator.join("=".join((str(k), str(v))) for k, v in my_header_info.items())

start = time.time()

try:
    print("================================================================")
    print('Sending request number: ', message.decode())
    print("================================================================")
    print('SOURCE_ROUTER', server_address)
    sent = s.sendto(message, server_address)
    end = time.time()
    elapsed_time = end - start

    #receive response
    data, address = s.recvfrom(MAX)
    print('from client      '.upper(), s.getsockname())
    print('from server:     {!r}'.format(data.decode()).upper(), address)
    print('Time Elapse      ', str(timedelta(seconds=elapsed_time)))
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

