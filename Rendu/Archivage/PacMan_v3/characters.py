#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from maze import Maze

class MovableCharacter(object):
    
    lastSeenCounter = 10
    
    def canGo(self,direction):
        movement = Maze.Directions[direction]
        return not self.maze.isWall(int(self.x+self.speed*movement[0])%self.maze.height,int(self.y+self.speed*movement[1])%self.maze.width)
    
    def canMove(self):
        return not self.maze.isWall(int(self.x+self.speed*self.dx)%self.maze.height,int(self.y+self.speed*self.dy)%self.maze.width)
    
    def chase(self):
        if list(self.lastSeen) == []:
            return False
        if self.chasing == None or not(self.chasing in list(self.lastSeen.keys())):
            self.chasing = list(self.lastSeen.keys())[0]
        coord = self.lastSeen[self.chasing][0]
        direction = self.maze.direction(self.getCoordinates(),coord)
        self.setDirection(direction)
    
    def decreaseLastSeen(self):
        toDelete = []
        for ls in self.lastSeen.keys():
            self.lastSeen[ls][1] -= 1
            if self.lastSeen[ls][1]==0:
                toDelete.append(ls)
        for ls in toDelete:
            self.lastSeen.pop(ls)
            
    def getCoordinates(self):
        return (int(self.x),int(self.y))
    
    def getDirection(self):
        return Maze.ReverseDirections[(self.dx,self.dy)]

    def updateSeen(self, name, coord):
        self.lastSeen[name] = [coord,MovableCharacter.lastSeenCounter]

    def setDirection(self,direction):
        if not (direction is None):
            movement = Maze.Directions[direction]
            self.dx = movement[0]
            self.dy = movement[1]
        return True

    def setPosition(self,x,y):
        self.x = x
        self.y = y
    
    def display(self):
        pass

    def flee(self):
        pass
    
    def move(self):
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
        self.seuilCloseDistance = 10
        self.chasing = None
        self.eatenPills = 0
        if (self.maze.takePill(self.x,self.y)) : self.eatenPills+=1
        self.hasPower = False
    
    def isAlone(self):
        closest,dist = self.maze.closestAmong(self.getCoordinates(),self.lastSeen)
        res = dist>self.seuilCloseDistance
        return res
    
    def gotoPill(self):
        coord1 = self.getCoordinates()
        coord2 = self.maze.closestPill(coord1)
        if coord2 is None:
            return False
        direction = self.maze.direction(coord1,coord2)
        self.setDirection(direction)
        return True

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
        self.chasing = None
        self.isEaten = False
    
    def isAlone(self):
        return list(self.lastSeen.keys())==[]
    
    def move(self):
        if self.canMove():
            self.x = (self.x+self.speed*self.dx)%self.maze.height
            self.y = (self.y+self.speed*self.dy)%self.maze.width