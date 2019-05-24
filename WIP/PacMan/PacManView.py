#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:42:59 2019

@author: valentinlebouvier
"""
from tkinter import Tk,Canvas


class PacManView(object):
        
    def __init__(self,engine):
        self.engine = engine
        
        self.root = Tk()
        self.root.title("PacMan")
        self.root.resizable(True,True)
        self.canvas = Canvas(self.root, background="black")
        self.canvas.grid()
        
    def update(self):
        pass
        
        
        
    def start(self):
        self.root.mainloop()
        

if __name__ == "__main__":
    
    view = PacManView()
    view.start()