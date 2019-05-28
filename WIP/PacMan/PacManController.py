#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:49:52 2019

@author: valentinlebouvier
"""
import py_trees
import toolkit as tool
from PacManEngine import PacManEngine
from PacManView import PacManView


class PacManController(object):
    
    def __init__(self,nbPacmans=1,nbGhosts=1):
        blackboard = py_trees.blackboard.Blackboard()
        blackboard.times = {}
        for v in ["Alone","Perdu","Gagné","Goto Pill","Random 1/2","Random 1/3","Random 1/4","No West Wall","No East Wall","No North Wall","No South Wall","Move West","Move East","Move South","Move North","EOG"]:
            blackboard.times[v] = []
        
        self.engine = PacManEngine(nbPacmans,nbGhosts)
        self.view = PacManView(self.engine,self)
        
        self.bt, parallel = tool.createGameBTHeader(self.engine)
        
        for idP in range(nbPacmans):
            btPacman, notAlone = tool.createPillSeeking(self.engine,"Pacman"+str(idP))
            notAlone = tool.createEquiprobable(self.engine,"Pacman"+str(idP))
            parallel.add_child(btPacman)
        for idG in range(nbGhosts):
            btGhost = tool.createEquiprobable(self.engine,"Ghost"+str(idG))
            parallel.add_child(btGhost)
        
        self.bt.setup(timeout=15)
    
    
    def start(self):
        try:
            self.bt.tick_tock(
                500,
                py_trees.trees.CONTINUOUS_TICK_TOCK,
                None,
                None
            )
        except KeyboardInterrupt:
            self.stop()

    
    def stop(self):
        self.bt.interrupt()
        self.engine.stop()
        self.view.stop()
        

if __name__=="__main__":
    
    controller = PacManController()
    controller.start()