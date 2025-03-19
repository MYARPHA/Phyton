import socket

def start_client():
    HOST = 'localhost'
    PORT = 50007

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    login = input("Введите ваш логин: ")
    client_socket.sendall(login.encode('utf-8'))

    while True:
        message = input("Введите сообщение (или 'end' для выхода): ")
        if message.lower() == 'end':
            break
        client_socket.sendall(message.encode('utf-8'))

    client_socket.close()


if __name__ == "__main__":
    start_client()