#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:24:36 2019

@author: valentinlebouvier
"""
from PacManModel import PacManModel
from PacManController import PacManController
from PacManView import PacManView


model = PacManModel()
controller = PacManController(model)
view = PacManView(model,controller)
