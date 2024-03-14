import socket
import json

#Format for the TCP connection
def tcp_client(url):

    #sets up the socket with a port number and server_address
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = '127.0.0.1'
    server_port = 12452

    try:

        #sends connection message
        sock.connect((server_address, server_port))
        print(f"Sending: {url}")
        sock.sendall(url.encode())

        #gets response
        response = sock.recv(1024)
        print(f"Received: {response.decode()}")

        #json/dict data that you can use
        data = json.loads(response)

        #example for you to mess with
        print(data['Title'])

    #error handling
    except:

        print("Hmm there seems to be an error with your echo server/client. You sure you have TCP_server.py running?")

    #close socket
    finally:
        sock.close()

#example test
test = input("What url?: ")

tcp_client(test)