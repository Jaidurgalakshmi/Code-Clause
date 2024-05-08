import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 5555

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message)
        except:
            # Remove the client if it disconnects
            clients.remove(client_socket)
            break

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            # Remove the client if unable to send message
            clients.remove(client)

def start_server():
    print(f"Server is running on {HOST}:{PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
