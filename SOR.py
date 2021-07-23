import numpy as np #Importamos la libreria numpy
A=np.array([[7,1,-1,2], #Definimos la  matriz
            [1,8,0,-2],
            [-1,0,4,-1],
            [2,-2,-1,6]])
b=np.array([3,-5,4,-3])
print("*****Programa Método SOR*****")
print("-----------------------------------------------")
print("La matriz ingresada es:")
print(A)
print("\n",b)
k=5 #Numero de iteraciones
w=1.1
n=A.shape[1] #numero de columnas
D=np.eye(n) #Matriz identidad
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)] #Matriz diagonal
LU=D-A
L=np.tril(LU)  #Matriz tridiagonal inferior
U=np.triu(LU) #Matriz tridiagonal  superior
D_wL=D-w*L
X=np.zeros(n) #almacenar las respuestas
print("\t\t\tSoluciones del SOR")
print("-----------------------------------------------")
print("Iteración",0,"es:",X)
# Método SOR
for i in range(k):
    D_wL_inv=np.linalg.inv(D_wL)
    X=np.dot(np.dot(D_wL_inv,(1-w)*D+w*U),X)+w*np.dot(D_wL_inv,b)
    print("Iteración", i + 1, "es:", X.round(decimals=4))