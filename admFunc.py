import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

# Modern color scheme and fonts
buttonColor = "#E1AFD1"
bgColor = "#FFE6E6"
fontColor = "#7469B6"

def resetAll(root,frame1):
    df.count_reset()
    # df.reset_voter_list()
    # df.reset_cand_list()
    Label(frame1, text="", fg=fontColor, bg=bgColor).grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", fg=fontColor, bg=bgColor, width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", fg=fontColor, bg=bgColor, font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="", fg=fontColor, bg=bgColor).grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    # bjp => EarthPony
    # cong => Pegasus
    # aap => Unicorn
    # ss => Alicorn

    electionCandidate1 = ImageTk.PhotoImage((Image.open("img/EarthPony.png")).resize((35,35),Image.LANCZOS))
    EarthPonyImg = Label(frame1, image=electionCandidate1, bg=bgColor).grid(row = 2,column = 0)

    electionCandidate2 = ImageTk.PhotoImage((Image.open("img/Pegasus.png")).resize((25,38),Image.LANCZOS))
    PegasusImg = Label(frame1, image=electionCandidate2, bg=bgColor).grid(row = 3,column = 0)

    electionCandidate3 = ImageTk.PhotoImage((Image.open("img/Unicorn.png")).resize((45,30),Image.LANCZOS))
    UnicornImg = Label(frame1, image=electionCandidate3, bg=bgColor).grid(row = 4,column = 0)

    electionCandidate4 = ImageTk.PhotoImage((Image.open("img/Alicorn.png")).resize((40,35),Image.LANCZOS))
    AlicornImg = Label(frame1, image=electionCandidate4, bg=bgColor).grid(row = 5,column = 0)

    # electionCandidate5 = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.LANCZOS))
    # notaImg = Label(frame1, image=electionCandidate5, bg=bgColor).grid(row = 6,column = 0)


    Label(frame1, text=" Meadowbrook           :       ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['EarthPony'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Skydancer              :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['Pegasus'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" Starwhisper            :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['Unicorn'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" CelestiaDream         :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['Alicorn'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    # Label(frame1, text=" NOTA            :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    # Label(frame1, text=result['nota'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
