# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:24:02 2022

@author: Elliot
"""

import random


class Drunk:
    def __init__(self, envir, drunks, house):
        """Drunk Constructor.

                Once parameters are created they are passed into function.
                Attributing characteristics to constructor.

                Parameters
                ----------

                envir: int
                2D List.

                drunks: list of drunks in Model.py
                These are the drunks in Model.py

                Self.is_at_home is an att therefore is not called
                ------

                Returns
                -------
                None.
                """
        self.env = envir
        self.agents = drunks
        self.x = 150  # Starting point of all drunks
        self.y = 137
        self.house = house
        self.is_at_home = False

    def move_up(self):
        """
                        Defining movement.

                        Functions
                        ----------
                        move_up - if self.y is greater than the shape of the environment
                        self.y would be set to zero.
                        (if y position goes beyond map. y goes through the opposite side)

                        Returns
                        -------
                        None
                """
        self.y += 1
        if self.y >= self.env.shape[1]:
            self.y = 0

    def move_down(self):
        """
        move_down - if y moves down and out of bounds y = the shape of the environment minus 1.
                        Because columns in data is counted from zero
                        Therefore 299 columns (300) and gets y to come through opposite side.
                        ------
        :return:
        None
        """
        self.y -= 1
        if self.y < 0:
            self.y = self.env.shape[1] - 1

    def move_left(self):
        """
        move_left - if x moves left and out of bounds, function beings it through opposite side.
        :return:
        None
        """
        self.x -= 1
        if self.x < 0:
            self.x = self.env.shape[0] - 1

    def move_right(self):
        """
        move-right - if x moves right and out of bounds, function brings it through opposite side.
        :return:
        """
        self.x += 1
        if self.x >= self.env.shape[0]:
            self.x = 0

    def move(self):
        """
                Defining movement.

                Functions
                ----------
                move_up - if random number generated between 0 and 3 is equals to 0 move up
                move_down - if random number generated between 0 and 3 is equals to 1 move down
                move_left - if random number generated between 0 and 3 is equals to 2 move left
                move_right - if random number generated between 0 and 3 is equals to 0 move right
                ------

                Returns
                -------
                self.x
                self.y

        """
        location = random.randint(0, 3)
        if location == 0:
            self.move_up()

        elif location == 1:
            self.move_down()

        elif location == 2:
            self.move_left()
        else:
            self.move_right()

    def steps(self, y, x):
        """
               Defining movement.

               Functions
               ----------
               Add 1 to the environment with every step. Helps Identify where agents were.
               ------
               Returns
               -------
                None
        """
        self.env[y][x] += 1
