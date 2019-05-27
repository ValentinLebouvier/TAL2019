#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:08:11 2019

@author: valentinlebouvier
"""
import threading
import time

from Maze import Maze
from Characters import PacMan,Ghost


class PacManEngine(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.maze = Maze()
        self.PacmanList = {}
        self.GhostList = {}
        self.PacmanList["Pacman"] = PacMan(1.5,1.5,1,self.maze)
        #self.PacmanList["MsPacman"] = PacMan(1,26,0.9,self.maze)
        #self.PacmanList["JrPacman"] = PacMan(29,14,0.8,self.maze)
        self.GhostList["Pinky"] = Ghost(11.5,9.5,1,self.maze)
        #self.GhostList["Blinky"] = Ghost(11,18,0.6,self.maze)
        #self.GhostList["Inky"] = Ghost(17,9,0.5,self.maze)
        #self.GhostList["Clyde"] = Ghost(17,18,0.4,self.maze)
        self.gameSpeed = .05
        self.stop_thread = False
        
        self.start()
    
    def displayText(self):
        disp = self.maze.displayText()
        for c in self.PacmanList.values():
            disp[int(c.x)][int(c.y)] = "☺"
        for g in self.GhostList.values():
            disp[int(g.x)][int(g.y)] = "X"
        for x in range(self.maze.height):
            for y in range(self.maze.width):
                print(disp[x][y],sep='',end='')
            print()
            
    def hasGhost(self,x,y):
        for g in self.GhostList:
            if (x,y)==g.getCoordinates():
                return True
        return False
    
    def hasLost(self):
        for c in self.PacmanList.values():
            for g in self.GhostList.values():
                if int(c.x)==int(g.x) and int(c.y)==int(g.y) and not c.hasPower:
                    return True
        return False
    
    def hasPacMan(self,x,y):
        for c in self.PacmanList:
            if (x,y)==c.getCoordinates():
                return True
        return False
    
    def hasWon(self):
        return not(self.hasLost()) and self.noMorePills()

    def noMorePills(self):
        return self.maze.hasNoPill()

    def run(self):
        time.sleep(1)
        while (True):
            self.updateSeen()
            
            for c in self.PacmanList.values():
                c.move()
            if self.hasLost():
                break
            for g in self.GhostList.values():
                g.move()
            if self.hasLost():
                break
            #self.displayText()
            self.view.update()
            
            time.sleep(self.gameSpeed)
            if (self.stop_thread):
                break
    
    def stop(self):
        self.stop_thread = True
    
    def setView(self,view):
        self.view = view
            
    def updateSeen(self):
        for g in self.GhostList.values():
            g.decreaseLastSeen()
        for c in self.PacmanList.values():
            coord1 = c.getCoordinates()
            for g in self.GhostList.values():
                coord2 = g.getCoordinates()
                c.updateSeen(g.name,coord2)
                if self.maze.canSee(coord1,coord2):
                    g.updateSeen(c.name,coord1)
    
        
    
