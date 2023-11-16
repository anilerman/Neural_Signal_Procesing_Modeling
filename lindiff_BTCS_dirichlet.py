import numpy
from scipy import sparse
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

M =50 # Number of points
N = 60 # Number of iterrations

x0 = 0 # Beginning of rod
xl =1 # End of rod

#Discrete your space
dx = (xl -x0)/(M-1)

#Discrete our time
t0 = 0
tf = 0.2

# Size of each time step
dt = (tf-t0)/(N-1)

aplha = 1.2 # Diffusion of Coefficient

r = dt*aplha/dx**2

xspan = numpy.linspace(x0, xl, M)
tspan = numpy.linspace(t0, tf, N)

#Setting the Vector
main_diagonal =(1+2*r)*numpy.ones((1,M-2))
off_diagonal = -r*numpy.ones((1,M-3))
a = main_diagonal.shape[1]
diagonals  =[main_diagonal, off_diagonal, off_diagonal]
A = sparse.diags(diagonals, [0,-1,1], shape=(a,a)).toarray() #creating the sparse matrix

# Use a 2D space-time matrix
u = numpy.zeros((M, N))

#Setting intial condition
u[:,0] = xspan-xspan**2

# Solve Dirchlet Boundary conditions
u[0, :] = 0.1 #100
u[-1,:] = 10.0

#Solver part, use N itterations. Start from 1 as we can 
for k in range(1, N):
    c = numpy.zeros((M-4,1)).ravel()
    b1 = numpy.asarray([r*u[0,k], r*u[-1,k]])
    b1 = numpy.insert(b1, 1, c)
    b2 = numpy.array(u[1:M-1, k-1])
    b =b1+b2
    u[1:M-1, k] = numpy.linalg.solve(A,b)

#Visualization part
x,t = numpy.meshgrid(tspan, xspan)
fig = plt.figure()
ax = fig.add_subplot(projection= '3d')
surf = ax.plot_surface(x ,t, u, linewidth=0, cmap=cm.coolwarm, antialiased =False)
ax.set_xticks([0, 0.05, 0.1, 0.15, 0.20])
ax.set_xlabel('Time')
ax.set_ylabel('Space')
ax.set_zlabel('u')
plt.tight_layout()
plt.show()


