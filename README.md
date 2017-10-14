## About 
This is a simple multi-client chat server using `sockets` written in `python`. 

The server asks for username when user wants to join the chatroom and accepts the connection only if the username is unique. It then broadcasts the message from one client to all other clients connected. Also informs about the entry/exit of any client.

## Download
Run the following command in your terminal to save the repository in your system
> $ git clone https://github.com/Rishija/python_chatServer.git

## Run
Once you are in the directory where `server.py` or `client.py` file exists, run by typing the following commands in your terminal.

### Server
> $ python server.py

### Client
> $ python client.py hostname

#### Example
For server and client running on the same system

**Server**
> $ python server.py
<pre>
				SERVER WORKING 
Client (127.0.0.1, 51638) connected  [ tesla ]
Client (127.0.0.1, 51641) connected  [ albert ]
Client (127.0.0.1, 51641) is offline  [ albert ]
</pre>



**Client 1**
> $ python client.py localhost

<pre>
CREATING NEW ID:
Enter username: tesla
Welcome to chat room. Enter 'tata' anytime to exit
You: Hello
albert joined the conversation 
albert: world
albert left the conversation
You:
</pre>

**Client 2**
> $ python client.py localhost
<pre>
CREATING NEW ID:
Enter username: albert
Welcome to chat room. Enter 'tata' anytime to exit
You: World
You: tata
DISCONNECTED!!
</pre>