import numpy as np

A=np.array([[3,1],[2,2]])
B=np.array([[1],[1]])
G=np.append(A,B,axis=1)
G=G.astype(np.float32)
n=0
S=[]
X=[]
shape=list((G.shape))
filas=shape[0]
columnas=shape[1]
"""QUITAR 0s DE LA DIAGONAL"""
for i in range(0,filas):
    for j in range(0,columnas):
        if i == j and G[i,j]==0:
            for k in range(0,filas):
                if G[k,j]!=0:
                    Fila1=np.copy(G[k])
                    Fila2=np.copy(G[i])
                    G[k]=Fila2
                    G[i]=Fila1
                    break
print(G)
for j in range(0,columnas):
    for i in range(0,filas):
        if i>n:
            print(G[i]-((G[i][j]/G[n][j])*G[n]))
            G[i]=G[i]-(G[i][j]/G[n][j])*G[n]
    n+=1
print(G)
X1=G[filas-1][columnas-1]/G[filas-1][columnas-2]
X.append(X1)
for j in range(columnas-1,0,-1):
    for i in range(filas-1,0,-1):
        if i==j:
            X.append(S[filas-1-i]/G[i][i])
        if len(S)<filas-1:
            S.append(G[i][columnas]-G[i][j]*X[j])
        S[filas-1-i]
print()(G)
        
    HOLA


