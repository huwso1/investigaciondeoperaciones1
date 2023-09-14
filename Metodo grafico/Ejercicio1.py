#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[2,1]])
b = np.array([5])
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(0, 60, 10000)
plt.plot(x1, (5 - 2*(x1)), label='2x1 + x2 <= 5')


plt.fill_between(x1, 0, (5 - (2*x1)), where=((5 - (2*x1)) <= 5) , alpha=0.1) 


plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('Y')
plt.ylabel('X')
plt.legend()




plt.show()
