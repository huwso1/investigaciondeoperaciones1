#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[2,3]])
b = np.array([60])
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(0, 60, 10000)
plt.plot(x1, (60 - (2*x1))/3, label='2x + 3y <= 60')


plt.fill_between(x1, 0, (60 - (2*x1))/3, where=((60 - (2*x1))/3 <= 60) & (x1 >= 0), alpha=0.1) 


plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

#Encontrar el vértice óptimo

plt.show()

