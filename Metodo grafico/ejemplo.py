

import cvxpy as cp;

# Creacion de dos variables de una sola dimension
x = cp.Variable(nonneg=True)
y = cp.Variable(nonneg=True)
h = cp.Variable(nonneg=True)

# Crear restricciones
constraints = [3*x+4*y-h<=4,x+3*y-4*h<=1]

#Funcion a minimizar
obj = cp.Maximize((3*x)+(6*y)-(4*h)) #El doble asterisco indica potencia

# Crear el problema y solucionar
prob = cp.Problem(obj, constraints)
prob.solve()  
print("status:", prob.status)
print("Valor maximo de la funcion", prob.value)
print("Valor optimo de las variables", x.value, y.value,h.value)