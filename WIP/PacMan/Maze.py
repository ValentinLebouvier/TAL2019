#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:57:06 2019

@author: valentinlebouvier
"""

import numpy as np

class Maze(object):
    
    HEIGHT = 31
    WIDTH = 28
    
    Wall = -1
    Pill = 1
    Empty = 0
    
    def init_maze(random=True):
        maze = [[1 for y in range(Maze.WIDTH)] for x in range(Maze.HEIGHT)]
        if (random):
            pass
        else:
            for x in range(Maze.HEIGHT):
                for y in range(Maze.WIDTH):
                    if (x==0|y==0|x==Maze.HEIGHT|y==Maze.WIDTH):
                        maze[x][y]=-1
        return maze
        
    def __init__(self,random_maze=False):
        self.maze = Maze.init_maze(random_maze)
        
    def canMoveWest(self,coord):
        return self.maze[coord[0]][(coord[1]-1)%Maze.WIDTH] != -1
    
    def canMoveEast(self,coord):
        return self.maze[coord[0]][(coord[1]+1)%Maze.WIDTH] != -1    
    
    def canMoveSouth(self,coord):
        return self.maze[(coord[0]+1)%Maze.HEIGHT][coord[1]] != -1
    
    def canMoveNorth(self,coord):
        return self.maze[(coord[0]-1)%Maze.HEIGHT][coord[1]] != -1
        
    def moveWest(self,coord):
        if self.canMoveWest():
            coord[1] = (coord[1]-1) % Maze.WIDTH
        return self.maze[coord[0]][coord[1]]==1;
        
    def moveEast(self,coord):
        if self.canMoveEast():
            coord[1] = (coord[1]+1) % Maze.WIDTH
        return self.maze[coord[0]][coord[1]]==1;
        
    def moveSouth(self,coord):
        if self.canMoveSouth():
            coord[0] = (coord[0]+1) % Maze.HEIGHT
        return self.maze[coord[0]][coord[1]]==1;
        
    def moveNorth(self,coord):
        if self.canMoveNorth():
            coord[0] = (coord[0]-1) % Maze.HEIGHT
        return self.maze[coord[0]][coord[1]]==1;
    
    