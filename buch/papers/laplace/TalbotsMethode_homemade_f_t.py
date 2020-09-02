# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 08:34:15 2020

@author: Severin Weiss
"""
import math
import numpy as np
import sympy as sym
from sympy import *
from sympy.integrals import laplace_transform
import matplotlib.pyplot as plt

t = symbols('t')
s = symbols('s')



class Talbot:
    def __init__(self, lamda, sigma, mu, n):
        self.lamda = lamda
        self.sigma = sigma
        self.mu = mu
        self.n = n
        
        
    def fTilde(self, Tn, Tn0):
        """ Calculates fTilde
        The first element fTilde[0] is calculated separatly by using Tn0.
        """
        
        sizeofTn = len(Tn)
        
        fTilde = [complex(0) for x in range(0,sizeofTn)]
        
        fTilde[0] = self.lamda*np.e**(t*self.sigma)/self.n*Tn0
        
        for r in range(1,sizeofTn):
            fTilde[r] = self.lamda*np.e**(t*self.sigma)/self.n*Tn[r]
        
        return fTilde
    
    def Calculate_Tn_Parameters(self):
        
        """ Calculates the Tn Summation.
        Tn will be a vector with n elements """
        
        # Initialize s_mu, F_tilde. s_mu_prime, Tn with zeros
        
        s_mu = s_mu_prime = [complex(0) for x in range(0,self.n)]
        theta_j = [complex(0) for x in range(0,self.n)]
        
        for k in range(0,self.n):
            
            # Calculate theta_j
            theta_j[k] = k*np.pi/self.n
            
            # Calculate s_mu
            s_mu[k] = theta_j[k]*(1/np.tan(theta_j[k])) + 1j*self.mu*theta_j[k]

            
            # Calculate s_mu_prime
            s_mu_prime[k] = 1j*(self.mu + (theta_j[k] - np.cos(theta_j[k]*np.sin(theta_j[k])))/np.square(np.sin(theta_j[k])))
            

        return theta_j, s_mu, s_mu_prime
    
    def Calculate_Tn(self,F):
        
        theta_j, s_mu, s_mu_prime = self.Calculate_Tn_Parameters()
        
        Tn0 = 0.5*self.mu*np.e**(t*self.lamda)*F[0]
        Tn = [complex(0) for x in range(0,self.n-1)]
        
        for j in range(1,len(F)-1):
            Tn[j] = np.e**(t*self.lamda*s_mu[j])*F[j]*1/1j*s_mu_prime[j]
        
        return Tn, Tn0
    

#--- Definition of Functions 

def evaluate_fTilde_at_t_zero(fTilde,t_zero):
    
    evaluated_fTilde = [complex(0) for x in range(0,len(fTilde))]
    
    for i in range(0,len(fTilde)):
        
        evaluated_fTilde[i] = fTilde[i].evalf(subs={t:t_zero})
    
    
    return evaluated_fTilde


def calculate_absolute_error_at_tzero(fExact, fTilde, t_zero):
    
    evaluated_fTilde = evaluate_fTilde_at_t_zero(fTilde,t_zero)
    
    magnitude_evaluated_fTilde = 0
    
    for i in range(0,len(evaluated_fTilde)):
        
        magnitude_evaluated_fTilde = abs(evaluated_fTilde[i]) + magnitude_evaluated_fTilde
   Severin Weiss
    absolute_error_at_tzero = abs(fExact.evalf(subs={t:t_zero}) - magnitude_evaluated_fTilde)
    
    return absolute_error_at_tzero



def calculate_absolute_error_over_time(fExact, fTilde, t_intervall):
    
    # t_intervall contains all time_steps to evaluate
    
    absolute_error_over_time = [float(0) for i in range(0,len(t_intervall))]
    
    for j in range(0,len(t_intervall)):
        
        evaluated_fTilde = evaluate_fTilde_at_t_zero(fTilde,t_intervall[j])
        
        magnitude_evaluated_fTilde = 0
        
        for i in range(0,len(evaluated_fTilde)):
            
            magnitude_evaluated_fTilde = abs(evaluated_fTilde[i]) + magnitude_evaluated_fTilde
            
            absolute_error_over_time[j] = abs(fExact.evalf(subs={t:t_intervall[j]}) - magnitude_evaluated_fTilde)
    
    return absolute_error_over_time


def plot_absolute_error_over_time(fExact, fTilde, time_intervall, nsteps):
    
    # time_intervall must be a list with starting time t_a and ending time t_b --> [t_a, t_b]
    
    intervall = time_intervall[1] - time_intervall[0]
    
    timestep = intervall/nsteps
    
    timevector = [float(0) for i in range(0,nsteps)]
    
    time = time_intervall[0]
    
    for i in range(0,nsteps):
        
        time = time + timestep
        
        timevector[i] = time + timestep 
    
    absolute_error_over_time = calculate_absolute_error_over_time(f_of_t_exact, fTilde, timevector)
    
    xvals = np.arange(time_intervall[0], time_intervall[1], timestep)
    yvals = absolute_error_over_time 
    
    plt.figure()
    plt.plot(xvals, yvals,label='error')
    plt.title("Error of the numerical Laplace Inversion 'F(s) = 2/(s**3)'")
    plt.xlabel("time t")
    plt.ylabel("error e")
    plt.show


def plot_absolute_error_at_certain_points(fExact, fTilde, timevector):
    
    # time_vector must be a list with all points in time to evaluate

    absolute_error_at_certain_points = calculate_absolute_error_over_time(f_of_t_exact, fTilde, timevector)
    
    xvals = timevector
    yvals = absolute_error_at_certain_points
    
    plt.figure()
    plt.plot(xvals, yvals, label='error')
    plt.title("Error of the numerical Laplace Inversion 'F(s) = 2/(s**3)'")
    plt.xlabel("time t")
    plt.ylabel("error e")
    plt.show
    plt.legend()
    
    
def table_absolute_error_at_certain_points(fExact, fTilde, timevector):
    
    # time_vector must be a list with all points in time to evaluate

    absolute_error_at_certain_points = calculate_absolute_error_over_time(f_of_t_exact, fTilde, timevector)
    
    data = [[] for x in range(0,len(timevector))]
    
    fig, axs = plt.subplots(2,1)
    
    if len(timevector) == len(absolute_error_at_certain_points):
        for i in range(0,len(timevector)):
            data[i] = [timevector[i], absolute_error_at_certain_points[i]]
            
    print(data)
    
    clust_data = data
    collabel = ("time", "Error")
    axs[0].axis('tight')
    axs[0].axis('off')
    the_table = axs[0].table(cellText = clust_data, colLabels=collabel, loc='center')

    plt.show()
    
    
def laplace_transform_comparison(fTilde, F_of_s):
    
    frequency_vector = [0.1, 1, 10, 100]
    laplace_transform_fTilde = [float(0) for x in range(0,len(fTilde))]
    
    for i in range(0,len(fTilde)):
        
        laplace_transform_fTilde[i] = laplace_transform(fTilde[i], t, s)

    
    print(laplace_transform_fTilde[0])
    print(laplace_transform_fTilde[0].evalf(subs={s:1}))
    
#    difference = [float(0) for x in range(0,len(frequency_vector))]
#    
#    for i in range(0,len(difference)):
#    
#        difference[i] = F_of_s.evalf(subs={s:frequency_vector[i]})- summe_laplace_transform_fTilde.evalf(subs={s:frequency_vector[i]})
#        
#    
#    print("This is the difference of F(s) and Laplace(fTilde) evaluated at certain points", difference, len(difference))
#    
#        
#    return None


#--- Defining Constants 

# Define lamda
LAMDA = 0.101
# Define sigma
SIGMA = 0.965
# Define mu
MU = 0.098953

# Define n
N = 100
# Time to evaluate
T_ZERO = 1


#--- Defining mathematical Functions for the Inversion and Evaluation

f_of_t_exact = t**2

F_of_s_exact = 2/(s**3)

# Initializing an Object (Talbot1) of the Class Talbot        
Talbot1 = Talbot(LAMDA,SIGMA,MU,N)
theta_j, s_mu, s_mu_prime = Talbot1.Calculate_Tn_Parameters()

# Now the Function F(s) has to be modified by setting s = sigma + lamda*s_mu
# Example for F(s) = 1/(s+1)


F = [complex(0) for x in range(0,len(theta_j))]

for i in range(1,len(s_mu)): # "-1" because of the first element in Tn
    substition_of_s = Talbot1.sigma + Talbot1.lamda*s_mu[i]
    F[0] = F_of_s_exact.evalf(subs={s:(SIGMA+LAMDA)})
    F[i] = F_of_s_exact.evalf(subs={s:substition_of_s})


# Calculate numeric Approximation of the Laplace Inversion
Tn, Tn0 = Talbot1.Calculate_Tn(F)
fTilde = Talbot1.fTilde(Tn,Tn0)


# Calculate the absolute Error evaluated at 
# certain t
# Plot of the error dependent on t ?

#error=calculate_absolute_error_at_tzero(f_of_t_exact, fTilde, 0)
#print(error)

#time_vector = [0, 0.1, 0.2, 0.3, 0.5, 0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,2,3]
#
#plot_absolute_error_at_certain_points(f_of_t_exact, fTilde, time_vector)

time_intervall = [0,1]

plot_absolute_error_over_time(f_of_t_exact, fTilde, time_intervall, 100)

#laplace_transform_comparison(fTilde, F_of_s_exact)




# show dependency of Paramters and poles of F(s)


