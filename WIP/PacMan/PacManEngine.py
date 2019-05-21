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


class PacManEngine(object):
    
    def __init__(self):
        self.maze = Maze()
        self.PacmanList = {}
        self.GhostList = {}
        self.PacmanList["Pacman"] = PacMan(1,1,1,self.maze)
        #self.PacmanList["MsPacman"] = PacMan(1,26,0.9,self.maze)
        #self.PacmanList["JrPacman"] = PacMan(29,14,0.8,self.maze)
        #self.GhostList["Pinky"] = Ghost(11,9,0.7,self.maze)
        #self.GhostList["Blinky"] = Ghost(11,18,0.6,self.maze)
        #self.GhostList["Inky"] = Ghost(17,9,0.5,self.maze)
        #self.GhostList["Clyde"] = Ghost(17,18,0.4,self.maze)
        self.gameSpeed = .45
        self.stop_thread = False
        self.thread = threading.Thread(target=self.run, args=(lambda : self.stop_thread,))
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution
    
    def run(self,stop):
        
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
            self.displayText()
            
            time.sleep(self.gameSpeed)
            if (stop()):
                break
            
            
    def noMorePills(self):
        return self.maze.hasNoPill()
    
    def hasLost(self):
        for c in self.PacmanList.values():
            for g in self.GhostList.values():
                if int(c.x)==int(g.x) and int(c.y)==int(g.y) and not c.hasPower:
                    return True
        return False
    
    def hasWon(self):
        return not(self.hasLost()) and self.noMorePills()
    
    def updateSeen(self):
        for c in self.PacmanList.values():
            c.decreaseLastSeen()
        for g in self.GhostList.values():
            g.decreaseLastSeen()
        for c in self.PacmanList.values():
            for g in self.GhostList.values():
                coord1,coord2 = c.getCoordinates(), g.getCoordinates()
                if self.maze.canSee(coord1,coord2):
                    c.updateSeen(g.name,coord2)
                    g.updateSeen(c.name,coord1)
    
    def displayText(self):
        disp = self.maze.displayText()
        for c in self.PacmanList.values():
            disp[int(c.x)][int(c.y)] = "☺"
        for g in self.GhostList.values():
            disp[int(g.x)][int(g.y)] = "Ö"
        for x in range(self.maze.height):
            for y in range(self.maze.width):
                print(disp[x][y],sep='',end='')
            print()
        
    def stop(self):
        self.stop_thread = True
    
