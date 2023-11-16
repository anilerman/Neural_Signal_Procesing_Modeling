def FTCS(u0, nt, dt, dx, alpha):
    u = u0.copy()
    sigma = (alpha**2)*dt/dx**2
    for n in range(nt):
        u[1:-1] = (u[1:-1] + sigma * (u[2:] - 2.0 * u[1:-1] + u[:-2]))
    return u

def init(line):
    line.set_data(x, [])
    return line,

def animat(i):
     u[1:-1] = (u[1:-1] + sigma*(u[2:]- 2.0* u[1:-1]+ u[:-2]))
     line.set_data(x, u)
     return line,