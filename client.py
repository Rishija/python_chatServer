import socket, select, string, sys
import socket, sys, threading, getpass, os, pickle
from datetime import datetime


#Helper function (formatting)
def display() :
	you="\33[33m\33[1m"+" You: "+"\33[0m"
	sys.stdout.write(you)
	sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        host = raw_input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port = 5000
    
    #asks for user name
    name=input("\33[34m\33[1m CREATING NEW ID:\n Enter username: \33[0m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    # connecting host
    try :
        s.connect((host, port))
    except :
        print("\33[31m\33[1m Can't connect to the server \33[0m")
        sys.exit()

    #if connected
    s.send(name.encode('utf-8'))
    display()

    def send():
        while True:
            try:
                sys.stdout.write(f"\033[1;32m{user} (me): \033[0m \033[;1m"); sys.stdout.flush()
                message = input()
                
                c.send(pickle.dumps((user, message)))
            except:
                print("Error while Sending!")

    def receive():
        while True:
            try:
                msg = c.recv(1024)
                USER, MESSAGE = pickle.loads(msg)

                print(f"\n{USER}: {MESSAGE}")
                sys.stdout.write(f"\033[1;32m{user} (me): \033[0m \033[;1m"); sys.stdout.flush()
            except:
                break
        

    send_thread = threading.Thread(target=send)
    receive_thread = threading.Thread(target=receive)


    send_thread.start()
    receive_thread.start()
'''
    while 1:
        socket_list = [sys.stdin, s]
        
        # Get the list of sockets which are readable
        rList, wList, error_list = select.select(socket_list , [], [])
        
        for sock in rList:
            #incoming message from server
            if sock == s:
                data = sock.recv(4096).decode('utf-8')
                if not data :
                    print('\33[31m\33[1m \rDISCONNECTED!!\n \33[0m')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    display()
        
            #user entered a message
            else :
                msg=sys.stdin.readline()
                s.send(msg.encode('utf-8'))
                display()
'''

if __name__ == "__main__":
    main()
