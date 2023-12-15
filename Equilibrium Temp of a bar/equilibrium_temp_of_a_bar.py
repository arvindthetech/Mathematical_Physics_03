#The equilibrium temperature of a bar of length L with insulated horizontal sides and the ends maintained at fixed temperatures.


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Given Parameter 
L = 10   #length of the rod in meter
T1 = 40  #Temp at one end in degree celsius
T2 = 200 #Temp at other end in degree celsius
Ta = 20  #Surrounding air temp in degree calsius
h = 0.01  #Heat transfer Coefficient in m^-2

#Converting temp in Kelvin
T1_K = T1 + 273.15
T2_K = T2 + 273.15
Ta_K = Ta + 273.15

#Function for the differential equation
def diff_eq(T,x):
    return [T[1],h*(Ta_K - T[0])]

#Function to solve the differential equ using the shooting method
def solve_shooting_method(T_guess):
    x = np.linspace(0,L,100) 
    T_initial = [T_guess, 0]
    T_solution = odeint(diff_eq, T_initial, x)
    return T_solution[:,0]

#Perform a binary search to finnd the correct intial gues
def find_initial_guess():
    lower_bound = T1_K
    upper_bound =T2_K

    while abs(upper_bound - lower_bound) > 1e-5:
        guess = (lower_bound + upper_bound)/2
        T_end = solve_shooting_method(guess)[-1]

        if T_end > T2_K:
            upper_bound = guess
        else:
            lower_bound = guess
    return guess

#Solve the problem
initial_guess = find_initial_guess()
temperature_profile = solve_shooting_method(initial_guess)

#Plot the temp distribution
x = np.linspace(0,L,100)
plt.plot(x, temperature_profile - 273.15, label="Temperature distribution")
plt.axhline(y=Ta, color="r",linestyle="--", label="Surrounding air temperature")
plt.xlabel("Distance along the rod (m)")
plt.title("Temperature (℃)")
plt.legend()
plt.grid()
plt.show()
