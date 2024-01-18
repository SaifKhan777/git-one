import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x=sp.symbols('x')
f=x**2
x_val=2
derivative =sp.diff(f,x)
slope=derivative.subs(x,x_val)
tangent_eq=slope*(x-x_val)+f.subs(x,x_val)

f_lambda=sp.lambdify(x,f,'numpy') #creates a NumPy-compatible function
tangent_lambda=sp.lambdify(x,tangent_eq,'numpy')
derivative_lambda=sp.lambdify(x,derivative,'numpy')

x_values=np.linspace(-5,5,100)
y_curve=f_lambda(x_values)
y_tangent=tangent_lambda(x_values)
y_derivative=derivative_lambda(x_values)
plt.figure(figsize=(10,6))

plt.plot(x_values,y_curve,label='Curve')
plt.plot(x_values,y_tangent,label="tangent")
plt.plot(x_values,y_derivative,label='Derivative')
plt.scatter([x_val], [f_lambda(x_val)], color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve, Tangent, and Derivative Plot')
plt.grid(True)
plt.show()
