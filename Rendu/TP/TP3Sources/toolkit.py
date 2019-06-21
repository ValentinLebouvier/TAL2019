#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import py_trees
from random import random


class Action(py_trees.behaviour.Behaviour):
    
    def setAction(self,fonction,argument="No Argument"):
        self.action = fonction
        self.argument = argument
    
    def update(self):
        status = py_trees.common.Status.RUNNING
        if self.argument=="No Argument":
            res = self.action()
        else:
            res = self.action(self.argument)
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
        if self.argument is None:
            res = self.condition()
        else:
            res = self.condition(self.argument)
        if res:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE


def addNoSuccessOverflow(bt):
    decorateurCondition = py_trees.decorators.Condition(bt,"",py_trees.common.Status.FAILURE)
    decorateurInversion = py_trees.decorators.Inverter(decorateurCondition,"")        
    return decorateurInversion

def createGameBTHeader(model):
    perdu = Condition("Gagné")
    perdu.setCondition(model.hasLost)
    
    gagne = Condition("Perdu")
    gagne.setCondition(model.hasWon)
    
    
    sequence = py_trees.composites.Sequence("→")
    bt = py_trees.trees.BehaviourTree(sequence)


    endOfGame = Action("EOG")
    endOfGame.setAction(endGame,(model,bt))
    
    parallel= py_trees.composites.Parallel("⇉",py_trees.common.ParallelPolicy.SuccessOnOne())
    
    selector = py_trees.composites.Selector("?",[gagne,perdu,parallel])
    
    sequence.add_children([selector,endOfGame])
    
    return bt, parallel


def createEquiprobable(model,character):
    if character in model.PacmanList.keys():
        c = model.PacmanList.get(character)
    else:
        c = model.GhostList.get(character)
    
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
    random4.setCondition(choose_1st_over,4)
    
    random3 = Condition("Random 1/3")
    random3.setCondition(choose_1st_over,3)
    
    random2 = Condition("Random 1/2")
    random2.setCondition(choose_1st_over,2)
    
    
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
    
    return decorateurInversion

def createPillSeeking(model, character):
    c = model.PacmanList.get(character)

    selector = py_trees.composites.Selector("?")
    
    gotoPill = Action("Goto Pill")
    gotoPill.setAction(c.gotoPill)
    guard = py_trees.decorators.EternalGuard(child=gotoPill,condition=c.isAlone)
    
    notAlone = createEquiprobable(model,character)
    
    selector.add_children([guard,notAlone])
    
    return selector

def createPacmanChase(model, character):
    c = model.GhostList.get(character)

    selector = py_trees.composites.Selector("?")
    
    isNotAlone = Condition("Not Alone")
    isNotAlone.setCondition(lambda :not(c.isAlone()))
    
    gotoPacman = Action("Goto Pacman")
    gotoPacman.setAction(c.chase)
    
    alone = Action("Stop Ghost")
    alone.setAction(c.setDirection,None)
    blocker = py_trees.decorators.Condition(alone,status=py_trees.common.Status.FAILURE)
    
    sequence = py_trees.composites.Sequence("→",[isNotAlone,gotoPacman])

    selector.add_children([sequence, blocker])
    
    return selector

def choose_1st_over(n):
    return random()<(1/n)

def endGame(args):
    print("END OF GAME")
    args[1].interrupt()
    if (args[0].hasWon()):
        print("Pacman a gagné")
    else:
        print("Pacman a perdu")

mazeTileset = [".","o","▓"]