import socket as sock

HOST = '127.0.0.1'
PORT = 9092





def get_image_path(url):
    socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket.connect((HOST, PORT))

    socket.send(url.encode('utf-8'))

    message = str(socket.recv(1024))

    path = message[2:-1]

    print(path)
    return path



Pokemon_Image = "https://www.serebii.net/pokemon/art/001.png"


get_image_path(Pokemon_Image)
