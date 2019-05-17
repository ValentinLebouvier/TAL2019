#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:08:11 2019

@author: valentinlebouvier
"""

from Maze import Maze
from Characters import PacMan


class PacManEngine(object):
    
    def __init__(self):
        self.maze = Maze()
        self.pacman = PacMan(1,1,self.maze)
        
    def noMorePills(self):
        return self.maze.hasNoPill()
    
    def hasLost(self):
        return False
    
    def hasWon(self):
        return not(self.hasLost()) and self.noMorePills()

    
    
