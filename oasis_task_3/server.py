import socket
import threading

def handle_client(client_socket, client_addr):
    print(f"New connection from {client_addr}")
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                print(f"Connection with {client_addr} closed")
                break
            print(f"Received message from {client_addr}: {data}")
            client_socket.send("Message received by server".encode("utf-8"))
        except Exception as e:
            print(f"Error occurred for {client_addr}: {e}")
            break
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 5555))
    server_socket.listen(5)

    print("Server is listening on port 5555")

    while True:
        try:
            client_socket, client_addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
            client_thread.start()
        except Exception as e:
            print(f"Error occurred while accepting connection: {e}")
            break

    server_socket.close()

if __name__ == "__main__":
    main()
