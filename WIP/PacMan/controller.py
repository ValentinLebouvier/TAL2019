#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import py_trees
import threading
import toolkit as tool


class PacManController(threading.Thread):
    
    def __init__(self,model,speed=None):
        threading.Thread.__init__(self)
        
        self.model = model
        self.subscribers = [model]
        if speed is None:
            self.speed = self.model.gameSpeed * 1000
        else :
            self.speed = speed*1000
        
        self.bt, parallel = tool.createGameBTHeader(self.model)
        
        for idP in range(self.model.nbPacmans):
            btPacman = tool.createPillSeeking(self.model,"Pacman"+str(idP))
            bt = tool.addNoSuccessOverflow(btPacman)
            parallel.add_child(bt)
        for idG in range(self.model.nbGhosts):
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
                self.speed,
                py_trees.trees.CONTINUOUS_TICK_TOCK,
                None,
                None #lambda x: print(py_trees.display.ascii_tree(self.bt.root,self.snapshot_visitor))
            )
        except KeyboardInterrupt:
            self.stop()
            
    
    def stop(self):
        self.bt.interrupt()
        for s in self.subscribers:
            s.stop()
    
    def subscribe(self, subs):
        self.subscribers.append(subs)
