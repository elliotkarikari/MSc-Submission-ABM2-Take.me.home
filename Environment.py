# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:01:20 2022

@author: Elliot
"""

"""
CSV containing details of raster grid is imported and read into model
It goes through data rows and appends it to our environment list. 
Thus creating our environment
"""

import pandas as pd


class Environment:
    def __init__(self):
        """Environment Constructor.

                Environment is made empty and read in with readEnvironment function
                drunk-data.to_numpy -
                get_location -
                Environment test finds all pixel identified as pubs and houses
                Parameters
                ----------
                None.
                ------
                Returns
                -------
                None.
        """
        self.environment = None

    # Function creating Environment
    def read_environment(self):
        # Load csv file into a Dataframe
        drunkdata = pd.read_csv('drunk.csv')

        # Convert Dataframe into a numpy array
        self.environment = drunkdata.to_numpy()
        print(self.environment)
        return self.environment

    # Find all pubs Test
    # pubs = 0
    # for i in range(len(environment)):
    #   for j in range(len(environment)):
    #      if environment[i][j] == 1:
    #          pubs += 1
    #           # print(i,j)
    #           # print("Pub")
    #      #print("Number of pubs: ", pubs)

    #     # Find all houses Test
    # house = 0
    # for i in range(len(environment)):
    #   for j in range(len(environment)):

    #     if environment[i][j] >=10 or environment[i][j]<=250:
    #       house += 1
    #           # print(i,j)
    #           # print("Home")
    #     #print("Number of houses: ", house)
