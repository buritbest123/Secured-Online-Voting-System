import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

bgColor = "#FFE6E6"
fontColor = "#7469B6"
buttonColor = "#E1AFD1"

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold'), fg=fontColor, bg=bgColor).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold'), fg=fontColor, bg=bgColor).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold'), fg=fontColor, bg=bgColor).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="", fg=fontColor, bg=bgColor).grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "EarthPony\nMeadowbrook", fg=fontColor, bg=buttonColor, variable = vote, value = "EarthPony", indicator = 0, height = 2, width=15, command = lambda: voteCast(root,frame1,"EarthPony",client_socket)).grid(row = 2,column = 1)
    electionCandidate1 = ImageTk.PhotoImage((Image.open("img/EarthPony.png")).resize((45,45),Image.LANCZOS))
    EarthPonyImg = Label(frame1, image=electionCandidate1, bg=bgColor).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Pegasus\nSkydancer", fg=fontColor, bg=buttonColor, variable = vote, value = "Pegasus", indicator = 0, height = 2, width=15, command = lambda: voteCast(root,frame1,"Pegasus",client_socket)).grid(row = 3,column = 1)
    electionCandidate2 = ImageTk.PhotoImage((Image.open("img/Pegasus.png")).resize((35,48),Image.LANCZOS))
    PegasusImg = Label(frame1, image=electionCandidate2, bg=bgColor).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Unicorn\nStarwhisper", fg=fontColor, bg=buttonColor, variable = vote, value = "Unicorn", indicator = 0, height = 2, width=15, command = lambda: voteCast(root,frame1,"Unicorn",client_socket) ).grid(row = 4,column = 1)
    electionCandidate3 = ImageTk.PhotoImage((Image.open("img/Unicorn.png")).resize((55,40),Image.LANCZOS))
    UnicornImg = Label(frame1, image=electionCandidate3, bg=bgColor).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Alicorn\nCelestiaDream", fg=fontColor, bg=buttonColor, variable = vote, value = "Alicorn", indicator = 0, height = 2, width=15, command = lambda: voteCast(root,frame1,"Alicorn",client_socket)).grid(row = 5,column = 1)
    electionCandidate4 = ImageTk.PhotoImage((Image.open("img/Alicorn.png")).resize((50,45),Image.LANCZOS))
    AlicornImg = Label(frame1, image=electionCandidate4, bg=bgColor).grid(row = 5,column = 0)

    # Radiobutton(frame1, text = "\nNOTA    \n  ", fg=fontColor, bg=buttonColor, variable = vote, value = "nota", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket)).grid(row = 6,column = 1)
    # electionCandidate5 = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((45,35),Image.LANCZOS))
    # notaImg = Label(frame1, image=electionCandidate5, bg=bgColor).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
