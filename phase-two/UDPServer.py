# UDPServer.py
import socket
import sys
import random
import datetime
from shortest_distance import g


def Main():
    HOST = '128.235.208.225'
    # HOST = 'localhost'
    PORT = 12346
    MAX = 4096

    # Datagram (udp) socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('Socket created')
    except socket.error as msg:
        print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    # Bind the socket to the port
    server_address = (HOST, PORT)
    my_header_table = g.distances
    print(my_header_table)

    try:
        s.bind(server_address)
    except socket.error as msg:
        print(msg)
    print('Socket Bind completed')
    # print('Listening at', s.getsockname())
    print('starting up on {} port {}'.format(*server_address))
    message =['Requested Header Information:',  'We received your headers']



    while True:
        # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        current_time = datetime.datetime.now().time()
        print('\nwaiting to receive message...')
        data, address = s.recvfrom(MAX)
        grabAddress = address[0]
        print(grabAddress)
        first_msg = grabAddress + ' ' + message[0]
        second_message = message[1]

        if data == b'1':
            print("requested number:".upper(), data.decode('UTF-8'), 'from ROUTER0 address: ', address)
            print(current_time, 'received {} bytes from {}'.format(len(data), address))
            print('Sending Header Information to: ', address)
            sent = s.sendto(first_msg.encode(), address)
            print(current_time, 'sent {} bytes back to {}'.format(sent, address))
        elif data == b'2':
            print("Received Header Information :".upper(), data.decode('UTF-8'), 'from address: ', address)
            sent = s.sendto(second_message.encode(), address)
            print(current_time, 'sent {} bytes back to {}'.format(sent, address))
            new_data, same_address = s.recvfrom(MAX)
            print('ROUTER0 Header information'.upper(), new_data.decode(), 'FROM:', same_address)
            header_info = s.sendto(new_data, same_address)
            print('received {} bytes from {}'.format(len(new_data), same_address))

        print(current_time, 'received {} bytes from {}'.format(len(data), address))
        print("******************************************************************")

if __name__ == '__main__':
    Main()
