First, run server1.py type in localhost/source ip when prompted for the first input,  then type the localhost/destination ip.

Second, in a separate terminal, run server2.py, then type in the destination ip you wrote for the first step as well as that source ip. 

Finally, switch back to the first terminal, and type your message to send a message through the TCP pipe while switching with the second terminal to send messages to yourself. Additionally, you can test this with a friend where you are on separate computers and your friend runs "server2.py" and you run "server1.py" with a similar test.

You can take the code for encryption and decryption from the code alongside the key generation in order to verify that they work to encrypt and decrypt data. This has already been done within development, so testing this is not important to future development.
