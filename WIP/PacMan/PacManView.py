#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:42:59 2019

@author: valentinlebouvier
"""
import threading
from tkinter import Toplevel,Canvas,Frame,NW,Tk
from PacManEngine import PacManEngine

class PacManView(threading.Thread):
    
    CELL_SIZE = 30
        
    def __init__(self,engine, controller):
        threading.Thread.__init__(self)
        self.controller = controller
        self.engine = engine
        self.engine.setView(self)
        self.isToStop = False
        
        self.start()
        
    def close(self):
        self.controller.stop()
    
    def closeUpdate(self):
        if self.isToStop:
            self.root.destroy()
        self.root.after(1000,self.closeUpdate)
        
    def stop(self):
        self.isToStop = True
        
    def update(self):
        for (x,y) in self.pills:
            if not self.engine.maze.hasPill(x,y):
                p = self.pills[(x,y)]
                self.backgroundCanvas.delete(p)
        for c in self.pacmans:
            (x,y)=self.engine.PacmanList[c].getCoordinates()
            direction = self.engine.PacmanList[c].getDirection()
            self.backgroundCanvas.delete(self.pacmans[c])
            if direction=="East":
                self.pacmans[c] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=30,extent=300,fill="yellow")
            elif direction=="West":
                self.pacmans[c] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=210,extent=300,fill="yellow")
            elif direction=="North":
                self.pacmans[c] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=120,extent=300,fill="yellow")
            elif direction=="South":
                self.pacmans[c] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=300,extent=300,fill="yellow")
        for g in self.ghosts:
            (x,y)=self.engine.GhostList[g].getCoordinates()
            self.backgroundCanvas.delete(self.ghosts[g])
            self.ghosts[g] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE+(PacManView.CELL_SIZE-2),start=0,extent=180,fill="pink")
    
    def run(self):
        self.root = Tk()
        self.root.title("PacMan")
        self.root.resizable(False,False)
        self.root.geometry(str(28*PacManView.CELL_SIZE)+"x"+str(31*PacManView.CELL_SIZE)+"+0+0")
        
        self.root.after(1000,self.closeUpdate)
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
        self.backgroundCanvas = Canvas(self.mainFrame,height=31*PacManView.CELL_SIZE,width=28*PacManView.CELL_SIZE,bg="black")
        background = [[self.backgroundCanvas.create_rectangle(y*PacManView.CELL_SIZE,x*PacManView.CELL_SIZE,(y+1)*PacManView.CELL_SIZE,(x+1)*PacManView.CELL_SIZE,fill="white",outline="light grey") for y in range(self.engine.maze.width) if not self.engine.maze.isWall(x,y)] for x in range(self.engine.maze.height)]
        self.pills = {}
        for x in range(self.engine.maze.height):
            for y in range(self.engine.maze.width):
                if self.engine.maze.hasPill(x,y):
                    self.pills[(x,y)]= self.backgroundCanvas.create_oval(y*PacManView.CELL_SIZE+(PacManView.CELL_SIZE//3),x*PacManView.CELL_SIZE+(PacManView.CELL_SIZE//3),(y+1)*PacManView.CELL_SIZE-(PacManView.CELL_SIZE//3),(x+1)*PacManView.CELL_SIZE-(PacManView.CELL_SIZE//3),fill="yellow")
        self.pacmans = {}
        for c in self.engine.PacmanList:
            (x,y) = self.engine.PacmanList[c].getCoordinates()
            
            self.pacmans[c] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE-1,start=30,extent=300,fill="yellow")
        self.ghosts = {}
        for g in self.engine.GhostList:
            (x,y) = self.engine.GhostList[g].getCoordinates()
            
            self.ghosts[g] = self.backgroundCanvas.create_arc(y*PacManView.CELL_SIZE+1,x*PacManView.CELL_SIZE+1,(y+1)*PacManView.CELL_SIZE-1,(x+1)*PacManView.CELL_SIZE+(PacManView.CELL_SIZE-2),start=0,extent=180,fill="pink")
            
        self.backgroundCanvas.pack()
        
        self.root.mainloop()
        
        

if __name__ == "__main__":
    engine = PacManEngine()
    engine.stop()
    
    view = PacManView(engine)
    view.start()