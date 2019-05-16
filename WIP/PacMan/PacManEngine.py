#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:08:11 2019

@author: valentinlebouvier
"""
import threading
import time

from Maze import Maze
from Characters import PacMan


class PacManEngine(object):
    
    def __init__(self):
        self.maze = Maze()
        self.characterList = {}
        self.characterList["Pacman"] = PacMan(1,1,self.maze)
        self.gameSpeed = 0.5
        self.stop_thread = False
        self.thread = threading.Thread(target=self.run, args=(lambda : self.stop_thread,))
        self.thread.daemon = True                            # Daemonize thread
        self.thread.start()                                  # Start the execution
    
    def run(self,stop):
        
        while (True):
            for c in self.characterList.values():
                c.move()
            
            time.sleep(self.gameSpeed)
            if (stop()):
                break
            
            
    def noMorePills(self):
        print("No More Pills")
        return self.maze.hasNoPill()
    
    def hasLost(self):
        return False
    
    def hasWon(self):
        return not(self.hasLost()) and self.noMorePills()
    
    def display(self):
        self.maze.display()
        
    def stop(self):
        self.stop_thread = True
    
