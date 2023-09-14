#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[1,0]])
b = np.array([[5]])
x1_bounds = (-10, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(-10, 70, 10000)
plt.plot(x1, 5+(x1*0), label='Y <= 5')


plt.fill_between(x1, 0, 5, where= (5+(x1*0)<=5) , alpha=0.1) 


plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()





plt.show()

