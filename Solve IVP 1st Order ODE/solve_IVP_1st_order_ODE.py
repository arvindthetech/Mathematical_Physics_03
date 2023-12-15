#To Solve an Value Problem (IVP) for Order Ordinary Differential Equation.

#   Lets_take_example_1st_order_ODE_Radioactive_decay
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Function defining the ODE dN/dt = -kN
def radioactive_decay(N,t,k):
    return -k*N

N0 = 1000
k = 0.01
t = np.linspace(0,1000,10)

#Solvi the ODE
solution = odeint(radioactive_decay,N0,t,args=(k,))

#Plot the solution 
plt.plot(t,solution,label="Radioactive Substance")
plt.xlabel("Time")
plt.ylabel("Quantity")
plt.title("Radioactive Decay(IVP)")
plt.legend()
plt.show()
