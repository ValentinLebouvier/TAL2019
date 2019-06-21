#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

class Robot(object):
    
    TIME_AllerCube = 5
    TIME_PrendreCube = 2
    TIME_AllerObjectif = 8
    TIME_DeposerCube = 2
    
    def __init__(self):
        self.time1=0
        self.time2=0
        self.time3=0
        self.time4=0
        
        
    def allerCube(self):
        if self.time1==0:
            self.time1 = time.time()
        if self.time1+Robot.TIME_AllerCube<= time.time():
            print("AllerCube : Succès")
            return True
        print("AllerCube : En Cours")
        return None
    
    def prendreCube(self):
        if self.time2==0:
            self.time2 = time.time()
        if self.time2+Robot.TIME_PrendreCube <= time.time():
            print("PrendreCube : Succès")
            return True
        print("PrendreCube : En Cours")
        return None
    
    def allerObjectif(self):
        if self.time3==0:
            self.time3 = time.time()
        if self.time3+Robot.TIME_AllerObjectif <= time.time():
            print("AllerObjectif : Succès")
            return True
        print("AllerObjectif : En Cours")
        return None
    
    def deposerCube(self):
        if self.time4==0:
            self.time4 = time.time()
        if self.time4+Robot.TIME_DeposerCube <= time.time():
            print("DeposerCube : Succès")
            return True
        print("DeposerCube : En Cours")
        return None
    