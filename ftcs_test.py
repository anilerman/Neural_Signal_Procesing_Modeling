import numpy as np
from matplotlib import pyplot
import functionlar as func


if __name__ == '__main__':

    # length of rod
    L = 1000

    # thermal diffusivity 
    alpha = 0.5

    # number if iterations 
    nt= 90000

    # number of points of your grid
    nx = 501

    # distance between adjacent point
    dx = L/(nx-1)

    # define the ;ocations on the grid
    x = np.linspace(0.0, L, num=nx)

    # initial condition
    u0 = np.zeros(nx)

    # boundary values
    u0[0] = 100
    u0[-1] = 0

    # setting the time  step size according to the stability condition
    dt= 0.5 * dx**2/alpha**2

    #run the FTCS scheme
    u = func.FTCS(u0, nt, dt, dx, alpha)

    # plot the temperature along the rod
    pyplot.figure(figsize=(6.0,4.0))
    pyplot.xlabel('Distance')
    pyplot.ylabel('Temperature')
    pyplot.grid()
    pyplot.xlim(0.0, L)
    pyplot.ylim(0.0, 100.0)
    pyplot.plot(x, u, color='C0', linestyle='-', linewidth=2) 
    pyplot.show()