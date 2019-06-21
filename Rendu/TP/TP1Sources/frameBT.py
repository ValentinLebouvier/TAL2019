#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import py_trees
import toolkit as tool
from robot import Robot

if __name__=="__main__":
    
    robot = Robot()
    
    speed = 500 #ms
    
    #racine = 
    
    bt = py_trees.trees.BehaviourTree(racine)
    
    stop = tool.Action()
    stop.setAction(bt.interrupt)
    
    #Construction Behaviour Tree
    
    
    bt.setup(timeout=15)
    
    try:
        bt.tick_tock(
            speed,
            py_trees.trees.CONTINUOUS_TICK_TOCK,
            None,
            None
        )
    except KeyboardInterrupt:
        print("Interruption")