
#Librerías

import Moduloss as md
import numpy as np
import matplotlib.pyplot as plt

"""Con ingreso de datos por el usuario"""
#Main que permita el ingreso de datos
# n=int(float(input("¿Cuántos datos tiene de carga?: ")))
# F=np.zeros(n)
# L=np.zeros(n)
# S=float(input("Ingrese el valor para su sección rectangular [mm2]: "))
# L0=int(input("Ingrese la longitud inicial (L0):  "))
# for i in range(0,n,1):
#     F[i]=float(input("Ingrese el valor de la carga "+str(i+1)+" [N]: "))
#     L[i]=float(input("Ingrese el valor de longitud "+str(i+1)+" [mm]: "))

#lONGITUD INICIAL

"""Con los datos recolectados inicialmente"""
n=12
S=50 #mm2
L0=100
F=np.array([0,1394,2808,5686,7502,8221,9969,12979,14241,14483,13968,12625])
L=np.array([100,100.03,100.08,100.13,100.2,100.25,100.64,101.91,103.18,104.45,105.72,106.99])

#Para la tensión

T=md.tension(S,F)


#Para el alargamiento unitario

au=md.alargamiento(L,L0)

#Generación de matriz

sln=np.ones(shape=(n,2))

for i in range(0,n,1):
    sln[i,0]=T[i]
    sln[i,1]=au[i]
    
#Matriz resultante
print("   Tensión   Alargamiento unitario")
print(sln)

#Gráfico
plt.figure(1)
plt.plot(au,T,marker="o",markersize=5)
plt.title("Gráfico de Tensión vs. Alargamiento")
plt.ylabel("Tensión [N/mm2]")
plt.xlabel("Alargamiento unitario (ε)")
plt.grid()
