import numpy as np #Importamos la libreria numpy
A=np.array([[7,1,-1,2], #Definimos la  matriz
            [1,8,0,-2],
            [-1,0,4,-1],
            [2,-2,-1,6]])
b=np.array([3,-5,4,-3])
print("*****Programa Método Gauss Seidel*****")
print("-----------------------------------------------")
print("La matriz ingresada es:")
print(A)
print("\n",b)
k=8 #Numero de iteraciones
n=A.shape[1] #numero de columnas
D=np.eye(n) #Matriz identidad
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)] #Matriz diagonal
LU=D-A
L=np.tril(LU)  #Matriz tridiagonal inferior
U=np.triu(LU) #Matriz tridiagonal  superior
DL=D-L
X=np.zeros(n) #almacenar las respuestas
print("\t\t\tSoluciones del Gauss Seidel")
print("-----------------------------------------------")
print("Iteración",0,"es:",X)
# Método Gauss Seidel
for i in range(k):
    DL_inv=np.linalg.inv(DL)
    X=np.dot(np.dot(DL_inv,U),X)+np.dot(DL_inv,b)
    print("Iteración",i+1, "es:",X.round(decimals=4))

