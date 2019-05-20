#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:53:47 2019

@author: valentinlebouvier
"""

class MovableCharacter(object):
    
    lastSeenCounter = 10
    
    Directions = {
            "West" : (0,-1),
            "East" : (0,1),
            "North" : (-1,0),
            "South" : (1,0)
                  }
    
    def setPosition(self,x,y):
        self.x = x
        self.y = y
    
    def getCoordinates(self):
        return (self.x,self.y)
    
    def setDirection(self,direction):
        movement = MovableCharacter.Directions.get(direction)
        self.dx = movement[0]
        self.dy = movement[1]
        return True
    
    def canGo(self,direction):
        movement = MovableCharacter.Directions.get(direction)
        return not self.maze.isWall(int(self.x+self.speed*movement[0])%self.maze.height,int(self.y+self.speed*movement[1])%self.maze.width)
    
    def canMove(self):
        return not self.maze.isWall(int(self.x+self.speed*self.dx)%self.maze.height,int(self.y+self.speed*self.dy)%self.maze.width)
    
    def updateSeen(self, name, coord):
        if not name in self.lastSeen:
            self.lastSeen.put(name,[coord,MovableCharacter.lastSeenCounter])
        else:
            self.lastSeen[name][0] = coord
    
    def decreaseLastSeen(self):
        for ls in self.lastSeen.keys:
            self.lastSeen[ls][1] -= 1
            if self.lastSeen[ls][1]==0:
                self.lastSeen.pop(ls)
    
    def chase(self, character):
        pass
    
    def flee(self):
        pass
    
    def move(self):
        pass
    
    def display(self):
        pass

    
class PacMan(MovableCharacter):
    
    def __init__(self,x,y,speed,maze,name="PacMan"):
        self.name = name
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.maze = maze
        self.lastSeen = {}
        self.eatenPills = 0
        if (self.maze.takePill(self.x,self.y)) : self.eatenPills+=1
        self.hasPower = False
    
    def move(self):
        if self.canMove():
            self.x = (self.x+self.speed*self.dx)%self.maze.height
            self.y = (self.y+self.speed*self.dy)%self.maze.width
            if self.maze.takePill(int(self.x),int(self.y)):
                self.eatenPills += 1

class Ghost(MovableCharacter):
    
    def __init__(self,x,y,speed,maze,name="PacMan"):
        self.name = name
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.maze = maze
        self.lastSeen = {}
        self.isEaten = False
    
    def move(self):
        if self.canMove():
            self.x = (self.x+self.speed*self.dx)%self.maze.height
            self.y = (self.y+self.speed*self.dy)%self.maze.width
    