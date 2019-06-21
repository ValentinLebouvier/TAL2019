#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model import PacManModel
from controller import PacManController
from view import PacManView


model = PacManModel()
controller = PacManController(model)
view = PacManView(model,controller)
