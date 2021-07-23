import numpy as np #Importamos la libreria numpy
#Definimos la matriz del sistema de ecuaciones
A=np.array([[6,0,0,0],[3,6,0,0],[4,-2,7,0],[5,-3,9,21]])
#Escribimps los terminos indepnedientes
b=np.array([12,-12,14,-2])
#Numero de ecuaciones
n=np.size(b)
#Vector para almacenar la solucion
x=np.zeros(n)
#Metodo de la Sustitucion Progresiva
for i in range(n):
    suma=0
    for j in range(i):
        suma+=A[i,j]*x[j]
    x[i]=(b[i]-suma)*1/A[i,i]
print("******Programa de Sustitución Progresiva*****\n")
print("La matriz Ingresada es:")
print(A)
print("\n",b)
print("-------------------------------------------------------------------")
print("Las soluciones del sistema de ecuaciones (x1,x2,x3,x4) es:")
print(x)