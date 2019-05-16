#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:53:47 2019

@author: valentinlebouvier
"""

class MovableCharacter(object):
    
    def setPosition(self,x,y):
        self.x = x
        self.y = y
    
    def getPosition(self):
        return (self.x,self.y)
    
    
    def moveWest(self):
        pass
    
    def moveEast(self):
        pass
    
    def moveSouth(self):
        pass
    
    def moveNorth(self):
        pass
    
    def display(self):
        pass

    
class PacMan(MovableCharacter):
    
    def __init__(self,x,y,maze,name="PacMan"):
        self.name = name
        self.x = x
        self.y = y
        self.maze = maze
        self.eatenPills = 0
        self.hasPower = False
        
    def canGoEast(self):
        return not self.maze.isWall(self.x,self.y+1)
    
    def canGoWest(self):
        return not self.maze.isWall(self.x,self.y-1)
    
    def canGoSouth(self):
        return not self.maze.isWall(self.x+1,self.y)
    
    def canGoNorth(self):
        return not self.maze.isWall(self.x-1,self.y)
    
    def moveEast(self):
        if self.canGoEast():
            self.y=(self.y+1)%self.maze.WIDTH
            if self.maze.takePill(self.x,self.y):
                self.eatenPills += 1
            return True
        return False
        
    def moveWest(self):
        if self.canGoWest():
            self.y=(self.y-1)%self.maze.WIDTH
            if self.maze.takePill(self.x,self.y):
                self.eatenPills += 1
            return True
        return False

    def moveSouth(self):
        if self.canGoSouth():
            self.x=(self.x+1)%self.maze.HEIGHT
            if self.maze.takePill(self.x,self.y):
                self.eatenPills += 1
            return True
        return False
    
    def moveNorth(self):
        if self.canGoNorth():
            self.x=(self.x-1)%self.maze.HEIGHT
            if self.maze.takePill(self.x,self.y):
                self.eatenPills += 1
            return True
        return False