import socket
from bs4 import BeautifulSoup
import requests


def tcp_server():

    #sets up server with port and address
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = '127.0.0.1'
    server_port = 12452
    server_sock.bind((server_address, server_port))

    #holds up to 5 connections and confirms it's listening
    server_sock.listen(5)
    print("Server is listening for incoming connections...")

    try:
        while True:

            #gets connection
            client_sock, client_address = server_sock.accept()
            print(f"Connection from {client_address}")

            try:

                #gets url from the client
                message = client_sock.recv(1024)
                print(f"Recieved message: {message.decode()}")
                url = message

                #uses beautiful soup to parse the data from the website
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")

                #sends data as text back to the client
                data = soup.text
                response = data
                client_sock.sendall(response.encode())

            #closes the socket
            finally:
                client_sock.close()
                print(f"Connection with{client_address} closed")

    #error handling
    except KeyboardInterrupt:
        print("Server is shutting down")

    #closes socket if error
    finally:
        server_sock.close()
        print("Server socket closed")

if __name__ == "__main__":
    tcp_server()

