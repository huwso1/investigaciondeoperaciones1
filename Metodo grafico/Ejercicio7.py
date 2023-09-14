#Código Python usado en el video:

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#Definir restricciones
A = np.array([[-500,-100],[-1000,-2500]])
b = np.array([-6000,-10000])
x1_bounds = (0, None)
x2_bounds = (0, None)

#Graficar restricciones
x1 = np.linspace(0, 100, 10000)
plt.plot(x1, (6000 - (500*x1))/100, label='500x + 100y >= 6000')
plt.plot(x1, (10000 - (1000*x1))/2500, label='1000x + 2500y >= 10000')


plt.fill_between(x1, 0, (6000 - (500*x1))/100, where=((6000 - (500*x1))/100<= 6000) & (x1 >= 0), alpha=0.1) 
plt.fill_between(x1, 0, (10000 - (1000*x1))/2500, where=((10000 - (1000*x1))/2500 <= 10000) & (x1 <= 0), alpha=0.1)

plt.xlim(x1_bounds)
plt.ylim(x2_bounds)
plt.xlabel('Asesinos')
plt.ylabel('Tanques')
plt.legend()

#Encontrar el vértice óptimo
c = np.array([40, 70]) #funcion objetivo
res = linprog(c, A_ub=A, b_ub=b, bounds=(x1_bounds, x2_bounds), method='simplex')

#Agregar el punto de la solución óptima al gráfico
vertice_optimo = (res.x[0], res.x[1])
plt.plot(vertice_optimo[0], vertice_optimo[1], 'ro', markersize=10)
A=""
A=A+' Optimal x = '+res.x[0].astype('str')+' Optimal y = '+res.x[1].astype('str')+""+' Valor optimo '+(res.fun).astype('str');
plt.xlabel(A)
print(' x = ' ,res.x[0] ,'y = ',res.x[1], 'con un valor de ', -res.fun)
plt.show()