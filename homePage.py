# Tingting run: python -u "c:\Users\Ramita\Downloads\Wireless\ITCS461-Online-Voting-System\homePage.py"
import subprocess as sb_p
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from Admin import AdmLogin
from voter import voterLogin

# Modern color scheme and fonts
buttonColor = "#E1AFD1"
bgColor = "#FFE6E6"
fontColor = "#7469B6"
highlightColor = "#77cbb9"  # Highlight color for hover effect

# Code Color: https://colorhunt.co/palette/ffe6e6e1afd1ad88c67469b6
# Global variable to track if the logo is already displayed
logo_displayed = False
logo_image = None  # To store the PhotoImage object

def Home(root, frame1, frame2):
    global logo_displayed, logo_image
    custom_font = font.Font(family="Lato", size=12, weight="bold")

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()
            if not (widget is logo_image):
                widget.destroy()

    # Improved button style with hover effect
    home_btn = tk.Button(frame2, text="Home", command = lambda: Home(root, frame1, frame2), fg=fontColor, bg=buttonColor, font=custom_font)
    home_btn.grid(row=0, column=0)
    home_btn.bind("<Enter>", lambda e: home_btn.config(bg=highlightColor))
    home_btn.bind("<Leave>", lambda e: home_btn.config(bg=buttonColor))

    frame2.pack(side=tk.TOP, fill=tk.X, pady=10)
    frame2.configure(bg=bgColor)

    root.title("Home")
    root.configure(bg=bgColor)

    if not logo_displayed:
        # Logo
        original_image = Image.open('img\Logo.png')
        resized_image = original_image.resize((150, 150), Image.LANCZOS)  # Resize to 300x200 or your desired size
        image = ImageTk.PhotoImage(resized_image)

        # Create a label to display the image
        image_label = tk.Label(root, image=image, bg=bgColor)
        image_label.pack(padx=0, pady=0)
        logo_displayed = True

    tk.Label(frame1, text="Home", font=('Lato', 25, 'bold'), fg=fontColor, bg=bgColor).grid(row=0, column=1)

    # Buttons with modern styling
    admin_btn = tk.Button(frame1, text="Admin Login", width=15, font=custom_font, fg=fontColor, bg=buttonColor, command=lambda: AdmLogin(root, frame1))
    admin_btn.bind("<Enter>", lambda e: admin_btn.config(bg=highlightColor))
    admin_btn.bind("<Leave>", lambda e: admin_btn.config(bg=buttonColor))

    voter_btn = tk.Button(frame1, text="Voter Login", width=15, font=custom_font, fg=fontColor, bg=buttonColor, command=lambda: voterLogin(root, frame1))
    voter_btn.bind("<Enter>", lambda e: voter_btn.config(bg=highlightColor))
    voter_btn.bind("<Leave>", lambda e: voter_btn.config(bg=buttonColor))

    newTab_btn = tk.Button(frame1, text="New Window", width=15, font=custom_font, fg=fontColor, bg=buttonColor, command=lambda: sb_p.call('start python homePage.py', shell=True))
    newTab_btn.bind("<Enter>", lambda e: newTab_btn.config(bg=highlightColor))
    newTab_btn.bind("<Leave>", lambda e: newTab_btn.config(bg=buttonColor))

    admin_btn.grid(row=3, column=1, pady=10)
    voter_btn.grid(row=5, column=1, pady=10)
    newTab_btn.grid(row=7, column=1, pady=10)

    frame1.pack(expand=True)
    root.mainloop()

def new_home():
    root = tk.Tk()
    root.geometry('500x500')

    # Set the path to your custom icon file
    icon_path = "img/Icon.ico"

    # Check if the icon file exists before setting it
    try:
        root.iconbitmap(icon_path)
    except:
        print("Error: Could not set the icon.")

    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    root.configure(bg=bgColor)
    frame1.configure(bg=bgColor)
    frame2.configure(bg=bgColor)
    Home(root, frame1, frame2)



if __name__ == "__main__":
    new_home()