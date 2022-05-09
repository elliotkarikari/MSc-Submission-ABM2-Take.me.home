# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:24:02 2022

@author: Elliot
"""

import random

class Drunk():
    def __init__(self, envir,drunks):
        """Agent Constructor.  
        
        If parameters aren't passes contrastor doesn't work. 
        
        Parameters
        ----------
        i: int 
        identity of agent
        
        environ: int
        List of list (2D list) containing numbers.
        
        drunks: list 
        list of drunks in Model.py
        These are the drunks in Model.py
        
        x: int 
        x position scrapped from website
        
        y: int 
        y position scrapped from website
        ------
        
        Returns
        -------
        None.
        """    
       
        self.env = envir
        self.agents = drunks
        self.x = 150# Starting point of all drunks
        self.y = 137 
        self.is_at_home = False
        
        
    def move_up(self):
      self.y += 1 % 300
      return self.x, self.y
    
    def move_down(self):
      self.y -= 1 % 300
      return self.x, self.y
    
    def move_left(self):
      self.x -= 1 % 300
      return self.x, self.y
    
    def move_right(self):
     self.x += 1 % 300
     return self.x,self.y
    
    # move
    # list [0-3]
    # Generate a random num between 0 and 3
    # if the random number == 0
    # move_up()
        
    def move(self):
                                
        if random.randint(0,3) == 0:
            x,y = self.move_up()
            return x,y
        elif random.randint(0,3) == 1:
            x,y = self.move_down()
            return x,y
        elif random.randint(0,3) == 2:
            x,y = self.move_left()
            return x,y
        else:
            x,y =self.move_right()
            return x,y       
                         
    

