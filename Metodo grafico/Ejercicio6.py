#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[2,1],[1,2],[1,1]])
b = np.array([180,160,100])
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(0, 200, 10000)
plt.plot(x1, (180 - (2*x1)), label='2x + 3y <= 180')
plt.plot(x1, (160 - x1)/2, label='x + 2y <= 160')
plt.plot(x1, (100 - x1), label='x + y <= 100')

plt.fill_between(x1, 0, (180 - (2*x1)), where=((180 - (2*x1)) <= 180) & (x1 >= 0), alpha=0.1) 
plt.fill_between(x1, 0, (160 - x1)/2, where=((160 - x1)/2 <= 160) & (x1 >= 0), alpha=0.1)
plt.fill_between(x1, 0, (100 - x1), where=((100 - x1) <= 0) & (x1 >= 0), alpha=0.1)

plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

#Encontrar el vértice óptimo
c = np.array([-4, -6]) #funcion objetivo
res = linprog(c, A_ub=A, b_ub=b, bounds=(x1_bounds, x2_bounds), method='simplex')

#Agregar el punto de la solución óptima al gráfico
vertice_optimo = (res.x[0], res.x[1])
plt.plot(vertice_optimo[0], vertice_optimo[1], 'ro', markersize=10)
A=""
A=A+' Optimal x = '+res.x[0].astype('str')+' Optimal y = '+res.x[0].astype('str')+""+' Valor optimo '+(-res.fun).astype('str');
plt.xlabel(A)
print(' x = ' ,res.x[0] ,'y = ',res.x[1], 'con un valor de ', -res.fun)
plt.show()

