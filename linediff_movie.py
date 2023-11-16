import numpy
import matplotlib
import sys 
import matplotlib.pyplot as plt
from matplotlib import animation


 #Lenght of the rod
L = 100
    
 #Thermal diffusion
alpha = 0.1

#Number 0f iterations
nt = 100

#Number of points on grid
nx = 101
    
#Distance between adjacent point
dx = L/(nx-1)
    
#Define the locations on the grid
x = numpy.linspace(0.0, L, num=nx)
    
#Intial condition
u0 = 40*numpy.random.rand(nx)
#numpy.ones(nx)
#15*numpy.ones(nx) 
#numpy.zeros(nx)
#10*numpy.random.rand(nx)
    
#Boundary values 
u0[0] = 100
u0 [-1]= 41.2
    
#setting the time
dt=0.5*dx**2/alpha**2

fig = plt.figure(figsize=(6.0,4.0))
axes = plt.axes(xlim=(0.0,L), ylim=(0.0, 100.0))
line, = plt.plot([], [], color = 'r', linestyle='-', linewidth=1)
plt.grid()
plt.xlabel('Distance')
plt.ylabel('Temperature')

def init():
    line.set_data(x, [])
    return line,

def animat(i):
     u[1:-1] = (u[1:-1] + sigma*(u[2:]- 2.0* u[1:-1]+ u[:-2]))
     line.set_data(x, u)
     return line,

# Run the FTCS scheme
u = u0.copy()
sigma = ((alpha**2)* dt/dx**2)
anim = animation.FuncAnimation(fig, animat, init_func=init, frames= nt, interval=1, blit=True)
plt.show()
