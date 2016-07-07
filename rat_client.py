# RAT client python
import socket

import argparse

# use argparse define port and host
parser = argparse.ArgumentParser(description='RAT client')
parser.add_argument('--port', default=39421, help='port for connect')
parser.add_argument('--host', default='127.0.0.1', help='host for connect')
args = parser.parse_args()


def __execute_command():
    # connection socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.host, args.port))

    print("Write command execute: ")
    command = raw_input(prompt)
    print(client.send(command))
    response = client.recv(4096)
    print response
    client.close()


prompt = '> '

__execute_command()

while True:
    print("Execute other command ?")
    print ("Yes or Not ? (Y/N)")
    confirmation = raw_input(prompt)
    print confirmation
    if str(confirmation) == 'Y':
        __execute_command()
    else:
        exit()
