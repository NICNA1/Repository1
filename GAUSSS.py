#import numpy as np

A=[[1,2],[4,0]]
B=[0,1]
G=A
for i in range(len(G)):
    G[i].append(B[i])
filas=len(G)
columnas=len(G[0])
print(filas,columnas)

print("A=",A,"B=",B,"G=",G)

"""for i in range(0,filas):
    for j in range(0,columnas):
        if i == j and G[i,j]==0:
            for k in range(0,filas):
                if G[k,j]!=0:
                    print(G[k],G[i],"i=",i,"k=",k)
                    G[[]]
                    print(turuleta,cuchufleta)
                    print(G)"""
                   
        
            

    
        
    


