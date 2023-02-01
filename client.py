import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openChatWindow()

def openChatWindow():
    window=Tk()
    window.title('LAN Music Sharing')
    window.geometry("500x350")
    window.configure(bg = '#ccffee')
    
    photo = PhotoImage(file = "pause.png")
    photoimage = photo.subsample(7, 7)

    photo2 = PhotoImage(file = "play.png")
    photoimage2 = photo2.subsample(13, 13)

    photo3 = PhotoImage(file = "search.png")
    photoimage3 = photo3.subsample(4, 4)

    selectlabel = Label(window, text= "Select a Song:", bg = '#ccffee', font = ("Calibri",15))
    selectlabel.place(x=2, y=1)

    searchlabel = Label(window, text= "Or Search:", bg = '#ccffee', font = ("Calibri",15))
    searchlabel.place(x=300, y=1)

    searchbar  = Entry(window, bg = "white", font = ("Calibri", 10))
    searchbar.place(x= 300, y = 30)

    searchButton = Button(window, image = photoimage3, compound = CENTER)
    searchButton.place(x= 450, y = 30)

    listbox = Listbox(window,height=10, width=39, activestyle = 'dotbox', bg = '#ccffee', borderwidth=2, font = ("Calibri", 10))
    listbox.place(x=10,y=30)
    
    resultbox = Listbox(window,height=8, width=25, activestyle = 'dotbox', bg = '#ccffee', borderwidth=2, font = ("Calibri", 10))
    resultbox.place(x=300,y=50)
    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx = 1)
    scrollbar1.config(command=listbox.yview)

    scrollbar2 = Scrollbar(resultbox)
    scrollbar2.place(relheight=1, relx = 1)
    scrollbar2.config(command=resultbox.yview)

    playButton = Button(window, text="Play", bd= 1, bg= "#ddffee", font = ("Calibri",10), image = photoimage2, compound = LEFT)
    playButton.pack(side = TOP)
    playButton.place(x=30,y=220)
    
    Stop = Button(window, text= "Pause", bd=1, bg="#ddffee", font = ("Calibri", 10), image = photoimage, compound = LEFT)
    Stop.pack(side = TOP)
    Stop.place(x=200, y=220)
  
    Upload =Button(window, text="Upload", width=10, bd = 1, bg ='#ddffee', font = ("Calibri", 10))
    Upload.place(x=30, y=280)

    Download =Button(window, text="Download", width=10, bd = 1, bg ='#ddffee', font = ("Calibri", 10))
    Download.place(x=200, y=280)

    infoLabel = Label(window, text="PLACEHOLDER...", fg = "blue", font = ("Calibri", 8))
    infoLabel.place(x=50, y = 320)
    window.mainloop()

setup()