import math
import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['text.usetex'] = True
#plt.rcParams.update({'font.size': 8})

m = 1                                # mass          (M)
l = 1                                # length of rod (L)
g = 9.8                              # gravity       (LT^2)
theta0 = 0.1                         # intial angle  
t0 = 0                               # intial time
omega0 = 0                           # initial angular velocity
tf = 10                              # time span of stimulation
tau = np.sqrt(l/g)                   # period of oscillation (timescale of the system)
dt = 0.0001                          # set any value as long as it is much smaller than tau
tM = math.floor(tf/dt)               
#k = 0.1                              # low drag coefficient 
k = 0.7                              # high drag coefficient


theta0_ls = [round(np.pi/100,3),round(np.pi/36,3),round(np.pi/18,3)]    # different initial angles


for theta0 in theta0_ls:
    t_ls = np.linspace(t0, tM * dt, tM + 1)
    
    theta_ls = np.zeros(tM+1)
    omega_ls = np.zeros(tM+1)
    
    # initial conditions
    theta_ls[0] = theta0
    omega_ls[0] = 0
    
    # Euler
    for i in range(tM):
        theta_ls[i+1] = theta_ls[i] + dt * omega_ls[i]                             # Euler for the first ODE, solve for theta
        omega_ls[i+1] = omega_ls[i] - dt * ((6*g/l) * np.sin(theta_ls[i])  + 3*k/m*omega_ls[i]   )  # Euler for the second ODE, solve for angular velocity
        
    plt.plot(t_ls/tau, theta_ls, label = r"$\theta_0=$" + str(theta0))
    
plt.xlabel("t (time)")
plt.ylabel(r"$\theta$ radians" )
#plt.title(r"Euler Method: $\theta$ vs Time for Different Initial Angles")

plt.legend(loc = 'upper right')

plt.savefig('rod_high_drag.pdf')
plt.show()



