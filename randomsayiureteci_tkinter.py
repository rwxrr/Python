#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
import random

class Uygulama(object):
    def __init__(self):
        self.araclar()

    def kodlar(self):
        self.liste = []
        for i in range(6):
            while len(self.liste) != 6:
                a = random.randint(1, 100)
                if a not in self.liste:
                    self.liste.append(a)
        self.etiket["text"] = self.liste

    def araclar(self):
        self.etiket = Label(text="Sayı üretmek için düğmeye basınız!",
                            fg="white",
                            bg="#61380B",
                            font="Helvetica 12 bold")

        self.etiket.pack()

        self.dugme = Button(text="Yeniden", command = self.kodlar)
        self.dugme.pack()

pencere = Tk()
pencere.geometry("300x50+600+460")
uyg = Uygulama()
mainloop()
