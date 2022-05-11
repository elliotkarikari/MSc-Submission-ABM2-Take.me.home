"""
__version__  1.0

This model is executed using a graphical user interface with a run menu.
When you run this code, a window should appear on your computer screen.
To run the model, navigate to this window and choose run from the menu bar.
To end the modl running choose the clear button in the menu bar.
"""
# Imports Libraries


import csv
import random
import tkinter
from sys import argv

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from Framework import Drunk
from Environment import Environment

'''
Step 1: Set-up parameters
'''

print("Step 1: Set-up parameters")
print("This is the name of the script: ", argv[0])

num_of_drunks = 25
num_of_iterations = 500
print("Number of arguments: ", len(argv))

'''
Step 2: Set-up environment this will contain data about the spatial 
environment in which agents act.

'''

print("Step 2: Set-up environment")
# Reads in environment
env = Environment()
envir = env.read_environment()
print(envir.shape)

'''
Step 3: Set-up agents.
'''
print("Step 3: Create drunks.")
# Defining Variables
drunks = []
# Make the drunks.
for i in range(num_of_drunks):
    # Houses are identified in increments of 10 From 10 to 250.
    home = ((1 + i) * 10)
    drunks.append(Drunk(envir, drunks, home))


print("Step 4: Animate drunks.")
'''
Step 4: Animate drunks. 

Find location. 
If location is not equal to drunks house and drunk is_at_home is equals to false,
drunks keep moving and steps are traced. 
When drunks is_at_home = True drunks stop moving

Parameters
----------
frames : int,
    Number of times frames after which canvas is cleared and redrawn 
------
'''


def update(frames):
    """Update function largely controls animation.
        frames display numer of iterations run on screen.

        Parameters
        ----------
        frame_number : int,
            Number of frames - frame is cleared and redrawn after given frame number.
        ------
        """
    fig.clear()
    global carry_on

    for j in range(num_of_drunks):
        location = envir[drunks[j].y][drunks[j].x]

        if location != drunks[j].house and drunks[
            j].is_at_home == False:  # Assigning False to drunks when location is not house
            drunks[j].move()
            drunks[j].steps(drunks[j].y, drunks[j].x)
        else:
            print(str("drunk  at House No. " + str(drunks[j].house) + " is at home"))
            drunks[j].is_at_home = True  # change value to True. Checking if equal

    if random.random() < 0.1:
        carry_on = False
    else:
        carry_on = True

        plt.ylim(0, 300)
        plt.xlim(0, 300)
        plt.imshow(envir, cmap="afmhot")
        plt.xlabel("Drunks stop moving when home")
        plt.title(label="Likely routes home after a good time at the pub",
                  loc="center",
                  fontstyle='italic')

        # Plot drunks

        for a in range(num_of_drunks):
            plt.scatter(drunks[a].x, drunks[a].y)
            plt.show()


'''
Step 5: GUI Parameters.
'''
print("Step 5: Set-Up GUI")
carry_on = True
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

""" Run function runs simulation.  
    Quit function quits animation
    save density function writes density info to csv file
    ----------
    Parameters
    ----------
    Does not take any parameters.
    """


def run():
    """ Run function runs simulation.
        ----------
        Parameters
        ----------
        Does not take any parameters.
        """
    print("Step 6: Animation.")
    global animation

    animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=500)
    canvas.draw()


def stop():
    """
    Quit function quits animation
    :return:
    None
    """
    quit()


def save_density():
    """
    Save density function writes density info to csv file
    :return:
    None
    """
    with open('environment_density.csv', 'w', newline='') as f:
        csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in envir:
            csvwriter.writerow(row)
        print("You have successfully run this model."
          "Density saved")


root = tkinter.Tk()
root.wm_title("Planning for Drunks")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root, )
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal")
model_menu.add_command(label="Clear model", command=stop, state="normal")
model_menu.add_command(label="Save Density", command=save_density, state="normal")

tkinter.mainloop()


