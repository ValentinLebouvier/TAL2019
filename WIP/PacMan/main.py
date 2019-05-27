#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:56:01 2019

@author: valentinlebouvier
"""

from PacManEngine import PacManEngine
from PacManView import PacManView
from random import random
import py_trees
import time

class Action(py_trees.behaviour.Behaviour):
    
    def setAction(self,fonction,argument=None):
        self.action = fonction
        self.argument = argument
    
    def update(self):
        blackboard = py_trees.blackboard.Blackboard()
        status = py_trees.common.Status.RUNNING
        tStart = time.time()
        if self.argument is None:
            res = self.action()
        else:
            res = self.action(self.argument)
        tEnd = time.time()
        blackboard.times[self.name].append(tEnd-tStart)
        if res is True:
            status = py_trees.common.Status.SUCCESS
        elif res is False:
            status = py_trees.common.Status.FAILURE
        return status


class Condition(py_trees.behaviour.Behaviour):
    
    def setCondition(self, condition, argument=None):
        self.condition = condition
        self.argument = argument
    
    def update(self):
        blackboard = py_trees.blackboard.Blackboard()
        tStart = time.time()
        if self.argument is None:
            res = self.condition()
        else:
            res = self.condition(self.argument)
        tEnd = time.time()
        blackboard.times[self.name].append(tEnd-tStart)
        if res:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE


def random1_4():
    rng = random()
    return rng<.25

def random1_3():
    return random()<.33

def random1_2():
    return random()<.5

def createEquiprobableBT(engine,character):
    if character in engine.PacmanList.keys():
        c = engine.PacmanList.get(character)
    else:
        c = engine.GhostList.get(character)
    
    goWest = Action("Move West")
    goWest.setAction(c.setDirection,"West")
    
    goEast = Action("Move East")
    goEast.setAction(c.setDirection,"East")
    
    goSouth = Action("Move South")
    goSouth.setAction(c.setDirection,"South")
    
    goNorth = Action("Move North")
    goNorth.setAction(c.setDirection,"North")
    
    noWestWall = Condition("No West Wall")
    noWestWall.setCondition(c.canGo, "West")
    
    noEastWall = Condition("No East Wall")
    noEastWall.setCondition(c.canGo, "East")
    
    noSouthWall = Condition("No South Wall")
    noSouthWall.setCondition(c.canGo,"South")
    
    noNorthWall = Condition("No North Wall")
    noNorthWall.setCondition(c.canGo, "North")
   
    
    random4 = Condition("Random 1/4")
    random4.setCondition(random1_4)
    
    random3 = Condition("Random 1/3")
    random3.setCondition(random1_3)
    
    random2 = Condition("Random 1/2")
    random2.setCondition(random1_2)
    
    
    sequenceW4 = py_trees.composites.Sequence("→",[random4,goWest])
    
    sequenceW3 = py_trees.composites.Sequence("→",[random3,goWest])
    sequenceE3 = py_trees.composites.Sequence("→",[random3,goEast])
    
    sequenceW2 = py_trees.composites.Sequence("→",[random2,goWest])
    sequenceE2 = py_trees.composites.Sequence("→",[random2,goEast])
    sequenceN2 = py_trees.composites.Sequence("→",[random2,goNorth])
    
    selector11 = py_trees.composites.Selector("?")
    
    selector21 = py_trees.composites.Selector("?")
    selector22 = py_trees.composites.Selector("?")
    
    selector31 = py_trees.composites.Selector("?")
    selector32 = py_trees.composites.Selector("?")
    selector33 = py_trees.composites.Selector("?")
    selector34 = py_trees.composites.Selector("?")
    
    selector41 = py_trees.composites.Selector("?")
    selector42 = py_trees.composites.Selector("?")
    selector43 = py_trees.composites.Selector("?")
    selector44 = py_trees.composites.Selector("?")
    selector45 = py_trees.composites.Selector("?")
    selector46 = py_trees.composites.Selector("?")
    selector47 = py_trees.composites.Selector("?")
    
    selectorWENS = py_trees.composites.Selector("?")
    selectorWEN = py_trees.composites.Selector("?")
    selectorWES = py_trees.composites.Selector("?")
    selectorWNS = py_trees.composites.Selector("?")
    selectorWN = py_trees.composites.Selector("?")
    selectorWE = py_trees.composites.Selector("?")
    selectorWS = py_trees.composites.Selector("?")
    selectorENS = py_trees.composites.Selector("?")
    selectorEN = py_trees.composites.Selector("?")
    selectorES = py_trees.composites.Selector("?")
    selectorNS = py_trees.composites.Selector("?")
    
    
    
    sequenceW = py_trees.composites.Sequence("→",[noWestWall,selector21])
    sequenceE = py_trees.composites.Sequence("→",[noEastWall,selector33])
    sequenceE_W = py_trees.composites.Sequence("→",[noEastWall,selector31])
    sequenceN = py_trees.composites.Sequence("→",[noNorthWall,selector47])
    sequenceN_W = py_trees.composites.Sequence("→",[noNorthWall,selector43])
    sequenceN_E = py_trees.composites.Sequence("→",[noNorthWall,selector45])
    sequenceN_WE = py_trees.composites.Sequence("→",[noNorthWall,selector41])
    sequenceS_W = py_trees.composites.Sequence("→",[noSouthWall,selectorWS])
    sequenceS_E = py_trees.composites.Sequence("→",[noSouthWall,selectorES])
    sequenceS_N = py_trees.composites.Sequence("→",[noSouthWall,selectorNS])
    sequenceS_WE = py_trees.composites.Sequence("→",[noSouthWall,selectorWES])
    sequenceS_WN = py_trees.composites.Sequence("→",[noSouthWall,selectorWNS])
    sequenceS_EN = py_trees.composites.Sequence("→",[noSouthWall,selectorENS])
    sequenceS_WEN = py_trees.composites.Sequence("→",[noSouthWall,selectorWENS])
    
    
    selector11.add_children([sequenceW,selector22])
    
    selector21.add_children([sequenceE_W,selector32])
    selector22.add_children([sequenceE,selector34])
    
    selector31.add_children([sequenceN_WE,selector42])
    selector32.add_children([sequenceN_W,selector44])
    selector33.add_children([sequenceN_E,selector46])
    selector34.add_children([sequenceN,goSouth])
    
    selector41.add_children([sequenceS_WEN,selectorWEN])
    selector42.add_children([sequenceS_WE,selectorWE])
    selector43.add_children([sequenceS_WN,selectorWN])
    selector44.add_children([sequenceS_W,goWest])
    selector45.add_children([sequenceS_EN,selectorEN])
    selector46.add_children([sequenceS_E,goEast])
    selector47.add_children([sequenceS_N,goNorth])
    
    selectorWENS.add_children([sequenceW4,sequenceE3,sequenceN2,goSouth])
    selectorWEN.add_children([sequenceW3,sequenceE2,goNorth])
    selectorWES.add_children([sequenceW3,sequenceE2,goSouth])
    selectorWNS.add_children([sequenceW3,sequenceN2,goSouth])
    selectorWN.add_children([sequenceW2,goNorth])
    selectorWE.add_children([sequenceW2,goEast])
    selectorWS.add_children([sequenceW2,goSouth])
    selectorENS.add_children([sequenceE3,sequenceN2,goSouth])
    selectorEN.add_children([sequenceE2,goNorth])
    selectorES.add_children([sequenceE2,goSouth])
    selectorNS.add_children([sequenceN2,goSouth])
    
    
    decorateurCondition = py_trees.decorators.Condition(selector11,"",py_trees.common.Status.FAILURE)
    decorateurInversion = py_trees.decorators.Inverter(decorateurCondition,"")
    
    bt = py_trees.trees.BehaviourTree(decorateurInversion)
    
    return bt

def createPillSeekingBT(engine,character):
    
    c = engine.PacmanList.get(character)
    
    selector = py_trees.composites.Selector("?")
    
    alone = Condition("Alone")
    alone.setCondition(c.alone)
    
    gotoPill = Action("Goto Pill")
    gotoPill.setAction(c.gotoPill)
    
    sequence = py_trees.composites.Sequence("→",[alone,gotoPill])
    random = createEquiprobableBT(engine,character).root
    
    selector.add_children([sequence,random])
    
    bt = py_trees.trees.BehaviourTree(selector)
    
    return bt



def endGame(args):
    
    print("END OF GAME")
    args[1].interrupt()
    if (args[0].hasWon()):
        print("Pacman a gagné")
    else:
        print("Pacman a perdu")
    


if __name__ == "__main__":
    
    blackboard = py_trees.blackboard.Blackboard()
    blackboard.times = {}
    for v in ["Alone","perdu","Gagné","Goto Pill","Random 1/2","Random 1/3","Random 1/4","No West Wall","No East Wall","No North Wall","No South Wall","Move West","Move East","Move South","Move North","EOG"]:
        blackboard.times[v] = []
    
    for i in range(1):
        engine = PacManEngine()
        view = PacManView(engine)
        
        engine.setView(view)
        
        perdu = Condition("perdu")
        perdu.setCondition(engine.hasLost)
        
        gagne = Condition("Gagné")
        gagne.setCondition(engine.hasWon)
        
        btPacman = createPillSeekingBT(engine,"Pacman")
        #btMsPacman = createEquiprobableBT(engine,"MsPacman")
        #btJrPacman = createEquiprobableBT(engine,"JrPacman")
        btPinky = createEquiprobableBT(engine,"Pinky")
        #btBlinky = createEquiprobableBT(engine,"Blinky")
        #btInky = createEquiprobableBT(engine,"Inky")
        #btClyde = createEquiprobableBT(engine,"Clyde")
        
        sequence = py_trees.composites.Sequence("→")
        
        bt = py_trees.trees.BehaviourTree(sequence)
        
        parallel = py_trees.composites.Parallel("⇉",py_trees.common.ParallelPolicy.SuccessOnOne(),[btPacman.root,btPinky.root])#,btMsPacman.root,btJrPacman.root,btPinky.root,btBlinky.root,btInky.root,btClyde.root])
        
        selector = py_trees.composites.Selector("?",[gagne,perdu,parallel])
        
        endOfGame = Action("EOG")
        endOfGame.setAction(endGame,(engine,bt))
        
        sequence.add_children([selector,endOfGame])
        
        bt.setup(timeout=15)
        try:
            bt.tick_tock(
                50,
                py_trees.trees.CONTINUOUS_TICK_TOCK,
                None,
                None
            )
        except KeyboardInterrupt:
            bt.interrupt()
        
        engine.stop()
        view.stop()
    
    for v in blackboard.times:
        if len(blackboard.times[v])!=0:
            print(v,sum(blackboard.times[v])/len(blackboard.times[v]))
    
