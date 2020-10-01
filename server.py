import socket, threading, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5003
SERVER = socket.gethostbyname(socket.gethostname())
s.bind((SERVER, PORT))

users = []

#Function to send message to all connected clients
def client(client_socket, addr, USER):
    while True:
        try:
            msg = client_socket.recv(1024)
            user , message = pickle.loads(msg)

            for client in users:
                client.send(pickle.dumps((user,message)))        
                   
        except:
            print("Brute force close")
            
                
def threads():
    s.listen()
    while True:
        try:
            client_socket, addr = s.accept()
            user = client_socket.recv(1024).decode('utf-8')

            
            users.append(client_socket)
                        
            thread = threading.Thread(target=client, args=(client_socket, addr, user))
            thread.start()
        
        except:
            s.close()
            
print("\033[1;32m[STARTING] Server!\033[0m \033[;1m")
threads()
