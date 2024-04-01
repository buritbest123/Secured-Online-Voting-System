import socket
import threading
import dframe as df
from threading import Thread
from dframe import *
from encryption import encrypt_file, decrypt_file 

lock = threading.Lock()

def client_thread(connection):
    data = connection.recv(1024)  # receiving voter details
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    
    if df.verify(log[0], log[1]):  # Authenticate
        if df.isEligible(log[0]):
            print('Voter Logged in... ID:'+str(log[0]))
            connection.send("Authenticate".encode())
            
            data = connection.recv(1024)  # Get Vote
            print("Vote Received from ID: "+str(log[0])+"  Processing...")
            lock.acquire()
            # update Database
            if df.vote_update(data.decode(), log[0]):
                print("Vote Casted Successfully by voter ID = "+str(log[0]))
                connection.send("Successful".encode())
            else:
                print("Vote Update Failed by voter ID = "+str(log[0]))
                connection.send("Vote Update Failed".encode())
            lock.release()
        else:
            print('Vote Already Cast by ID:'+str(log[0]))
            connection.send("VoteCasted".encode())
    else:
        print('Invalid Voter')
        connection.send("InvalidVoter".encode())

    connection.close()


def voting_Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())   ### 1
        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
