""" The typical Lotka-Volterra Model simulated using scipy """

import scipy as sc
import scipy.integrate as integrate
import pylab as p #Contains matplotlib for plotting
import sys

# import matplotlip.pylab as p #Some people might need to do this

def dR_dt(pops, t=0):
    """ Returns the growth rate of predator and prey populations at any
    given time step """

    R = pops[0]
    C = pops[1]
    dRdt = r*R*(1-(R/k)) - a*R*C
    dydt = -z*C + e*a*R*C

    return sc.array([dRdt, dydt])

# Define parameters:
if len(sys.argv) < 6:
    print "Not enough command line arguments"
    #Add a quit script line

r = float(sys.argv[1]) # Resource growth rate
a = float(sys.argv[2]) # Consumer search rate (determines consumption rate)
z = float(sys.argv[3]) # Consumer mortality rate
e = float(sys.argv[4]) # Consumer production efficiency
k = float(sys.argv[5])

# Now define time -- integrate from 0 to 15, using 1000 points:
t = sc.linspace(0, 15,  1000)

x0 = 10
y0 = 5
z0 = sc.array([x0, y0]) # initials conditions: 10 prey and 5 predators per unit area

pops, infodict = integrate.odeint(dR_dt, z0, t, full_output=True)

infodict['message']     # >>> 'Integration successful.'

prey, predators = pops.T # What's this for?
f1 = p.figure() #Open empty figure object
p.plot(t, prey, 'g-', label='Resource density') # Plot
p.plot(t, predators  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population')
p.title('Consumer-Resource population dynamics')
p.text(1, 1, "r = " + sys.argv[1] + ", a = " + sys.argv[2] + " , z = " + sys.argv[3] +", e = " + sys.argv[4] + ", k = " + sys.argv[5])
p.show()
f1.savefig('../Results/prey_and_predators_2.pdf') #Save figure
