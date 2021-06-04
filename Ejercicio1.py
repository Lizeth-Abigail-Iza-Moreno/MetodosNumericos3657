#calcular la inversa de matrices de dimensión 2 × 2.
import numpy as np  #Importamos "numpy"
print('\t********* INVERSA DE UNA MATRIZ DE 2x2 ********')
print('---------------------------------------------')
#Ingresar los valores de la matriz de 2x2
A=float(input('Ingresar el valor de a:'))
B=float(input('Ingresar el valor de b:'))
C=float(input('Ingresar el valor de c:'))
D=float(input('Ingresar el valor de d:'))
print('\nLa Matriz ingresada de 2x2 es:\n',np.array([[A,B],[C,D]]))
#calculamos el determinante de la matriz de 2x2
det=A*D-B*C
#si la determinante es 0 entonces no hay inversa
if(det==0):
    print('No existe inversa de la matriz')
else:
    # Calculamos los cofactores
    A1 = (1/det)*D
    B1 = (1/det)*(-B)
    C1 = (1/det)*(-C)
    D1 = (1/det)*A
    # Sacamos por pantalla la matriz inversa
    print('\nLa matriz inversa es:\n',np.array([[A1,B1],[C1,D1]]))
