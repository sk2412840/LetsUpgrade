from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')


Label_1=Label(root,text="Paste The YouTube Link Here", font=("bold",20))
Label_1.place(x=100,y=20)


mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=100, y=80)


def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(r'C:\Users\kaku\Downloads\YouTube'):
        os.makedirs(r'C:\Users\kaku\Downloads\YouTube')
    ytvideo.download(r'C:\Users\kaku\Downloads\YouTube') 

Button(root,text="Download Video", width=25, bg='red',fg="white", command=downloadVideo).place(x=191, y=125)

root.mainloop()
