#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import py_trees

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

