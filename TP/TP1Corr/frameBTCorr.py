#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import py_trees
import toolkit as tool
from robot import Robot

if __name__=="__main__":
    
    robot = Robot()
    
    speed = 500 #ms
    
    #Construction Behaviour Tree
    
    racine =  py_trees.composites.Sequence()
    
    bt = py_trees.trees.BehaviourTree(racine)
    
    allerCube = tool.Action()
    allerCube.setAction(robot.allerCube)
    
    prendreCube = tool.Action()
    prendreCube.setAction(robot.prendreCube)
    
    allerObjectif = tool.Action()
    allerObjectif.setAction(robot.allerObjectif)
    
    deposerCube = tool.Action()
    deposerCube.setAction(robot.deposerCube)
    
    stop = tool.Action()
    stop.setAction(bt.interrupt)
    
    racine.add_children([allerCube,prendreCube,allerObjectif,deposerCube,stop])
    
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