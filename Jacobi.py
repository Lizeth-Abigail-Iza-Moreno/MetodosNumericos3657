import numpy as np #Importamos la libreria numpy
A=np.array([[7,1,-1,2], #Definimos la  matriz
            [1,8,0,-2],
            [-1,0,4,-1],
            [2,-2,-1,6]])
b=np.array([3,-5,4,-3])
print("*****Programa Metodo Jacobi*****")
print("La matriz ingresada es:")
print(A)
print("\n",b)
k=15 #Numero de iteraciones
n=A.shape[1] #numero de columnas
D=np.eye(n) #Matriz identidad
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)]
LU=D-A
L=np.tril(LU) #Matriz tridiagonal inferior
U=np.triu(LU)#Matriz tridiagonal  superior
X=np.zeros(n) #Almacenar las respuestas
error=[]
print("\t\t\tSoluciones del método jacobi")
print("Iteración",0,"es:",X)
#Metodo Jacobi
for i in range(k):
    D_inv=np.linalg.inv(D)
    X=np.dot(np.dot(D_inv,L+U),X)+np.dot(D_inv,b)
    print("Iteración",i+1, "es:",X.round(decimals=4))

