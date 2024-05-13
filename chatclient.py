import tkinter as tk
import socket
import threading
import time
from Crypto.Cipher import AES
import secrets

class ChatAppClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Chat Client")

        self.key = b'\xd6\x13\x93\xf0T\xec\x82\x03\xdeV.\xf0dEI\n\xf83\xf1\xdb\x8c\xee\xad\x02\xa8\x05\x12:\xb9\x8c\xd2\xde'
        self.iv = b'\\\xee\x8f%\xd9\x8d\x9d\xcb\xa1\xccf\xf5\x04l\xea`'

        self.setup_socket()

        self.setup_gui()

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True  # Daemonize the thread
        self.receive_thread.start()

    def setup_socket(self):
        self.socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip0 = input("Type in your IPV4 address: ")
        self.ip = input("Type the client IPV4 address: ")
        self.port= int(input("What port do you want to listen through? (pick a number 1200-65536 if you get an error without the GUI opening, try again and pick an unused port) "))
        self.port1= int(input("Which port do you want to talk through? (must be the listening port used on the other device) "))
        self.socket2.bind((self.ip0, self.port))
        
        self.socket2.settimeout(2.0)  # 2 seconds timeout for receiving messages

    def setup_gui(self):
        self.msg_display = tk.Text(self.root, height=10, width=50)
        self.msg_display.pack()

        self.msg_label = tk.Label(self.root, text="Enter message:")
        self.msg_label.pack()

        self.msg_entry = tk.Entry(self.root)
        self.msg_entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

    def receive_messages(self):
        while 1:
            try:
                message, sender_address = self.socket2.recvfrom(1024)
                decrypted_msg = self.decrypt_message(message)
                self.msg_display.insert(tk.END, f"Received: {decrypted_msg}\n")
            except socket.timeout:
                time.sleep(2)  # Continue waiting for messages


    def send_message(self):
        message = self.msg_entry.get()
        encrypted_msg = self.encrypt_message(message)
        self.socket2.sendto(encrypted_msg, (self.ip, self.port1))  # Assuming receiver's address and port
        self.msg_display.insert(tk.END, f"Sent: {message}\n")
        self.msg_entry.delete(0, tk.END)  # Clear the input field after sending

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

    def decrypt_message(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_bytes = cipher.decrypt(ciphertext)
        decrypted_text = decrypted_bytes.decode().rstrip('\x00')
        return decrypted_text

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatAppClient(root)
    root.mainloop()
