import socket
from Crypto.Cipher import AES
import secrets
Key = b'\xd6\x13\x93\xf0T\xec\x82\x03\xdeV.\xf0dEI\n\xf83\xf1\xdb\x8c\xee\xad\x02\xa8\x05\x12:\xb9\x8c\xd2\xde'
IV = b'\\\xee\x8f%\xd9\x8d\x9d\xcb\xa1\xccf\xf5\x04l\xea`'

#Keys and Initialization Vector were written using the following functions
def generate_aes_key(key_size=32):
    return secrets.token_bytes(key_size)

def generate_aes_iv():
    return secrets.token_bytes(16)  # IV length is always 16 bytes for AES

def encrypt_aes_cbc(plaintext, key=Key, iv=IV):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()  # Convert string to bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad_text(plaintext)  # Ensure padded text is bytes
    encrypted_bytes = cipher.encrypt(padded_text)
    return encrypted_bytes

def pad_text(text, block_size=16):
    padding_length = block_size - (len(text) % block_size)
    padding = bytes([0x20]) * padding_length  # Create padding bytes
    padded_text = text + padding
    return padded_text

def decrypt_aes_cbc(ciphertext, key=Key, iv=IV):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(ciphertext)
    decrypted_text = decrypted_bytes.decode()
    return decrypted_text

def main():
    # Create a UDP socket
    socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip0 = input("Input your IP address:")
    ip = input("Input your target IP address:")
    # Receiver's address and port (System 1)
    receiver_address = (ip, 12346)

    # Bind the socket to a port for receiving messages
    socket2.bind((ip0, 12345))

    # Set a timeout for receiving messages
    socket2.settimeout(20.0)  # 20 seconds

    try:
        while True:
            # Receive message from System 1
            message, sender_address = socket2.recvfrom(1024)
            print("System 1:", decrypt_aes_cbc(message))

            # Reply to System 1
            reply = input("System 2: Enter reply : ")

            if reply.lower() == 'exit':
                break

            # Send the reply back to System 1
            socket2.sendto(encrypt_aes_cbc(reply), sender_address)
    except socket.timeout:
        print("System 1 did not send any message.")
        socket2.close()

if __name__ == "__main__":
    main()
