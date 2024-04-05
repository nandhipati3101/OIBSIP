import socket
import threading

host = "127.0.0.1"
port = 1234
limit = 5
active_clients = []


def listen_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode("UTF-8")
            if message != "":
                final_msg = f"[{username}]: {message}"
                send_messages(final_msg)
            else:
                print("The message from client is empty")
        except Exception as e:
            print(f"Error listening to messages from {username}: {e}")
            break


def send_message_to_client(client, message):
    try:
        client.sendall(message.encode())
    except Exception as e:
        print(f"Error sending message to client: {e}")


def send_messages(message):
    for user in active_clients:
        send_message_to_client(user[1], message)


def client_handling(client):
    while True:
        try:
            username = client.recv(2048).decode("UTF-8")
            if username != "":
                active_clients.append((username, client))
                break
            else:
                print("Username is empty")
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    threading.Thread(target=listen_messages, args=(client, username)).start()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((host, port))
        print(f"Running the server on port {port} and host {host}")
    except Exception as e:
        print(f"Unable to bind the host and the server: {e}")
        return

    server.listen(limit)
    while True:
        try:
            client, address = server.accept()
            print("Successfully connection takes place")
            threading.Thread(target=client_handling, args=(client,)).start()
        except Exception as e:
            print(f"Error accepting client connection: {e}")

if __name__ == "__main__":
    main()
