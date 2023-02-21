# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:53:01 2023

@author: itziar
"""

import numpy as np
def gauss(A,B): 
    #Resuelve  el nuevo sistema lineal con el nuevo vector b=DB
    #el vector solución se llamará coef
    A= np.array(A,dtype=float)

    #Matriz ampliada
    #AB= np.concatenate((A,B),axis=1)
    AB = np.c_[A,B] 
    AB0= np.copy(AB)
    #PIVOTE
    tamano= np.shape(AB)
    n=tamano[0]
    m=tamano[1]

    for i in range(0,n-1,1):
        #columna desde diagonal i en adelante
        columna= abs(AB[i:,i])
        dondemax= np.argmax(columna)
        
        #dondemax no está en la diagonal
        if (dondemax !=0):
            #para intercambiar filas
            temporal =np.copy(AB[i,:])
            AB[i,:]= AB[dondemax+i,:]
            AB[dondemax+i,:]=temporal
    AB1= np.copy(AB)
    #eliminación
    for i in range (0, n-1,1):
        pivote= AB[i,i]
        adelante= i+1
        for k in range (adelante, n,1):
            factor= AB[k,i]/pivote
            AB[k,:]=AB[k,:]- AB[i,:]*factor
            
    #sustitución
    ultfila= n-1
    ultcolumna= m-1
    X=np.zeros(n,dtype=float)

    for i in range(ultfila, 0-1,-1):
        suma= 0
        for j in range (i+1,ultcolumna, 1):
            suma= suma + AB[i,j]*X[j]
        b= AB[i,ultcolumna]
        X[i]= (b-suma)/AB[i,i]
    X= np.transpose([X])
    coef= X
    #print(coef)
    return coef
    