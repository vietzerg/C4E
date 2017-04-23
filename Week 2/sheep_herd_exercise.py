# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 08:26:41 2017

@author: PA
"""

import random

sheep_herd = [ random.randrange(1,400) for i in range(7) ]

#print (sheep_herd)

def shear_sheep_and_grow(your_sheep_herd, n_grow):
    max_sheep = max(your_sheep_herd)
    print ("Hello, my name is Viet Zerg and these are my sheep sizes:\n",your_sheep_herd)
    print ("Now my biggest sheep has size",max_sheep,"let's shear it!")
    your_sheep_herd[your_sheep_herd.index(max_sheep)] = 8
    print ("After the initial sheering, here is my flock\n",your_sheep_herd,"\n")
    
    for month in range(1,n_grow+1):
        your_sheep_herd = [ sheep + 50 for sheep in your_sheep_herd ]
        print ("MONTH {}:".format(month))
        print ("One month has passed, now here is my flock in month {}\n".format(month), your_sheep_herd)
        if month < n_grow:
            max_sheep = max(your_sheep_herd)
            print ("Now my biggest sheep has size",max_sheep,"let's shear it!")
            your_sheep_herd[your_sheep_herd.index(max_sheep)] = 8
            print ("OK, after sheering, here is my flock\n",your_sheep_herd,"\n")
     
    sum_sheep = sum(your_sheep_herd)    
    print ("My flock has size in total: {}".format(sum_sheep))
    print ("I would get {0} * 2$ = {1}$".format(sum_sheep,sum_sheep*2))
        
shear_sheep_and_grow(sheep_herd, 4)