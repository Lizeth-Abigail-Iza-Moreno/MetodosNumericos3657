import numpy as np #Importamos la matriz numpy
MAT_B=np.array([[4 , 6 , 10],  #Definimos la matriz B
                [6 , 3 , 19],
                [10 , 19 , 62]])
def cholesky(MAT_B): #Método de descomposición de  cholesky
    MAT_B = np.array(MAT_B,float)
    L = np.zeros_like(MAT_B)
    n,_= np.shape(MAT_B)
    for j in range(n):
        for i in range(j, n):
            if i == j:
                L[i, j] = np.sqrt(MAT_B[i, j] - np.sum(L[i, :j] ** 2))
            else:
                L[i, j] = (MAT_B[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L
l=cholesky(MAT_B)
Tl=np.transpose(l) #Matriz Transpuesta
print("\t******Programa Descomposición de Cholesky******")
print("La Matriz B:")
print(MAT_B)
print("\nLa Matriz L es :")
print(l)
print("\nLa Matriz Transpuesta de L :")
print(Tl)