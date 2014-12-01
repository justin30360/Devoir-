#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pythonFonctionParallelepipede.py
#
# Ecrivez un programme qui convertisse en metres par seconde et en km/h
# une vitesse fournie par l'utilisateur en miles/heure
# Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#
#specifications
#parametre :
# aucun
#retour :
#
#
#
def entree():
#Les entrees du programme
print ("convertir des milles en km/h.\n")
v = float(input("indiquez la vitesse en milles:"))
return v
#specifications
#parametre :
# v un nombre reel representant une vitesse en milles
#retour
# k representant la vitesse en km/h
def metier(v):
#le calcul
k= v*1.609
return k
#specifications
def pourImpression(v):
#les sorties du programme
print ("\nLa vitesse en km/h est : "+str(v)+" km/h.")
print (" ---> Debut du programme.\n")
vitesse=entree()
vitesse=metier(vitesse)
pourImpression(vitesse)
print ("\n ---> Fin du programme.")

    Status
    API
    Training
    Shop
    Blog
    About

    © 2014 GitHub, Inc.
    Terms
    Privacy
    Security
    Contact

