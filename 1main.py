from tkinter import *
from PIL import Image

import os, random


class Mission1(object):
    def __init__(self):
        self.affichage_drapeau = Tk()
        self.affichage_drapeau.config(bg="#252525")
        self.affichage_drapeau.title("Mission 1 : daouanim")
        self.affichage_drapeau.geometry("1280x720")
        self.affichage_drapeau.resizable(0, 0)

        self.points = 0
        self.essai = 0





    def affichage(self):

        self.canvas_drapeaux = Canvas(self.affichage_drapeau, width = 800, height = 500, bg = "#252525")
        self.canvas_drapeaux.pack(pady = 20, padx = 25)

        self.frame_boutton = Frame(self.affichage_drapeau, width = 250, height = 100,bg = "#252525")
        self.frame_boutton.pack(side = BOTTOM, pady = 10, padx = 5)

        self.drapeaux_guess = StringVar()
        
        self.guess_drapeaux = Entry(self.frame_boutton, textvariable= self.drapeaux_guess)
        self.guess_drapeaux.pack(pady = 20, padx = 20)
        self.boutton_entrer = Button(self.frame_boutton, height = 2, width = 10,font = ("Alef", "12"), text = "Envoyer", bg = "#252525", fg = "#F8F8FF", command = self.verif)
        self.boutton_entrer.pack(pady = 5, padx = 20, side = RIGHT)
        self.boutton_skip = Button(self.frame_boutton, height = 2, width = 10,font = ("Alef", "12"),text = "Skip", bg = "#252525", fg = "#F8F8FF", command = self.skip)
        self.boutton_skip.pack(pady = 5, padx = 20 ,side = LEFT)

        self.points_affichage = Label(self.frame_boutton,height = 8, width = 10,font = ("Alef", "12"), text = self.points, bg = "#252525", fg = "#F8F8FF")
        self.points_affichage.pack(pady = 10)


        self.random_choix()
    

    def random_choix(self):

        self.drapeau_folder = os.listdir()
        self.choix_drapeaux = random.choice(self.drapeau_folder)
        self.images_drapeaux = PhotoImage(file=self.choix_drapeaux)
        self.canvas_drapeaux.create_image(400, 250, image=self.images_drapeaux)
            

    def verif(self):
        if self.drapeaux_guess.get() == self.choix_drapeaux.split(".")[0]:
            self.points = self.points + 1
            self.reset()
            
        else:
            self.points = self.points - 1
            self.reset()
                

    def reset(self):
        
        self.points_affichage.pack_forget()
        self.points_affichage = Label(self.frame_boutton,height = 8, width = 10,font = ("Alef", "15"), text = self.points, bg = "#252525", fg = "#F8F8FF" )
        self.points_affichage.pack(pady = 10)
        self.choix_drapeaux = ""
        self.random_choix()

    def skip(self):
        self.points = self.points - 1
        self.points_affichage.pack_forget()
        self.points_affichage = Label(self.frame_boutton,height = 8, width = 10,font = ("Alef", "12"), text = self.points, bg = "#252525", fg = "#F8F8FF")
        self.points_affichage.pack(pady = 10)
        self.choix_drapeaux = ""
        self.random_choix()
        
        
        
            

        

        
        
        
m1 = Mission1()
m1.affichage()
