
import math
import numpy as np
import matplotlib.pyplot as plt

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
k = 3                                # drag coefficient

# phase placeholder and grid
theta = np.linspace(-np.pi, np.pi, 1000)
theta_dot = np.linspace(-10, 10, 1000)
theta, omega = np.meshgrid(theta, theta_dot)

# phase plan
theta_dot = omega
#omega_dot = -(k/m)*omega - (g/l)*np.sin(theta)        #damped
omega_dot = - (g/l)*np.sin(theta)                    #undamped

# phase portrait
plt.streamplot(theta, omega, theta_dot, omega_dot, density=1.5, linewidth=1, arrowsize=1)



plt.xlabel('$\\theta$')
plt.ylabel('$\\theta\'$')
#plt.title('Phase Portrait for Damped Pendulum')
plt.savefig('phase-undamped.pdf')
plt.show()

