# BCOG200_FinalProject by gh14
# A Peer to Peer AES Encrypted TCP Messaging Platform
## Project Description:
1. The project aims to implement two servers for text communication using Python. These servers will communicate with each other through TCP (Transmission Control Protocol) and encrypt their messages using the AES (Advanced Encryption Standard) encryption algorithm. This will ensure secure communication between the servers, maintaining confidentiality of the transmitted data. Additionally, a graphical user interface (GUI) will be provided for user interaction to have a more user friendly feel.

## Functions (included one more):
2a. `encrypt(message, key)`: This function will take a plaintext message and an encryption key as input, and encrypt the message using the AES encryption algorithm. It will return the encrypted message.

2b. `decrypt(ciphertext, key)`: This function will take an encrypted message and the corresponding decryption key as input, and decrypt the message using the AES decryption algorithm. It will return the decrypted plaintext message.

2c. `gui()`: This function will create a graphical user interface using a Python GUI library (e.g., Tkinter, PyQt, or Kivy) to provide an intuitive interface for users to interact with the servers. It will include features such as input fields for messages, buttons for sending and receiving messages, and display areas for the conversation history.

2d. `main()`: This function will serve as the entry point of the program. It will handle the initialization of the servers, establish connections between them, and manage the flow of communication. Additionally, it will invoke the GUI function to launch the graphical interface for user interaction.
