import pygame
from tkinter.filedialog import *
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import font
import mutagen
from mutagen.easyid3 import EasyID3
import pigpio
import sys

pygame.init()


class FrameApp(Frame):
    def __init__(self,root):
         tk.Frame.__init__(self,root)

         self.grid()
         self.paused = False
         self.playlist =list()
         self.actual_song = 0    
        # self.song_data=[]

         self.frame1=tk.Frame(root,bg='blue')
         self.frame1.place(relx=0.5,rely=0.89,relwidth=0.3,relheight=0.6,anchor='n')
       
         imageb1=Image.open('C:\\Users\\LENOVO\\Desktop\\yes7.png')
         imageb11=ImageTk.PhotoImage(imageb1)
         self.b1=tk.Button(self.frame1,image=imageb11,command=self.play_music)
         self.image=imageb11
         self.b1.grid(row=3,column=4)
         
         imageb2=Image.open('C:\\Users\\LENOVO\\Desktop\\yes8.png')
         imageb22=ImageTk.PhotoImage(imageb2)
         self.b2 =tk.Button(self.frame1,image=imageb22, command=self.previous_song)
         self.b2.image=imageb22
         self.b2.grid(row=3,column=5)

         imageb3=Image.open('C:\\Users\\LENOVO\\Desktop\\yes5.png')
         imageb33=ImageTk.PhotoImage(imageb3)
         self.b3 =tk.Button(self.frame1,image=imageb33, command=self.toggle)
         self.b3.image=imageb33
         self.b3.grid(row=3,column=7)

         imageb4=Image.open('C:\\Users\\LENOVO\\Desktop\\yes7.png')
         imageb44=ImageTk.PhotoImage(imageb4)
         self.b4 =tk.Button(self.frame1, image=imageb44, command=self.next_song)
         self.b4.image=imageb4
         self.b4.grid(row=3,column=8)

         imageb5=Image.open('C:\\Users\\LENOVO\\Desktop\\yes11.png')
         imageb55=ImageTk.PhotoImage(imageb5)
         self.b5=tk.Button(self.frame1, image=imageb55, command=self.add_to_list)
                  
         self.b5.image=imageb55
         self.b5.grid(row=3,column=8)
        
        
        
         self.label1 =tk.Label(bg='#980000',fg='white',width=50)
         self.label1.place(relx=0.48,rely=0.83,relwidth=0.5,anchor='n')

         self.output =tk.Text(root,bg='#A0A0A0',fg='white',font=40,bd=3,width=80,height=30)
         self.output.grid(row=5,column=5,padx=300)
         #sys.stdout = tk.TextRedirector(self.output, "stdout")
        # sys.stderr = tk.TextRedirector(self.output, "stderr")


         #self.output.
       
        # set event to not predefined value in pygame
         self.SONG_END = pygame.USEREVENT + 1             
      # et event is not pedfined in ppygame
       

        # TODO: Make progressbar, delete songs from playlist, amplify volume

    def add_to_list(self):
        """
        Opens window to browse data on disk and adds selected songs to play list
        :return: None
        """
        directory = askopenfilenames()
        # appends song directory on disk to playlist in memory
        for song_dir in directory:
            print(song_dir)
            self.playlist.append(song_dir)
        self.output.delete(0.0, END)

        for key, item in enumerate(self.playlist):
            # appends song to textbox
            song = EasyID3(item)
            song_data = (str(key + 1) + ' : ' + song['title'][0] + ' - '
                         + song['artist'][0])
            
            self.output.insert(END,song_data ,'\n')

    def song_data(self):
        """
        Makes string of current playing song data over the text box
        :return: string - current song data
        """
        song = EasyID3(self.playlist[self.actual_song])
        song_data = "Now playing: Nr:" + str(self.actual_song + 1) + " " + \
                    str(song['title']) + " - " + str(song['artist'])
        return song_data

    def play_music(self):
        """
        Loads current song, plays it, sets event on song finish
        :return: None
        """
        directory = self.playlist[self.actual_song]
        pygame.mixer.music.load(directory)
        pygame.mixer.music.play(1, 0.0)
        pygame.mixer.music.set_endevent(self.SONG_END)
        self.paused = False
        self.label1['text'] = self.song_data()

    def check_music(self):
        """
        Listens to END_MUSIC event and triggers next song to play if current 
        song has finished
        :return: None
        """
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.next_song()

    def toggle(self):
        """
        Toggles current song
        :return: None
        """
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        elif not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def get_next_song(self):
        """
        Gets next song number on playlist
        :return: int - next song number
        """
        if self.actual_song + 2 <= len(self.playlist):
            return self.actual_song + 1
        else:
            return 0

    def next_song(self):
        """
        Plays next song
        :return: None
        """
        self.actual_song = self.get_next_song()
        self.play_music()

    def get_previous_song(self):
        """
        Gets previous song number on playlist and returns it
        :return: int - prevoius song number on playlist
        """
        if self.actual_song - 1 >= 0:
            return self.actual_song - 1
        else:
            return len(self.playlist) - 1

    def previous_song(self):
        """
        Plays prevoius song
        :return: 
        """
        self.actual_song = self.get_previous_song()
        self.play_music()

        
root =tk.Tk()
HEIGHT=1000
WEIDTH=1000
canvas=tk.Canvas(root,height=HEIGHT,width=WEIDTH,bg='black')

#image2 =Image.open('C:\\Users\\LENOVO\\Pictures\\color.png')
#image1 = ImageTk.PhotoImage(image2)
#background_label=tk.Label(root,image=image1)
#background_label.place(relwidth=1,relheight=1)


app = FrameApp(root)

while True:
    # runs mainloop of program
    app.check_music()
    app.update()

