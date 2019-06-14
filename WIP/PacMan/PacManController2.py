# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:49:52 2019

@author: valentinlebouvier
"""
import py_trees
import time
import threading
import toolkit as tool
from PacManModel import PacManModel
from PacManView import PacManView


class PacManController(threading.Thread):
    
    def __init__(self,model,nbPacmans=1,nbGhosts=1,speed=0.5):
        threading.Thread.__init__(self)
        blackboard = py_trees.blackboard.Blackboard()
        blackboard.times = {}
        for v in ["Alone","Perdu","Gagné","Goto Pill","Random 1/2","Random 1/3","Random 1/4","No West Wall","No East Wall","No North Wall","No South Wall","Move West","Move East","Move South","Move North","EOG","Goto Pacman","Stop Ghost","Not Alone"]:
            blackboard.times[v] = []
        
        self.model = model
        self.subscribers = [model]
        self.speed = speed
        
        self.bt, parallel = tool.createGameBTHeader(self.model)
        
        for idP in range(nbPacmans):
            btPacman = tool.createPillSeeking(self.model,"Pacman"+str(idP))
            bt = tool.addNoSuccessOverflow(btPacman)
            parallel.add_child(bt)
        for idG in range(nbGhosts):
            btGhost = tool.createPacmanChase(self.model,"Ghost"+str(idG))
            bt = tool.addNoSuccessOverflow(btGhost)
            parallel.add_child(bt)
        
        self.snapshot_visitor = py_trees.visitors.SnapshotVisitor()
        self.bt.visitors.append(self.snapshot_visitor)
        
        self.bt.setup(timeout=15)
        
        self.start()
    
    
    def run(self):
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
        for s in self.subscribers:
            s.stop()
    
    def subscribe(self, subs):
        self.subscribers.append()
