#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[2,-4]])
b = np.array([-4])
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(-20, 60, 10000)
plt.plot(x1, (x1+2)/2, label='2x + -4y <= -4')


plt.fill_between(x1, 0, (x1+2)/2, where=((x1+2)/2 >= 0), alpha=0.1) 


plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()


plt.show()

