# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 10:23:54 2017

@author: PA
"""

import random

# CREATE AN OBJECT FOR SHEEPS, WHICH HAS KEYS AND VALUES TO KEEP TRACK OF THE SHEEP HERD
# (1) THERE IS A BUG IN LINE 17, WHERE randrange() DOES NOT ALLOW FOR EQUAL start AND stop VALUES
# 4/27/2017: I CHANGED THE randrange() TO randint() AND CHECKED IF IT WORKED. YEAH AND IT WORKED! I WAS A DUMB FOR NOT INCREMENTING THE max_size BY 1 SO THAT randrange() WILL INCLUDE THE
# max_size VALUE !!!
# BUG (1) RESOLVED.

def create_sheep_herd():
    name = input("Hello, what's your name? ")
    many = int(input("How many sheeps do you want to have? "))
    max_size = int(input("How big is the biggest sheep? "))
    sheep_herd_created = dict(sheep_size = [ random.randrange(1,max_size+1) for i in range(many) ], month = 0, owner = name)
    print ("\nHello, {}, your sheep herd has been generated as follows\n".format(name),sheep_herd_created)
    return sheep_herd_created

def shear_sheeps(your_sheep_herd):
    max_sheep = max(your_sheep_herd["sheep_size"])
    print ("\nHello, my name is {} and these are my sheep sizes:\n".format(your_sheep_herd["owner"]),your_sheep_herd["sheep_size"])
    print ("Now my biggest sheep(s) has size",max_sheep,"let's shear them!")
    if max_sheep > 8:
        
        # In case there are many sheeps with the maximum size
        
        for index, sheep in enumerate(your_sheep_herd["sheep_size"]):
            if sheep == max_sheep:
                your_sheep_herd["sheep_size"][index] = 8
        print ("After the initial sheering, here is my flock\n",your_sheep_herd["sheep_size"],"\n")
    else:
        print ("Oops. Sheeps in your herd are too small to shear!")
    return your_sheep_herd

def grow(your_sheep_herd):
        your_sheep_herd["sheep_size"] = [ sheep + 50 for sheep in your_sheep_herd["sheep_size"] ]
        your_sheep_herd["month"] += 1
        print ("\nMONTH {}:".format(your_sheep_herd["month"]))
        print ("One month has passed, now here is my flock in month {}\n".format(your_sheep_herd["month"]), your_sheep_herd["sheep_size"])

def sell_sheeps(your_sheep_herd):
    sum_sheep = sum(your_sheep_herd["sheep_size"])    
    print ("\nMy flock has size in total: {}".format(sum_sheep))
    print ("I would get {0} * 2$ = {1}$".format(sum_sheep,sum_sheep*2))
    

#TESTING AREA
sheep_herd = create_sheep_herd()
shear_sheeps(sheep_herd)
grow(sheep_herd)
grow(sheep_herd)
grow(sheep_herd)
shear_sheeps(sheep_herd)
sell_sheeps(sheep_herd)
print (sheep_herd)
