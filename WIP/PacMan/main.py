#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:56:01 2019

@author: valentinlebouvier
"""

from PacManEngine import PacManEngine
from random import random
import py_trees

class Action(py_trees.behaviour.Behaviour):
    
    def setAction(self,fonction):
        self.action = fonction
    
    def update(self):
        status = py_trees.common.Status.RUNNING
        res = self.action()
        if res is True:
            status = py_trees.common.Status.SUCCESS
        elif res is False:
            status = py_trees.common.Status.FAILURE
        return status


class Condition(py_trees.behaviour.Behaviour):
    
    def setCondition(self,condition):
        self.condition = condition
    
    def update(self):
        res = self.condition()
        if res:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE
        
def randomMoveWest():
    return random()<.25

def randomMoveEast():
    return random()<.75

def randomMoveSouth():
    return random()<1.

def randomMoveNorth():
    return random()<.5


def createPacManDeterministeBT(engine):
    root = py_trees.composites.Selector()
    
    noPills = py_trees.behaviour.Behaviour("NoMorePills")
    
    goWest = Action("Move West")
    goWest.setAction(engine.pacman.moveWest)
    
    goEast = Action("Move East")
    goEast.setAction(engine.pacman.moveEast)
    
    goSouth = Action("Move South")
    goSouth.setAction(engine.pacman.moveSouth)
    
    goNorth = Action("Move North")
    goNorth.setAction(engine.pacman.moveNorth)
    
    noWestWall = Condition("No West Wall")
    noWestWall.setCondition(engine.pacman.canGoWest)
    
    noEastWall = Condition("No East Wall")
    noEastWall.setCondition(engine.pacman.canGoEast)
    
    noSouthWall = Condition("No South Wall")
    noSouthWall.setCondition(engine.pacman.canGoSouth)
    
    noNorthWall = Condition("No North Wall")
    noNorthWall.setCondition(engine.pacman.canGoNorth)
    
    sequenceWest = py_trees.composites.Sequence("→",[noWestWall,goWest])
    sequenceEast = py_trees.composites.Sequence("→",[noEastWall,goEast])
    sequenceSouth = py_trees.composites.Sequence("→",[noSouthWall,goSouth])
    sequenceNorth = py_trees.composites.Sequence("→",[noNorthWall,goNorth])
    
    selector = py_trees.composites.Selector("?",[sequenceWest,sequenceNorth,sequenceEast,sequenceSouth])
    
    decorateurCondition = py_trees.decorators.Condition(selector,"",py_trees.common.Status.FAILURE)
    decorateurInversion = py_trees.decorators.Inverter(decorateurCondition,"")
    
    root.add_children([noPills,decorateurInversion])
    
    bt = py_trees.trees.BehaviourTree(root)
    
    return bt
    
def createPacManRandomBT(engine):
    root = py_trees.composites.Selector()
    
    noPills = py_trees.behaviour.Behaviour("NoMorePills")
    
    goWest = Action("Move West")
    goWest.setAction(engine.pacman.moveWest)
    
    goEast = Action("Move East")
    goEast.setAction(engine.pacman.moveEast)
    
    goSouth = Action("Move South")
    goSouth.setAction(engine.pacman.moveSouth)
    
    goNorth = Action("Move North")
    goNorth.setAction(engine.pacman.moveNorth)
    
    noWestWall = Condition("No West Wall")
    noWestWall.setCondition(engine.pacman.canGoWest)
    
    noEastWall = Condition("No East Wall")
    noEastWall.setCondition(engine.pacman.canGoEast)
    
    noSouthWall = Condition("No South Wall")
    noSouthWall.setCondition(engine.pacman.canGoSouth)
    
    noNorthWall = Condition("No North Wall")
    noNorthWall.setCondition(engine.pacman.canGoNorth)
    
    okMoveWest = Condition("Random Move West")
    okMoveWest.setCondition(randomMoveWest)
    
    okMoveEast = Condition("Random Move East")
    okMoveEast.setCondition(randomMoveEast)
    
    okMoveNorth = Condition("Random Move North")
    okMoveNorth.setCondition(randomMoveNorth)
    
    okMoveSouth = Condition("Random Move South")
    okMoveSouth.setCondition(randomMoveSouth)
    
    sequenceWest = py_trees.composites.Sequence("→",[noWestWall,okMoveWest,goWest])
    sequenceEast = py_trees.composites.Sequence("→",[noEastWall,okMoveEast,goEast])
    sequenceSouth = py_trees.composites.Sequence("→",[noSouthWall,okMoveSouth,goSouth])
    sequenceNorth = py_trees.composites.Sequence("→",[noNorthWall,okMoveNorth,goNorth])
    
    selector = py_trees.composites.Selector("?",[sequenceWest,sequenceNorth,sequenceEast,sequenceSouth])
    
    decorateurCondition = py_trees.decorators.Condition(selector,"",py_trees.common.Status.FAILURE)
    decorateurInversion = py_trees.decorators.Inverter(decorateurCondition,"")
    
    root.add_children([noPills,decorateurInversion])
    
    bt = py_trees.trees.BehaviourTree(root)
    
    return bt




if __name__ == "__main__":
    
    engine = PacManEngine()
    
    bt = createPacManRandomBT(engine)
    
    bt.setup(timeout=15)
    try:
        bt.tick_tock(
            500,
            py_trees.trees.CONTINUOUS_TICK_TOCK,
            None,
            None
        )
    except KeyboardInterrupt:
        bt.interrupt()
