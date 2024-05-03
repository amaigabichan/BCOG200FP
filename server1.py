import tkinter as tk
import socket
from Crypto.Cipher import AES
import secrets

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Chat App")

        self.key = b'\xd6\x13\x93\xf0T\xec\x82\x03\xdeV.\xf0dEI\n\xf83\xf1\xdb\x8c\xee\xad\x02\xa8\x05\x12:\xb9\x8c\xd2\xde'
        self.iv = b'\\\xee\x8f%\xd9\x8d\x9d\xcb\xa1\xccf\xf5\x04l\xea`'
        self.receiver_address = ("192.1.168.151", 12345)

        self.setup_socket()

        self.setup_gui()

    def setup_socket(self):
        self.socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip0 = input("Type in your IPV4 address: ")
        self.ip = input("Type the client IPV4 address: ")
        self.receiver_address = (self.ip, 12345)

        self.socket1.bind((self.ip0, 12346))
        self.socket1.settimeout(20.0)

    def setup_gui(self):
        self.msg_label = tk.Label(self.root, text="Enter message:")
        self.msg_label.pack()

        self.msg_entry = tk.Entry(self.root)
        self.msg_entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.msg_display = tk.Text(self.root, height=10, width=50)
        self.msg_display.pack()

    def send_message(self):
        message = self.msg_entry.get()
        encrypted_msg = self.encrypt_message(message)
        self.msg_display.insert(tk.END, f"Sent: {message}\n")
        self.send_udp_message(encrypted_msg)
       

    def encrypt_message(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_text = self.pad_text(plaintext)
        encrypted_bytes = cipher.encrypt(padded_text)
        return encrypted_bytes

    def pad_text(self, text, block_size=16):
        padding_length = block_size - (len(text) % block_size)
        padding = bytes([0x20]) * padding_length
        padded_text = text.encode() + padding
        return padded_text

    def send_udp_message(self, message):
        self.socket1.sendto(message, self.receiver_address)
        try:
            response, _ = self.socket1.recvfrom(1024)
            decrypted_msg = self.decrypt_message(response)
            self.msg_display.insert(tk.END, f"Received: {decrypted_msg}\n")
        except socket.timeout:
            self.msg_display.insert(tk.END, "No response received.\n")

    def decrypt_message(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_bytes = cipher.decrypt(ciphertext)
        decrypted_text = decrypted_bytes.decode().rstrip('\x00')
        return decrypted_text

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
