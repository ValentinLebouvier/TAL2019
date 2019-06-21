#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk,Canvas
from PacManModel import PacManModel
from PacManController import PacManController

class PacManView(Tk):
    
    CELL_SIZE = 30
        
    def __init__(self,model, controller):
        Tk.__init__(self)
        self.controller = controller
        self.model = model
        
        self.controller.subscribe(self)
        self.model.subscribe(self)
        
        self.start()
        
    def close(self):
        self.controller.stop()
        
    def stop(self):
        self.destroy()        
        
    def update(self):
        for (x,y) in self.pills:
            if not self.model.maze.hasPill(x,y):
                p = self.pills[(x,y)]
                self.canvas.delete(p)
        for p in self.pacmans:
            self.updatePacman(p)
        for g in self.ghosts:
            (x,y)=self.model.GhostList[g].getCoordinates()
            self.canvas.delete(self.ghosts[g])
            self.ghosts[g] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE+(PacManView.CELL_SIZE-2),start=0,extent=180,fill="pink")
    
    def updatePacman(self,c):
        (x,y)=self.model.PacmanList[c].getCoordinates()
        direction = self.model.PacmanList[c].getDirection()
        self.canvas.delete(self.pacmans[c])
        if direction=="East":
            self.pacmans[c] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=30,extent=300,fill="yellow")
        elif direction=="West":
            self.pacmans[c] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=210,extent=300,fill="yellow")
        elif direction=="North":
            self.pacmans[c] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=120,extent=300,fill="yellow")
        elif direction=="South":
            self.pacmans[c] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=300,extent=300,fill="yellow")
    
    def start(self):
        self.title("PacMan")
        self.resizable(False,False)
        self.geometry(str(28*PacManView.CELL_SIZE)+"x"+str(31*PacManView.CELL_SIZE)+"+0+0")
        
        self.protocol("WM_DELETE_WINDOW",self.close)
        
        self.canvas = Canvas(self,height=31*PacManView.CELL_SIZE,width=28*PacManView.CELL_SIZE,bg="black")
        background = [[self.canvas.create_rectangle(y*PacManView.CELL_SIZE,x*PacManView.CELL_SIZE,(y+1)*PacManView.CELL_SIZE,(x+1)*PacManView.CELL_SIZE,fill="white",outline="light grey") for y in range(self.model.maze.width) if not self.model.maze.isWall(x,y)] for x in range(self.model.maze.height)]
        self.pills = {}
        for x in range(self.model.maze.height):
            for y in range(self.model.maze.width):
                if self.model.maze.hasPill(x,y):
                    self.pills[(x,y)]= self.canvas.create_oval(y*PacManView.CELL_SIZE+(PacManView.CELL_SIZE//3),x*PacManView.CELL_SIZE+(PacManView.CELL_SIZE//3),(y+1)*PacManView.CELL_SIZE-(PacManView.CELL_SIZE//3),(x+1)*PacManView.CELL_SIZE-(PacManView.CELL_SIZE//3),fill="yellow")
        self.pacmans = {}
        for c in self.model.PacmanList:
            (x,y) = self.model.PacmanList[c].getCoordinates()
            self.pacmans[c] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=30,extent=300,fill="yellow")
        self.ghosts = {}
        for g in self.model.GhostList:
            (x,y) = self.model.GhostList[g].getCoordinates()
            self.ghosts[g] = self.canvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE+(PacManView.CELL_SIZE-2),start=0,extent=180,fill="pink")
            
        self.canvas.pack()
        
        self.mainloop()
