# Imports Libraries
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter
import random
import matplotlib.animation as anim
from Framework import Drunk
from Environment import Environment
import csv

'''
Step 1: Initialise parameters
'''

print("Step 1: Initialise parameters")
num_of_drunks = 10
num_of_iterations = 500

'''
Step 2: Initialise environment this will contain data about the spatial 
environment in which agents act.

'''

print("Step 2: Initialise environment")
# Reads in environment
env = Environment()
envir = env.read_environment()
print(envir.shape)

'''
Step 3: Initialise agents.
'''
print("Step 3: Initialise agents.")
# Defining Variables
drunks = []
# Make the drunks.
for i in range(num_of_drunks):
    # Houses are identified in increments of 10 From 10 to 250.
    house = ((1 + i) * 10)
    drunks.append(Drunk(envir, drunks, house))

carry_on = True
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

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
    fig.clear()
    global carry_on

    for j in range(num_of_drunks):
        location = envir[drunks[j].y][drunks[j].x]

        if location != drunks[j].house and drunks[
            j].is_at_home == False:  # Assigning False to drunsk when location is not house
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
        plt.imshow(envir, cmap="Set3")
        plt.xlabel("Drunks stop moving when home")
        plt.title(label="This model show my like route home after a good time at the pub",
                  loc="center",
                  fontstyle='italic')

        # Plot drunks

        for a in range(num_of_drunks):
            plt.scatter(drunks[a].x, drunks[a].y)
            plt.show()


""" Run function runs simulation.  
    Quit function quits animation
    save density function writes density info to csv file
    ----------
    Parameters
    ----------
    Does not take any parameters.
    """


def run():
    print("Step 5: Run Animation.")

    animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=200)
    canvas.draw()

def quit():
    global root
    root.quit()
    save_density()
    print("Simulation ended")


def save_density():
    with open('environment.density.txt', 'w', newline='') as f:
        csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in envir:
            csvwriter.writerow(row)


'''Creates GUI'''

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root, )
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal")
model_menu.add_command(label="Clear model", command=quit, state="normal")

tkinter.mainloop()
