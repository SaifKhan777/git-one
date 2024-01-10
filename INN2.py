import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1/(1+math.exp(-x))

def tanh(x):
    return 2/(1+math.exp(-2*x))-1

def relu(x):
    return max(0,x)

def lky_relu(x):
    return max(0.01*x,x)

def sILU(x):
    return x/(1+math.exp(-x))

def guss(x):
    return - (math.exp(-x*-x))

def softplus(x):
    return math.log(1+math.exp(x))


size=10

x_values = np.linspace(-7,7,100)
y_values=[sigmoid(x)for x in x_values]
plt.plot(x_values, y_values, label='Sigmoid Function')

x_values = np.linspace(-7,7,100)
y_values=[tanh(x)for x in x_values]
plt.plot(x_values, y_values, label='Sigmoid Function')

x_values = np.linspace(-7,7,100)
y_values=[relu(x)for x in x_values]
plt.plot(x_values, y_values, label='Sigmoid Function')
