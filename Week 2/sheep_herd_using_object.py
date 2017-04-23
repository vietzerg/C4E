# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 10:23:54 2017

@author: PA
"""

import random

# CREATE AN OBJECT FOR SHEEPS, WHICH HAS KEYS AND VALUES TO KEEP TRACK OF THE SHEEP HERD

def create_sheep_herd():
    name = input("Hello, what's your name? ")
    many = int(input("How many sheeps do you want to have? "))
    max_size = int(input("How big is the biggest sheep? "))
    sheep_herd_created = dict(sheep_size = list(random.sample(range(1,max_size), many)), month = 0, owner = name)
    print ("\nHello, {}, your sheep herd has been generated as follows\n".format(name),sheep_herd_created)
    return sheep_herd_created

def shear_sheeps(your_sheep_herd):
    max_sheep = max(your_sheep_herd["sheep_size"])
    print ("\nHello, my name is {} and these are my sheep sizes:\n".format(your_sheep_herd["owner"]),your_sheep_herd["sheep_size"])
    print ("Now my biggest sheep has size",max_sheep,"let's shear it!")
    your_sheep_herd["sheep_size"][your_sheep_herd["sheep_size"].index(max_sheep)] = 8
    print ("After the initial sheering, here is my flock\n",your_sheep_herd["sheep_size"],"\n")
    return your_sheep_herd

def grow(your_sheep_herd):
        your_sheep_herd["sheep_size"] = [ sheep + 50 for sheep in your_sheep_herd["sheep_size"] ]
        your_sheep_herd["month"] += 1
        print ("\nMONTH {}:".format(your_sheep_herd["month"]))
        print ("One month has passed, now here is my flock in month {}\n".format(your_sheep_herd["month"]), your_sheep_herd["sheep_size"])

def sell_sheeps(your_sheep_herd):
    sum_sheep = sum(your_sheep_herd["sheep_size"])    
    print ("My flock has size in total: {}".format(sum_sheep))
    print ("I would get {0} * 2$ = {1}$".format(sum_sheep,sum_sheep*2))
    

#TESTING AREA
sheep_herd = create_sheep_herd()
shear_sheeps(sheep_herd)
grow(sheep_herd)
grow(sheep_herd)
grow(sheep_herd)
print (sheep_herd)