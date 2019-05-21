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
    
    Directions = {
            "West" : (0,-1),
            "East" : (0,1),
            "North" : (-1,0),
            "South" : (1,0)
                  }
    ReverseDirections = {
            (0,0):None,
            (0,-1):"West",
            (0,1):"East",
            (-1,0):"North",
            (1,0):"South"
            }
    
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
        self.nbOfPills = sum(1 for x in range(self.height) for y in range(self.width) if self.hasPill(x,y))
        self.createGraph()
        
    def createGraph(self):
        self.graph = nx.Graph()
        sommets = [(x,y) for x in range(self.height) for y in range(self.width) if not self.isWall(x,y)]
        self.graph.add_nodes_from(sommets)
        edges = [(coord1,coord2,1) for coord1 in sommets for coord2 in sommets if self.isNextTo(coord1,coord2)]
        self.graph.add_weighted_edges_from(edges)
    
    def isNextTo(self,coord1,coord2):
        return ( 
                (coord1[0]==coord2[0] and (coord1[1]==(coord2[1]+1)%self.width or coord1[1]==(coord2[1]-1)&self.width))
                or (coord1[1]==coord2[1] and (coord1[0]==(coord2[0]+1)%self.height or coord1[0]==(coord2[0]-1)%self.height))
                )
                
        
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
        path = nx.astar_path(self.graph,coordStart,coordEnd)
        firstStep = (path[1][0]-coordStart[0],path[1][1]-coordStart[1])
        return Maze.ReverseDirections[firstStep]
        
    
    def closestPill(self, coord):
        adjs = [adj for adj in self.graph[coord].keys()]
        i=0
        while i<len(adjs):
            adj = adjs[i]
            if self.hasPill(adj[0],adj[1]):
                return adj
            adjs = adjs+[a for a in self.graph[adj].keys() if not a in adj]
            i +=1
        return None
        
    
    def closestPowerPill(self, coord):
        pass
    
    def canSee(self, coordStart, coordEnd):
        if coordStart[0]==coordEnd[0]:
            for y in range(coordStart[1],coordEnd[1]):
                if self.isWall(coordStart[0],y):
                    return False
            return True
        elif coordStart[1]==coordEnd[1]:
            for x in range(coordStart[0],coordEnd[0]):
                if self.isWall(x, coordStart[1]):
                    return False
            return True
        return False
        
                       
                       
            
    