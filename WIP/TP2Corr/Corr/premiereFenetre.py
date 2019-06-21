#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

if __name__=="__main__":
    
    fenetre = tk.Tk()
    
    bouton = tk.Button(fenetre,text="Quitter",command=fenetre.destroy)
    bouton.pack()
    
    fenetre.mainloop()