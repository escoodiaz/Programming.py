

"""Se requiere un código en python que calcule la norma infinito para una matriz de N x 
N. Utilice ciclos en la solución. Consulte y compare su resultado utilizando la siguiente 
función de numpy np.linalg.norm(matriz, np.inf. Hay 
también para la 1 y Frobenius. A continuación se da un ejemplo 
con una matriz de 3x3, pero el cÃ³digo debe funcionar para una matriz cuadrada de 
cualquier tamaño"""


#Librerías


import numpy as np
import numpy.linalg as alg


#Matriz modelo

A1=np.array([[3,-1,4],[-5,0,2],[1,-2,6]])

"""Se puede utilizar cualquier matriz nxn"""

n=len(A1) #Tamaño de matriz

#Con sumatorias y ciclos for

print("Usando sumatorias y ciclos for, se tiene que: \n")

#Para la norma 1

Summc=0.0
for i in range(0,n,1):
    
    Summc+=np.abs(A1[i,:])
    
x=np.max(Summc)

print("la norma 1 es de: ",x)

#Para la norma inf

Summf=0.0
for i in range(0,n,1):
    
    Summf+=np.abs(A1[:,i])
    
x1=np.max(Summf)

print("La norma infinito es de:",x1)

#La norma de frobenius

Summfro=0.0
for i in range(0,n,1):
    Summfro+=A1[:,i]**2
    
x=np.sqrt(np.sum(Summfro))

print("la norma de Frobenius es de ",x)

print("##################################################")

print("Con funciones de Numpy:")


#Utilizando función de numpy

normainfnp=alg.norm(A1,np.inf)
normafronp=alg.norm(A1,"fro")
norma1=alg.norm(A1,1)

print("La norma 1 es de ",norma1)
print("La norma infinito es de ",normainfnp)
print("La norma de Frobenius es de ",normafronp)



    

  
 






   

