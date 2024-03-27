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
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
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

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.LANCZOS))
    bjpImg = Label(frame1, image=bjpLogo, bg=bgColor).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25,38),Image.LANCZOS))
    congImg = Label(frame1, image=congLogo, bg=bgColor).grid(row = 3,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45,30),Image.LANCZOS))
    aapImg = Label(frame1, image=aapLogo, bg=bgColor).grid(row = 4,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40,35),Image.LANCZOS))
    ssImg = Label(frame1, image=ssLogo, bg=bgColor).grid(row = 5,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25),Image.LANCZOS))
    notaImg = Label(frame1, image=notaLogo, bg=bgColor).grid(row = 6,column = 0)


    Label(frame1, text="BJP              :       ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" AAP               :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" Shiv Sena    :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" NOTA            :          ", fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], fg=fontColor, bg=bgColor, font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
