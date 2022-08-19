import tkinter as tk
from tkinter import filedialog as fd
import vlc


class MediaPlayer():
    def __init__(self):
        self.window = self.get_media_player()

    def set_full_screen(self):
        fs = True if not self.media_player.get_fullscreen() else False
        self.media_player.set_fullscreen(fs)

    def set_media(self):
        file_name = fd.askopenfilename()
        short_name = file_name.split("/")[-1]
        print(short_name)
        media = vlc.Media(file_name)
        self.media_player = vlc.MediaPlayer()
        self.media_player.set_media(media)
        self.media_player.play()

    def play_media(self):
        self.media_player.play()

    def stop_media(self):
        self.media_player.stop()

    def pause_media(self):
        self.media_player.set_pause(1)

    def get_media_player(self):
        self.root = tk.Tk()
        self.root.title('Медиа плеер')
        self.root.geometry("300x85+800+20")
        self.txt = 'txt'


        self.change_video = tk.Button(self.root,
                                      text='Выберите видео',
                                      command=self.set_media,
                                      justify='center'
                                      ).grid(row=0, column=0)

        self.fs = tk.Button(self.root,
                            text='Полный экран',
                            command=self.set_full_screen,
                            justify='center'
                            ).grid(row=0, column=2)

        self.stop = tk.Button(self.root,
                              text='Stop',
                              command=self.stop_media,
                              justify='center',
                              width=10,
                              background='red').grid(row=1, column=0)

        self.pause = tk.Button(self.root,
                               text='Pause',
                               command=self.pause_media,
                               justify='center',
                               width=10,
                               background='light blue').grid(row=1, column=1)

        self.play = tk.Button(self.root,
                              text='Play',
                              command=self.play_media,
                              justify='center',
                              width=10,
                              background='green').grid(row=1, column=2)

        if self.txt != 'txt':
            self.root.title(self.txt)

        self.root.columnconfigure(0, minsize=100)
        self.root.columnconfigure(1, minsize=100)
        self.root.columnconfigure(2, minsize=100)

        self.root.rowconfigure(0, minsize=30)
        self.root.rowconfigure(1, minsize=50)
        self.root.rowconfigure(2, minsize=30)

        self.root.mainloop()
        return self.root



