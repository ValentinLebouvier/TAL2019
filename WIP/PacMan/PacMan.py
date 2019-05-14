#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:08:11 2019

@author: valentinlebouvier
"""

import py_trees


class PacMan(py_trees.blackboard.Blackboard):
    
    
    def Reset():
        self.maze = Maze()