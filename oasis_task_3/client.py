import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    while True:
        try:
            message = input("Enter your message: ")
            if not message:
                print("Exiting client")
                break
            client_socket.send(message.encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8")
            print(f"Response from server: {response}")
        except Exception as e:
            print(f"Error occurred: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
