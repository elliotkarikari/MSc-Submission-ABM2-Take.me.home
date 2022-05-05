# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:01:10 2022

@author: Elliot
"""


# Imports Libraries 
import Environment
import matplotlib.pyplot as plt
import Framework



#Defining Variables 


#Reads in environment
environ = Environment.readEnvironment()

#Show environment
plt.ylim(0, 300)
plt.xlim(0, 300)
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
plt.imshow(environ)



 
