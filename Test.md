First, run server1.py type in localhost/source ip when prompted for the first input,  then type the localhost/destination ip.

Second, in a separate terminal, run server2.py, then type in the destination ip you wrote for the first step as well as that source ip. 

Finally, switch back to the first terminal, and type your message to send a message through the TCP pipe while switching with the second terminal to send messages to yourself. Additionally, you can test this with a friend where you are on separate computers and your friend runs "server2.py" and you run "server1.py" with a similar test.

As messages could not display without having a working TCP connection, it is evident that that portion works. Additionally, as an encryption decryption scheme, such as AES, needs both ends to properly decrypt and encrypt to have comprehensible text, that portion also works.

You can take the code for encryption and decryption from the code alongside the key generation in order to verify that they work to encrypt and decrypt data. This has already been done within development, so testing this is not urgent for future development.

#NOTE: pycryptodome is a required library to be installed before running! Intall it with
```
pip install pycryptodome
```
# UPDATED INSTRUCTIONS FOR TESTING

1. Open two command line interfaces

2. Change the directory to the folder containing the Python file (chatclient.py)

3. On one command prompt run this:
python chatclient.py

Type in your IPV4 address: 127.0.0.1
Type the client IPV4 address: 127.0.0.1
What port do you want to listen through? (pick a number 1200-65536 if you get an error without the GUI opening, try again and pick an unused port) 6001
Which port do you want to talk through? (must be the listening port used on the other device) 6000



4. On another command prompt run this:

python chatclient.py
Type in your IPV4 address: 127.0.0.1
Type the client IPV4 address: 127.0.0.1
What port do you want to listen through? (pick a number 1200-65536 if you get an error without the GUI opening, try again and pick an unused port) 6000
Which port do you want to talk through? (must be the listening port used on the other device) 6001
