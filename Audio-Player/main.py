import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

root = Tk()
root.title("Audio Player By AP")
root.geometry("500x650")  
root.configure(bg="#f0f0f0")

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root, textvariable=v, width=35, bg="#f0f0f0", font=("Arial", 12, "bold"))

index = 0

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    v.set(realnames[index])

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def unpausesong(event):
    pygame.mixer.music.unpause()
    v.set("Song unpaused")

def pausesong(event):
    pygame.mixer.music.pause()
    v.set("Song paused")

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

label = Label(root, text='Music Player', bg="#f0f0f0", font=("Arial", 20, "bold"))
label.pack(pady=10)

listbox = Listbox(root, bg="#fff", fg="#000", width=50, height=10)
listbox.pack()

for items in realnames:
    listbox.insert(0, items)

nextbutton = Button(root, text='⏩', bg="#008CBA", fg="#fff", width=10, font=("Arial", 16, "bold"), pady=4)
nextbutton.pack(pady=5)

previousbutton = Button(root, text='⏪', bg="#008CBA", fg="#fff", width=10, font=("Arial", 16, "bold"), pady=4)
previousbutton.pack(pady=5)

pausebutton = Button(root, text='||', bg="#008CBA", fg="#fff", width=10, font=("Arial", 16, "bold"), pady=4)
pausebutton.pack(pady=5)

unpausebutton = Button(root, text='▷', bg="#008CBA", fg="#fff", width=10, font=("Arial", 16, "bold"), pady=4)
unpausebutton.pack(pady=5)

stopbutton = Button(root, text='◼️', bg="#008CBA", fg="#fff", width=10, font=("Arial", 16, "bold"), pady=4)
stopbutton.pack(pady=5)

nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
pausebutton.bind("<Button-1>", pausesong)
unpausebutton.bind("<Button-1>", unpausesong)
stopbutton.bind("<Button-1>", stopsong)

songlabel.pack()
root.mainloop()
