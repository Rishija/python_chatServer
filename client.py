import socket, sys, threading, getpass, os, pickle



#Helper function (formatting)
def display() :
	you="\33[33m\33[1m"+" You: "+"\33[0m"
	sys.stdout.write(you)
	sys.stdout.flush()


if len(sys.argv)<2:
    host = input("Enter host ip address: ")
else:
    host = sys.argv[1]

port = 5003
    
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

def send():
    while True:
        try:
            sys.stdout.write(f"\033[1;32m{name} (me): \033[0m \033[;1m"); sys.stdout.flush()
            message = input()
                
            s.send(pickle.dumps((name, message)))
        except:
            print("Error while Sending!")

def receive():
    while True:
        try:
            msg = s.recv(1024)
            USER, MESSAGE = pickle.loads(msg)

            if (USER == name):

                print(f"\nYou: {MESSAGE}")
            #sys.stdout.write(f"\033[1;32m{name} (me): \033[0m \033[;1m"); sys.stdout.flush()
            else:
                sys.stdout.write(f"\033[1;32m {USER}: \033[0m \033[;1m"); sys.stdout.flush()
        except:
            break
send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)

send_thread.start()
receive_thread.start()
