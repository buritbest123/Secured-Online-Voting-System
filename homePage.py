# Tingting run: python -u "c:\Users\Ramita\Downloads\Wireless\ITCS461-Online-Voting-System\homePage.py"
import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin
from tkinter import Button, font

buttonColor = "#58A399"
bgColor = "#496989"
fontColor = "#FFFFFF"



def Home(root, frame1, frame2):

    custom_font = font.Font(family="Helvetica", size=12, weight="bold")

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()
    
    Button(frame2, text="Home", command = lambda: Home(root, frame1, frame2), fg=fontColor, bg=buttonColor).grid(row=0,column=0)
    Label(frame2, text="                                                                         ", bg=bgColor).grid(row = 0,column = 1)
    Label(frame2, text="                                                                         ", bg=bgColor).grid(row = 0,column = 2)
    Label(frame2, text="         ", bg=bgColor).grid(row = 1,column = 1)
    frame2.pack(side=TOP)
    frame2.configure(bg=bgColor)

    root.title("Home")
    root.configure(bg=bgColor)

    Label(frame1, text="Home", font=('Helvetica', 25, 'bold'), fg=fontColor, bg=bgColor).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="", bg=bgColor).grid(row = 1,column = 0)
    #Admin Login
    admin = Button(frame1, text="Admin Login", width=15, command=lambda: AdmLogin(root, frame1), font=custom_font, fg=fontColor, bg=buttonColor)

    #Voter Login
    voter = Button(frame1, text="Voter Login", width=15, command = lambda: voterLogin(root, frame1), font=custom_font, fg=fontColor, bg=buttonColor)

    #New Tab
    newTab = Button(frame1, text="New Window", width=15, command = lambda: sb_p.call('start python homePage.py', shell=True), font=custom_font, fg=fontColor, bg=buttonColor)

    Label(frame1, text="", bg=bgColor).grid(row = 2,column = 0)
    Label(frame1, text="", bg=bgColor).grid(row = 4,column = 0)
    Label(frame1, text="", bg=bgColor).grid(row = 6,column = 0)
    admin.grid(row = 3, column = 1, columnspan = 2)

    voter.grid(row = 5, column = 1, columnspan = 2)
    newTab.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    frame2 = Frame(root)
    root.configure(bg=bgColor)
    frame1.configure(bg=bgColor)
    frame2.configure(bg=bgColor)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()