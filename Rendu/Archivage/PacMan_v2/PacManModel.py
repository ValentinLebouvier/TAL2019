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


class PacManModel(threading.Thread):
    
    def __init__(self,nbPacmans,nbGhosts,speed):
        threading.Thread.__init__(self)
        self.maze = Maze()
        self.PacmanList = {}
        self.GhostList = {}
        self.subscribers = []
        for idP in range(nbPacmans):
            self.PacmanList["Pacman"+str(idP)] = PacMan(1.5,1.5,1,self.maze,"Pacman"+str(idP))
        for idG in range(nbGhosts):
            self.GhostList["Ghost"+str(idG)] = Ghost(11.5,9.5,0.9,self.maze,"Ghost"+str(idG))
        self.gameSpeed = speed
        self.stop_thread = False
        self.updateSeen()
        
        self.start()
    
    def __repr__(self):
        disp = self.maze.getTextMatrix()
        for c in self.PacmanList.values():
            disp[int(c.x)][int(c.y)] = "P"
        for g in self.GhostList.values():
            disp[int(g.x)][int(g.y)] = "G"
        return disp
            
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
            if (self.stop_thread):
                break
            for v in self.subscribers:
                v.update()
            time.sleep(self.gameSpeed)
    
    def stop(self):
        self.stop_thread = True
    
    def subscribe(self,subs):
        self.subscribers.append(subs)
            
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
    
        
    
