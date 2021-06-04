# Código para calcular el sen(pi/3) con la serie de taylor, truncar cuando n=50
#Importamos la libreria numpy y renombramos para invocarla como pn
import numpy as pn
x = pn.pi/3
n = 51 #truncamos  para  que nos salga los  primeros 50 valores
sen_x = 0  #inicializamos el acumulador en cero
print("\n\t*****CACULAMOS EL SEN(pi/3)****")
print("\nn    pn(x)")
#ciclo para acumular /sumar los terminos
for k in range(n):
    sen_x=sen_x+(-1)**k*x**(2*k+1)/pn.math.factorial(2*k+1)
    print(k,sen_x)
