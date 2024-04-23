import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
import hashlib
import ssl

bgColor = "#FFE6E6"
fontColor = "#7469B6"
buttonColor = "#E1AFD1"

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Helvetica', 12, 'bold'), fg=fontColor, bg=bgColor).grid(row = 1, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,voter_ID,password):
    # Hash the password entered by the user
    hashed_password = hash_password(password)
    
    # Construct message to send to the server (voter_ID and hashed_password)
    message = f"{voter_ID} {hashed_password}"
    
    # Wrap the client socket with SSL/TLS
    ssl_client_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLS)
    
    # Send message to the server
    ssl_client_socket.send(message.encode())
    
    # Receive authentication response from the server
    authentication_response = ssl_client_socket.recv(1024).decode()
    
    # Determine how to proceed based on the authentication response
    if authentication_response == "Authenticate":
        votingPg(root, frame1, client_socket)
    elif authentication_response == "VoteCasted":
        message = "Vote has Already been Cast"
        failed_return(root,frame1,client_socket,message)
    elif authentication_response == "InvalidVoter":
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)
    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)


def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Voter Login", font=('Helvetica', 18, 'bold'), fg=fontColor, bg=bgColor).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="", fg=fontColor, bg=bgColor).grid(row = 1,column = 0)
    Label(frame1, text="Voter ID:      ", fg=fontColor, bg=bgColor, anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:   ", fg=fontColor, bg=bgColor, anchor="e", justify=LEFT).grid(row = 3,column = 0)

    voter_ID = tk.StringVar()
    name = tk.StringVar()
    password = tk.StringVar()
    

    e1 = Entry(frame1, textvariable = voter_ID)
    e1.grid(row = 2,column = 2)
    e3 = Entry(frame1, textvariable = password, show = '*')
    e3.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=10, bg=buttonColor, fg=fontColor, command = lambda: log_server(root, frame1, client_socket, voter_ID.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()

def hash_password(password):
    # Encode password as bytes before hashing
    password_bytes = password.encode('utf-8')
    # Use SHA-256 hash function
    hashed_password = hashlib.sha512(password_bytes).hexdigest()
    return hashed_password


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         voterLogin(root,frame1)
