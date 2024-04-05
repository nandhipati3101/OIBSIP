import socket
import threading

host = "127.0.0.1"
port = 1234


def listen_messages(client):
    while True:
        try:
            message = client.recv(2048).decode("UTF-8")
            if message != "":
                print(message)
            else:
                print("The message from the server is empty")
        except Exception as e:
            print(f"Error listening to messages from the server: {e}")
            break


def send_messages(client):
    while True:
        try:
            message = input("Message: ")
            if message != "":
                client.sendall(message.encode())
            else:
                print("Empty message")
                break
        except Exception as e:
            print(f"Error sending message to the server: {e}")
            break


def communication(client):
    try:
        username = input("Enter the username: ")
        if username != "":
            client.sendall(username.encode())
        else:
            print("Please enter the username")
            return

        threading.Thread(target=listen_messages, args=(client,)).start()
        send_messages(client)

    except Exception as e:
        print(f"Error in communication: {e}")


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        print("Successfully connection takes place")
    except Exception as e:
        print(f"Unable to connect to the server: {e}")
        return

    communication(client)


if __name__ == "__main__":
    main()