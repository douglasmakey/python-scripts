# Rat shell control - client python
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

    try:
        client.connect((args.host, args.port))
    except socket.error as msg:
        print "Error in sockect connection %s" % str(msg)
        exit()

    print("Write command execute: ")
    command = raw_input(prompt)
    client.send(command)
    response = client.recv(4096)
    if response is None:
        print "[Server] without response"
    print response
    client.close()


prompt = '> '

__execute_command()

while 1:
    print("Execute other command ?")
    print ("Yes or Not ? (Y/N)")
    confirmation = raw_input(prompt)
    print confirmation
    if str(confirmation) in ['Y', 'y', 'yes', 'YES', 'Yes']:
        __execute_command()
    else:
        exit()
