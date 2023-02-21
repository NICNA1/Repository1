# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:53:03 2023

@author: itziar
"""

import numpy as np
import Gausslucia as luci
#1. Factorización A=LU
print("Descomposición de matrices cuadradas: ")
m= int(input("Introduce el número de filas de la matriz: "))
A= np.zeros([m,m])
u= np.zeros([m,m])
l= np.zeros([m,m])
b= []
print("Introduce los elementos de la matriz")
#f para filas, c para columnas. Se hace esto para que pregunte contando desde uno
for f in range(0,m):
    for c in range(0,m):
        A[f,c]=(input("Elemento a["+str(f+1)+","+str(c+1)+"]"))
        u[f,c]=A[f,c]
print("Introduce los elementos de b")
for f in range(0,m):
    numeros= int(input("Elemento b["+str(f+1)+"]"))
    b.append(numeros)
   
def factor_LU(A):
    #Operaciones para hacer ceros debajo de la diagonal
    for k in range(0,m):
        for f in range(0,m):
            if (k==f):
                l[k,f]=1
            if(k<f):
                factor=(A[f,k]/A[k,k])
                l[f,k]=factor
                for c in range(0,m):
                    A[f,c]= A[f,c]- (factor*A[k,c])
                    u[f,c]= A[f,c]
    return (l,u)
    
    """
    Comprobación
    matrizr= np.zeros([m,m])
    for f in range(0,m):
        for c in range(0,m):
            for k in range(0,m):
                matrizr[f,c] += (l[f,k]*u[k,c])
    print(matrizr)

    """
L,U=factor_LU(A)
print("Impresión de resultados")
print("Matriz L")
print(L)
print("Matriz U")
print(U)
print("b",b)

#2.Sustitución 1: LY=PB
Y= luci.gauss(L,b)
print(Y)


sol= luci.gauss(U,Y)
print("La solución es: ")
print(sol)
     




