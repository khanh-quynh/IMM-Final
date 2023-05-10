import math
import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['text.usetex'] = True
#plt.rcParams.update({'font.size': 8})

m = 1               # mass          (M)
l = 1               # length of rod (L)
g = 9.8             # gravity       (LT^2)
theta0 = 0.1        # intial angle  
t0 = 0              # intial time
tf = 10             # time span of stimulation
tau = np.sqrt(l/g)  # period of oscillation (timescale of the system)

dt_lst = [0.0005, 0.01, 0.05, 0.1]   # different time steps (delta_t)

for dt in dt_lst:
    
    tM = math.floor(tf/dt)
    
    t = np.linspace(t0, tf, tM)
    theta = np.zeros(tM)
    omega = np.zeros(tM)

    # initial conditions
    theta[0] = theta0
    omega[0] = 0

    # Euler
    for i in range(tM - 1):
        theta[i+1] = theta[i] + dt * omega[i]              # Euler for first ODE, solve for theta
        omega[i+1] = omega[i] - dt * (3*g/2*l) * np.sin(theta[i])  # Euler for second ODE, solve for angular velocity
        
    plt.plot(t/tau, theta, label='dt={}'.format(dt))

plt.xlabel(r"$\frac{t}{τ}$ (dimensionless time)")
plt.ylabel(r"$\theta$ radians" )
#plt.title(r"Euler Method: $\theta$ vs. Dimensionless Time Scale")
plt.legend()

#plt.savefig('rod-theta-dimensionless.pdf');
plt.show()
