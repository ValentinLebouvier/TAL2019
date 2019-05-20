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
        self.PacmanList["Pacman"] = PacMan(1,1,self.maze)
        self.GhostList["Pinky"] = Ghost(1,12,self.maze)
        self.gameSpeed = 1
        self.stop_thread = False
        self.thread = threading.Thread(target=self.run, args=(lambda : self.stop_thread,))
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution
    
    def run(self,stop):
        
        while (True):
            for c in self.PacmanList.values():
                c.move()
            if self.hasLost():
                break
            for g in self.GhostList.values():
                g.move()
            if self.hasLost():
                break
            self.display()
            
            time.sleep(self.gameSpeed)
            if (stop()):
                break
            
            
    def noMorePills(self):
        #print("No More Pills")
        return self.maze.hasNoPill()
    
    def hasLost(self):
        for c in self.PacmanList.values():
            for g in self.GhostList.values():
                if c.x==g.x and c.y==g.y and not c.hasPower:
                    return True
        return False
    
    def hasWon(self):
        return not(self.hasLost()) and self.noMorePills()
    
    def display(self):
        disp = self.maze.displayText()
        for c in self.PacmanList.values():
            disp[c.x][c.y] = "☺"
        for g in self.GhostList.values():
            disp[g.x][g.y] = "Ö"
        for x in range(Maze.HEIGHT):
            for y in range(Maze.WIDTH):
                print(disp[x][y],sep='',end='')
            print()
        
    def stop(self):
        self.stop_thread = True
    
