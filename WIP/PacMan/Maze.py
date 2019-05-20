#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:57:06 2019

@author: valentinlebouvier
"""

import networkx as nx

class Maze(object):
    
    HEIGHT = 31
    WIDTH = 28
    
    Wall = -1
    Pill = 1
    Empty = 0
    
    def init_maze(height, width, random=True):
        maze = [[1 for y in range(width)] for x in range(height)]
        if random:
            pass
        else:
            maze =[ 14*[-1] + [-1]*14,
                    [-1]+12*[1]+[-1] + [-1]+[1]*12+[-1],
                    [-1]+[1]+4*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*4+[1]+[-1],
                    [-1]+[1]+4*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*4+[1]+[-1],
                    [-1]+[1]+4*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*4+[1]+[-1],
                    [-1]+13*[1] + [1]*13+[-1],
                    [-1]+[1]+4*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*4+[1]+[-1],
                    [-1]+[1]+4*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*4+[1]+[-1],
                    [-1]+6*[1]+2*[-1]+4*[1]+[-1] + [-1]+[1]*4+[-1]*2+[1]*6+[-1],
                    6*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*6,
                    6*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+5*[1] + [1]*5+[-1]*2+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*6,
                    10*[1]+4*[-1] + [-1]*4+[1]*10,
                    6*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+5*[1] + [1]*5+[-1]*2+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*6,
                    6*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*6,
                    [-1]+12*[1]+[-1] + [-1]+[1]*12+[-1],
                    [-1]+[1]+4*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*4+[1]+[-1],
                    [-1]+[1]+4*[-1]+[1]+5*[-1]+[1]+[-1] + [-1]+[1]+[-1]*5+[1]+[-1]*4+[1]+[-1],
                    [-1]+3*[1]+2*[-1]+8*[1] + [1]*8+[-1]*2+[1]*3+[-1],
                    3*[-1]+[1]+2*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*2+[1]+[-1]*3,
                    3*[-1]+[1]+2*[-1]+[1]+2*[-1]+[1]+4*[-1] + [-1]*4+[1]+[-1]*2+[1]+[-1]*2+[1]+[-1]*3,
                    [-1]+6*[1]+2*[-1]+4*[1]+[-1] + [-1]+[1]*4+[-1]*2+[1]*6+[-1],
                    [-1]+[1]+10*[-1]+[1]+[-1] + [-1]+[1]+[-1]*10+[1]+[-1],
                    [-1]+[1]+10*[-1]+[1]+[-1] + [-1]+[1]+[-1]*10+[1]+[-1],
                    [-1]+13*[1] + [1]*13+[-1],
                    14*[-1] + [-1]*14
                ]
        return maze
        
    def __init__(self, height=None, width=None, random_maze=False):
        if height is None:
            self.height = Maze.HEIGHT
        else:
            self.height = height
        if width is None:
            self.width = Maze.WIDTH
        else:
            self.width = width            
        self.maze = Maze.init_maze(self.height,self.width,random_maze)
        
        
    def isWall(self,x,y):
        return self.maze[x%self.height][y%self.width]==Maze.Wall
    
    def hasPill(self,x,y):
        return self.maze[x%self.height][y%self.width]==Maze.Pill
    
    def takePill(self,x,y):
        if self.hasPill(x,y):
            self.maze[x][y]=Maze.Empty
            return True
        return False
    
    def hasNoPill(self):
        for x in range(self.height):
            for y in range(self.width):
                if self.hasPill(x,y):
                    return False
        return True
    
    def display(self):
        tileset = [".","o","▓"]
        for x in range(self.height):
            for y in range(self.width):
                print(tileset[self.maze[x][y]], sep='', end=' ')
            print()
    
    def displayText(self):
        res = [["" for y in range(self.width)] for x in range(self.height)]
        tileset = [".","o","▓"]
        for x in range(self.height):
            for y in range(self.width):
                res[x][y] = tileset[self.maze[x][y]]
        return res
    
    def direction(self, coordStart, coordEnd):
        pass
    
    def closestPill(self, coord):
        pass
    
    def closestPowerPill(self, coord):
        pass
    
    def canSee(self, coordStart, coordEnd):
        if coordStart[0]==coordEnd[0]:
            for y in range(coordStart[1],coordEnd[1]):
                if self.isWall(coordStart[0],y):
                    return False
            return True
        elif coordStart[0]==coordEnd[0]:
            for x in range(coordStart[0],coordEnd[0]):
                if self.isWall(x, coordStart[1]):
                    return False
            return True
        return False
        
                       
                       
            
    