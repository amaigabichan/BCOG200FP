# BCOG200_FinalProject by gh14
# A Peer to Peer AES Encrypted TCP Messaging Platform
## Project Description:
1. The project aims to implement two servers for text communication using Python. These servers will communicate with each other through TCP (Transmission Control Protocol) and encrypt their messages using the AES (Advanced Encryption Standard) encryption algorithm. This will ensure secure communication between the servers, maintaining confidentiality of the transmitted data. Additionally, a graphical user interface (GUI) will be provided for user interaction to have a more user friendly feel.

## Functions (included one more):

1. `__init__(self, root)`: 
    - Constructor method that initializes the chat application.
    - Sets up the GUI, initializes the socket, and starts a thread to receive messages.

2. `setup_socket(self)`:
    - Initializes a UDP socket for communication.
    - Binds the socket to a specific IP address and port.
    - Sets a timeout for receiving messages.

3. `setup_gui(self)`:
    - Creates the graphical user interface (GUI) for the chat application.
    - Creates a text box to display messages, an entry field to type messages, and a send button.

4. `receive_messages(self)`:
    - Continuously listens for incoming messages on the socket.
    - Decrypts and displays received messages in the GUI.

5. `send_message(self)`:
    - Gets the message from the entry field in the GUI.
    - Encrypts the message using AES.
    - Sends the encrypted message to the specified IP address and port using UDP.
    - Inserts the sent message into the GUI and clears the entry field.

6. `encrypt_message(self, plaintext)`:
    - Encrypts the given plaintext message using AES encryption in CBC mode.
    - Adds padding to the plaintext to ensure it's a multiple of the block size.

7. `pad_text(self, text, block_size=16)`:
    - Adds padding to the given text to ensure it's a multiple of the block size.

8. `decrypt_message(self, ciphertext)`:
    - Decrypts the given ciphertext message using AES decryption in CBC mode.
    - Removes any padding added during encryption.
  
## Updates/Documentation
The project aims to implement two servers for text communication using Python. These servers will communicate with each other through TCP (Transmission Control Protocol) and encrypt their messages using the AES (Advanced Encryption Standard) encryption algorithm. This will ensure secure communication between the servers, maintaining confidentiality of the transmitted data. Additionally, a graphical user interface (GUI) was provided for user interaction to have a more user friendly feel.

This is the completed functionality from the proposed project in command line and end-to-end encryption and communication has been achieved. As messages could not display without having a working TCP connection, it is evident that that portion works. Additionally, as an encryption decryption scheme, such as AES, needs both ends to properly decrypt and encrypt to have comprehensible text, that portion also works.

**Port Inclusion**: Added a port variable to specify the listening port for the client. This allows the client to listen for incoming messages on a specific port. This change enhances the functionality of the project by enabling communication through a defined port, ensuring that messages are received on the correct channel. It aligns with the project's aim of implementing secure communication between the servers while maintaining confidentiality of the transmitted data.

**Server1 Removal**: Since you're now using a client-to-client communication model, there's no need for a dedicated server (Server1). Each client acts as both a sender and receiver. This simplifies the architecture of the system, making it more efficient and suitable for peer-to-peer communication, which aligns with the project's objective of implementing a peer-to-peer messaging platform. Removal of Server1 also eliminates potential single points of failure, enhancing the robustness of the system.

**Clarification in Instructions**: Updated the instructions to make it clearer for users to understand. Specifically, added prompts for entering the IPv4 address and listening port, making it easier for users to configure the client. This enhancement improves user experience by providing clear instructions for setting up and using the application, aligning with the goal of creating a user-friendly GUI for intuitive interaction with the servers. Additionally, a note is added to inform users about the requirement of installing the pycryptodome library before running the program, ensuring smooth execution of the encryption and decryption functionalities.

#NOTE: pycryptodome is a required library to be installed before running! Intall it with
```
pip install pycryptodome
```

# UPDATED INSTRUCTIONS FOR TESTING

1. Open two command line interfaces
2. Change the directory to the folder containing the Python file (*chatclient.py*)
3. On one command prompt run this:
python chatclient.py
Type in your IPV4 address: 127.0.0.1
Type the client IPV4 address: 127.0.0.1
What port do you want to listen through? (pick a number 1200-65536 if you get an error without the GUI opening, try again and pick an unused port) 6001
Which port do you want to talk through? (must be the listening port used on the other device) 6000

5. On another command prompt run this:
python chatclient.py
Type in your IPV4 address: 127.0.0.1
Type the client IPV4 address: 127.0.0.1
What port do you want to listen through? (pick a number 1200-65536 if you get an error without the GUI opening, try again and pick an unused port) 6000
Which port do you want to talk through? (must be the listening port used on the other device) 6001
