#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[-2,-1],[-1,1],[1,0]])
b = np.array([-3,0,0.5])
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(0, 60, 10000)
plt.plot(x1, (3 - (2*x1)), label='2x +y >= 3')
plt.plot(x1, x1, label='y<=x')
plt.plot(x1, 0.5+(x1*0), label='x <=5')


plt.fill_between(x1, 0, x1, where=(x1 >= 0) , alpha=0.1)
plt.fill_between(x1, 0, (3 - (2*x1)), where=((3 - (2*x1)) <= 3), alpha=0.1) 
plt.fill_between(x1, 0, 0.5+(x1*0), where=(0.5+(x1*0) <= 0.5 )  , alpha=0.1)

plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()


plt.show()

