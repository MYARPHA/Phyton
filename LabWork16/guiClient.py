import socket
import tkinter as tk


def send_message():
    message = message_entry.get()
    if message:
        client_socket.sendall(message.encode('utf-8'))
        message_entry.delete(0, tk.END)


def start_gui_client():
    global client_socket, message_entry

    HOST = 'localhost'
    PORT = 50007

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    root = tk.Tk()
    root.title("Чат клиент")

    tk.Label(root, text="Введите сообщение:").pack()
    message_entry = tk.Entry(root)
    message_entry.pack()
    tk.Button(root, text="Отправить", command=send_message).pack()

    root.mainloop()
    client_socket.close()


if __name__ == "__main__":
    start_gui_client()
