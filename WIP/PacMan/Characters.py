#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:53:47 2019

@author: valentinlebouvier
"""

from Maze import Maze

class MovableCharacter(object):
    
    Directions = {
            "West" : (0,-1),
            "East" : (0,1),
            "North" : (-1,0),
            "South" : (1,0)
                  }
    
    def setPosition(self,x,y):
        self.x = x
        self.y = y
    
    def getPosition(self):
        return (self.x,self.y)
    
    def setDirection(self,direction):
        movement = MovableCharacter.Directions.get(direction)
        self.dx = movement[0]
        self.dy = movement[1]
        return True
    
    def canGoWest(self):
        movement = MovableCharacter.Directions.get("West")
        return not self.maze.isWall(self.x+movement[0],self.y+movement[1])
    
    def canGoEast(self):
        movement = MovableCharacter.Directions.get("East")
        return not self.maze.isWall(self.x+movement[0],self.y+movement[1])
    
    def canGoNorth(self):
        movement = MovableCharacter.Directions.get("North")
        return not self.maze.isWall(self.x+movement[0],self.y+movement[1])
    
    def canGoSouth(self):
        movement = MovableCharacter.Directions.get("South")
        return not self.maze.isWall(self.x+movement[0],self.y+movement[1])
    
    def canMove(self):
        pass
    
    def move(self):
        pass
    
    def display(self):
        pass

    
class PacMan(MovableCharacter):
    
    def __init__(self,x,y,maze,name="PacMan"):
        self.name = name
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.maze = maze
        self.eatenPills = 0
        if (self.maze.takePill(self.x,self.y)) : self.eatenPills+=1
        self.hasPower = False
        
    def canMove(self):
        return not self.maze.isWall(self.x+self.dx,self.y+self.dy)
    
    def move(self):
        if self.canMove():
            self.x = (self.x+self.dx)% Maze.HEIGHT
            self.y = (self.y+self.dy)% Maze.WIDTH
            if self.maze.takePill(self.x,self.y):
                self.eatenPills += 1

class Ghost(MovableCharacter):
    def __init__(self,x,y,maze,name="PacMan"):
        self.name = name
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.maze = maze
        self.isEaten = False
        
    def canMove(self):
        return not self.maze.isWall(self.x+self.dx,self.y+self.dy)
    
    def move(self):
        if self.canMove():
            self.x = (self.x+self.dx)% Maze.HEIGHT
            self.y = (self.y+self.dy)% Maze.WIDTH
    