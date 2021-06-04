#Grafique de ambas funciones en el mismo gráfico
#Importamos las librerias matplolib y numpy y las renombra para invocarla como np y plt
import matplotlib.pyplot as plt
import numpy as np
#definimos las funcion cuadratica y racional
def f(x):
    return x**2-x+1
def g(x):
    return 2/(x-1)
#coordenadas del eje x
x=np.linspace(-30,30,1000)
fig=plt.figure(figsize=(8,4))
#Graficamos y colocamos el color a cada una de las funciones
plt.plot(x,f(x),'r--',label='f(x)=$x^2-x+1$')
plt.plot(x,g(x),'b',label='$g(x)=2/x-1$')
#Damos nombres al eje 'X' y 'Y'
plt.xlabel('x')
plt.ylabel('y')
#Limita los valores de los ejes
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.grid(True) #coloca cuadriculas
plt.title('Gráfica de funciones') #titulo de la gráfica
plt.legend(loc = 1)
plt.show() #Mostramos las graficas
