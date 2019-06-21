#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Noeud(object):
    
    def __init__(self,nom):
        self.nom = nom
        self.enfants = []
        self.marque = False
        
    def ajouterEnfant(self,enfant):
        self.enfants.append(enfant)
        
    def parcours(self):
        self.marque = True
        print(self.nom)
        for enfant in self.enfants:
            if not enfant.marque:
                enfant.parcours()


if __name__=="__main__":
    
    a = Noeud("A")
    b = Noeud("B")
    c = Noeud("C")
    d = Noeud("D")
    e = Noeud("E")
    f = Noeud("F")
    
    a.ajouterEnfant(b)
    a.ajouterEnfant(c)
    a.ajouterEnfant(d)
    
    b.ajouterEnfant(a)
    b.ajouterEnfant(e)
    
    c.ajouterEnfant(b)
    
    e.ajouterEnfant(f)
    e.ajouterEnfant(d)
    
    a.parcours()
    