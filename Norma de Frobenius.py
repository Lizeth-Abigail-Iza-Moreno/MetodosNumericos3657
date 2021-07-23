import numpy as np #importamos la matriz numpy
from math import sqrt
A=np.array([[6,1,-1,5], # definimos la matriz
            [1,8,4,4],
            [8,-2,4,-1],
            [1,6,4,3]])
print("\n\t*****Programa de la Norma de Frobenius*****")
print("----------------------------------------------------")
print("La matriz ingresada es:\n",A)
filas=A.shape[0] #Numero de filas
columnas=A.shape[1]#Numero de columnas
sumar=0
#Norma de Frobenius
for i in range(filas):
    for j in range(columnas):
        sumar+=pow(A[i][j],2)
    Res=sqrt(sumar) #Resultado
print("----------------------------------------------------")
print("El resultado de la norma de Frobenius es:",Res)
