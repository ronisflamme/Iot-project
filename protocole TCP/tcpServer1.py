import ssl
import socket

from pip._vendor import requests

response = requests.get("https://localhost", verify=False, )

# Define the SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="C:\Program Files (x86)\OpenSSL-Win32\bin\certificate", keyfile="C:\Program Files (x86)\OpenSSL-Win32\bin\certificate\privateKey.key")

# Configuration du serveur
host = 'localhost'
port = 8000


# Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
tcp_socket.bind((host, port))

# Listen for incoming connections
tcp_socket.listen()
print("Serveur TCP démarré. En attente de connexions...")

while True:
    # Accept incoming connections
    client_socket, addr = tcp_socket.accept()
    print("Client connecté :", addr)
    # Wrap the socket with SSL/TLS
    secure_socket = ssl_context.wrap_socket(client_socket, server_side=True)

    # Receive data from the client
    data = secure_socket.recv(1024)
    print(data)
    received_data = data.decode()
    print("Message reçu du client :", received_data)
    # Process the data
    # ...

    # Send data back to the client
    secure_socket.sendall(b'Thank you for connecting')

    # Close the connection
    secure_socket.close()