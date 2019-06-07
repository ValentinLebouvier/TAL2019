#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:49:52 2019

@author: valentinlebouvier
"""
import py_trees
import time
import toolkit as tool
from PacManEngine import PacManEngine
from PacManView import PacManView


class PacManController(object):
    
    def __init__(self,nbPacmans=1,nbGhosts=1,speed=0.5):
        blackboard = py_trees.blackboard.Blackboard()
        blackboard.times = {}
        for v in ["Alone","Perdu","Gagné","Goto Pill","Random 1/2","Random 1/3","Random 1/4","No West Wall","No East Wall","No North Wall","No South Wall","Move West","Move East","Move South","Move North","EOG","Goto Pacman","Stop Ghost","Not Alone"]:
            blackboard.times[v] = []
        
        self.engine = PacManEngine(nbPacmans,nbGhosts,speed)
        self.view = PacManView(self.engine,self)
        self.speed = speed
        
        self.bt, parallel = tool.createGameBTHeader(self.engine)
        
        for idP in range(nbPacmans):
            btPacman = tool.createPillSeeking(self.engine,"Pacman"+str(idP))
            bt = tool.addNoSuccessOverflow(btPacman)
            parallel.add_child(bt)
        for idG in range(nbGhosts):
            btGhost = tool.createPacmanChase(self.engine,"Ghost"+str(idG))
            bt = tool.addNoSuccessOverflow(btGhost)
            parallel.add_child(bt)
        
        self.snapshot_visitor = py_trees.visitors.SnapshotVisitor()
        self.bt.visitors.append(self.snapshot_visitor)
        
        self.bt.setup(timeout=15)
    
    
    def start(self):
        try:
            self.bt.tick_tock(
                self.speed*1000,
                py_trees.trees.CONTINUOUS_TICK_TOCK,
                None,
                None #lambda x: print(py_trees.display.ascii_tree(self.bt.root,self.snapshot_visitor))
            )
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
        self.stop()

    
    def stop(self):
        self.bt.interrupt()
        self.engine.stop()
        self.view.stop()
        

if __name__=="__main__":
    
    controller = PacManController(speed=0.05)
    controller.start()