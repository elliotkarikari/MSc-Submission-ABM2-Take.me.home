# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:01:10 2022

@author: Elliot
"""

# Imports Libraries
import matplotlib
matplotlib.use('TkAgg') #TkAgg renders data to a tk Canvas
import matplotlib.pyplot as plt
import tkinter
import random
import matplotlib.animation as anim
import Framework 
from Environment import Environment



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

#Reads in environment
env = Environment()
envir = env.readEnvironment()
print (envir)


'''
Step 3: Initialise agents.
'''
print("Step 3: Initialise agents.")
# Defining Variables
drunks= []    
# Make the drunks.
for i in range(num_of_drunks):
   drunks.append(Framework.Drunk(envir,drunks))

carry_on = True
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



    
def update(frame_number):

    """Once canvas is drawn. It updates the canvas per frame_number. 
    
    If the arguement frame_number isn't passed frame is not updated.
    
    Parameters
    ----------
    frame_number : int,
        Number of times frames after which canvas is cleared and redrawn 
    ------
    """
    # Clear fig
    fig.clear() 
    global carry_on

#Agentframework Tasks                                       
#    random.shuffle(drunks)    # Agent order is randomized 
    
#Loops through list of agents and calls agent methods defined in agentframework. This gives agency to created agents   
    for i in range (num_of_drunks):
        #print (agents[i].i)
        #Process the agents in a randomish order.
        drunks[i].move()
    if random.random() < 0.1:
        carry_on = False
        #print("stopping condition")
    else:
        carry_on = True
        #print("Continuing")
        

    # Plot            
    # Plot environment
    plt.ylim(0,300) 
    plt.xlim(0,300)
    plt.imshow(envir, cmap="binary")
    plt.xlabel('My Home is the outter box, The pub is the inner box')
    plt.title(label="This model show the likely route home after a good time at the pub",
                  loc="center",
                  fontstyle='italic')
    
    #Plot drunks
    for i in range (num_of_drunks):
               plt.scatter(drunks[i].x, drunks[i].y) # y and x points (Sheep) plots on map, colour white
               #print(agents[i].getx(),agents[i].gety())

plt.show()


"""This runs simulation.  
    
    Parameters
    ----------
    Does not take any parameters.
    ------
    Step 4: Animate agents.
    """
def run(): 
    print("Step 4: Animate agents.")
    
    animation = anim.FuncAnimation(fig, update, interval=1, repeat=False, frames=50)
    canvas.draw()
    """Create animated plot. Continues to update the plot until stopping criteria is met.""" 
    



def quit():
    
    """This stops the simulation.
    
    Parameters
    ----------
   Does not take any parameters. 
    ------
    """
    global root
    root.quit()

'''Creates GUI'''

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root,)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
                      
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 
model_menu.add_command(label="Clear model", command=quit, state="normal")


tkinter.mainloop()