import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path

song_counter ={}
listbox ={}


from playsound import playsound
import pygame
from pygame import mixer

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client"  : client,
            "address" : addr,
            "connected_with " : "",
             "file_name"      :  "",
             "file_size"      : 4096
}
        
        print(f"Connection established with{client_name} : {addr}")

        thread = Thread(target = handleClient , args=(client,client_name))
        thread.start()


def getFiles():
    global SERVER
    global clients

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter,filename)
        song_counter = song_counter + 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing"+song_selected)

    else:
        infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

PlayButton = Button(window,text="Play",width=10,bd=1,bg='SkyBlue',font={"Calibri",10},command=play)
PlayButton.place(x=30,y=300)


Stop = Button(window,text="Stop",width=10,bd=1,bg='SkyBlue',font={"Calibri",10},command=stop)
Stop.place(x=200,y=200)


    