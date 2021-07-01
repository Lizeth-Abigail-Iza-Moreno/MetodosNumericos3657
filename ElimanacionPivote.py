#importamos la libreria  numpy
import numpy as np
#Definimos la matriz
A = np.array([[4., -1., -1.,  0.],
              [-1., 4.,  0., -1.],
              [-1., 0.,  4., -1.],
              [0., -1., -1., 4.]])
B = np.array([30.,60.,40.,70.])
A1=np.copy(A)
B1=np.copy(B)
n=len(B)
print("\t*****Programa Método de Eliminación gaussiana con pivote parcial*****")
print("-------------------------------------------------------------------")
print("\nLa matriz Ingresada es: \n", A)
print("\n",B)
#Método con pivoteo parcial
for k in range(n-1):
        #Se Elije el elemento de pivote más grande a continuación (incluido) k
        maxindex = abs(A[k:,k]).argmax()+ k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        #Intercambiar filas
        if maxindex != k:
            A[[k,maxindex]] = A[[maxindex, k]]
            B[[k,maxindex]] = B[[maxindex, k]]
for k in range(0,n-1):
#Método de eliminación gaussiana
    for i in range(k+1,n):
        mult= A[i,k]/A[k,k]
        for j in range(k,n):
            A[i,j]-=mult*A[k,j]
        B[i] -=mult*B[k]
x=np.zeros(n)
x[n-1]=B[n-1]/A[n-1,n-1]
#Sustitución regresiva
for i in range(n-2,-1,-1):
    sumaj=0
    for j in range(i+1,n):
        sumaj += A[i,j]*x[j]
        x[i]=(B[i]-sumaj)/A[i,i]
#Imprimimos las soluciones del sistema de ecuaciones
print("--------------------------------------------------------------------------------------")
print("\nLas soluciones del sistema de  ecuaciones (T1,T2,T3,T4) es:")
print(np.linalg.solve(A , B))