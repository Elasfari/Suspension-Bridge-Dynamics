import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the parameters of the model
m = 1000 # mass of the roadway (kg)
c = 100 # damping coefficient (N*s/m)
k = 10000 # spring constant (N/m)

# Define the initial conditions
x0 = 0 # initial displacement (m)
v0 = 0 # initial velocity (m/s)

# Define the time range
t_start = 0 # start time (s)
t_end = 10 # end time (s)
t_step = 0.01 # time step (s)

def model(x, t):
  # Extract the state variables from x
  x1 = x[0] # displacement
  x2 = x[1] # velocity

  # Evaluate the right-hand side of the differential equations
  x1dot = x2
  x2dot = (1/m)*(F(t) - c*x2 - k*x1)

  # Return the derivative of the state variables
  xdot = [x1dot, x2dot]
  return xdot

# Define the function that represents the external force
def F(t):
  # In this example, we will assume that the external force is a simple
  # sinusoidal function of time, with amplitude A and frequency omega
  A = 100 # amplitude (N)
  omega = 0.1 # frequency (1/s)
  return A*np.sin(omega*t)

# Solve the system of differential equations using the odeint function
t = np.linspace(t_start, t_end, int((t_end-t_start)/t_step))
x = odeint(model, [x0, v0], t)

# Plot the results
plt.plot(t, x[:,0])
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.show()
