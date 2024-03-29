# BCOG200_FinalProject by gh14
# A Peer to Peer AES Encrypted TCP Messaging Platform
## Project Description:
1. The project aims to implement two servers for text communication using Python. These servers will communicate with each other through TCP (Transmission Control Protocol) and encrypt their messages using the AES (Advanced Encryption Standard) encryption algorithm. This will ensure secure communication between the servers, maintaining confidentiality of the transmitted data. Additionally, a graphical user interface (GUI) will be provided for user interaction to have a more user friendly feel.

## Functions (included one more):
2a. `encrypt_aes_cbc(plaintext, key=Key, iv=IV)`: This function takes a plaintext message and an encryption key as input, and encrypts the message using the AES encryption algorithm using a chain-block-cipher. It returns the encrypted message in bytes.

2b. `decrypt_aes_cbc(ciphertext, key=Key, iv=IV)`: This function takes an encrypted message and the corresponding decryption key as input, and decrypts the message using the AES decryption algorithm using a chain-block-cipher. It returns the decrypted plaintext message as a string.

2c. `gui()`: This function will create a graphical user interface using a Python GUI library (e.g., Tkinter, PyQt, or Kivy) to provide an intuitive interface for users to interact with the servers. It will include features such as input fields for messages, buttons for sending and receiving messages, and display areas for the conversation history.

2d. `main()`: This function servers as the entry point of the program. It handles the initialization of the servers, establishes connections between them, and manages the flow of communication. Additionally, it will invoke the GUI function to launch the graphical interface for user interaction.

2e. `pad_text(text, block_size=16)`: This function pads text to make sure the length is divisible by 16 bytes as is required by AES. It fills the padding characters with spaces, thus a 0x20 keycode. This is a helper function for encrypt_aes_cbc.

## Updates/Documentation
The project aims to implement two servers for text communication using Python. These servers will communicate with each other through TCP (Transmission Control Protocol) and encrypt their messages using the AES (Advanced Encryption Standard) encryption algorithm. This will ensure secure communication between the servers, maintaining confidentiality of the transmitted data. Additionally, a graphical user interface (GUI) will be provided for user interaction to have a more user friendly feel.

This is the completed functionality from the proposed project in command line, as other than the GUI, end-to-end encryption and communication has been achieved. As messages could not display without having a working TCP connection, it is evident that that portion works. Additionally, as an encryption decryption scheme, such as AES, needs both ends to properly decrypt and encrypt to have comprehensible text, that portion also works.

I must still complete the GUI. I want to add functions/functionality to change keys and initialization vectors through a handshake process to add additional security which may cause difficulties in the future. Additionally, I want to be able to send files possibly.

#NOTE: pycryptodome is a required library to be installed before running! Intall it with
```
pip install pycryptodome
```
