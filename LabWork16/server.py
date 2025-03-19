import socket
from datetime import datetime


def start_server():
    HOST = ''  # Прослушивание всех интерфейсов
    PORT = 50007  # Порт сервера

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Сервер запущен и ожидает подключений...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Подключение от {addr}")
        login = conn.recv(1024).decode('utf-8')
        print(f"{login} подключился")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            timestamp = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
            print(f"{timestamp} {login}: {message}")
        conn.close()


if __name__ == "__main__":
    start_server()