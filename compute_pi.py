
"""

Cálculo del valor para el número PI

"""

#Write a program that takes N as an input from the user
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipython=get_ipython()
ipython.magic("%clear")
#Método de Leibniz

def leb (datok,datopileb):
    n=len(datok)
    summ=0.0
    for i in range(0,n,1):
        summ+=(1/((4*i+1)*(4*i+3)))
        datok[i]=i
        datopileb[i]=8*summ
    return(datok,datopileb)

#Método de euler

def eul (x,y):
    n=len(x)
    sum=0.0
    for i in range (1,n+1,1):
        sum+=1/(i**2)
        x[i-1]=i
        y[i-1]=np.sqrt(6*sum)
        
    return(x,y)

#Calculo error

def err(er):
    er=np.abs((piT-er)/piT)*100
    
    return er

#Main del programa

n=int(input("Ingrese un valor entero de N: "))

ipython.magic("%clear")

#Vectores
kvec=np.zeros(n)
pilebb=np.zeros(n)
pieleberr=np.zeros(n)

keul=np.zeros(n)
pieul=np.zeros(n)
pieulerr=np.zeros(n)

#Uso de las funciones
kvec,pilebb=leb(kvec,pilebb)
keul,pieul=eul(keul,pieul)

#Calculo error
piT=3.141592
#Error caso leb
for i in range (0,n,1):
    pieleberr[i]=err(pilebb[i])
    
#Error caso eul

for i in range (0,n,1):
    pieulerr[i]=err(pieul[i])
    
plt.figure(1)

plt.plot(kvec,pilebb,label="Método de Leibniz")
plt.plot(keul,pieul,label="Método de Euler")
plt.xlabel("Valores de k")
plt.ylabel("Valor de PI")
plt.legend()
plt.title("Valores de pi con variaciones en k por los métodos de Euler y Leibniz")
plt.grid()
    
plt.figure(2)
plt.title("Error respecto a k")
plt.plot(kvec,pieleberr,label="Error con el método de Leibniz")
plt.plot(keul,pieulerr,label="Error con método de Euler")
plt.xlabel("Valores de k")
plt.ylabel("%Error")
plt.legend()
plt.grid()

print("Con una N de: ",n)
print("Se observa que tras el aumento en los valores de k, los valores obtenidos de PI son cada vez más cercanos al valor teórico de PI")
print("En la gráfica de los errores se tiene que con el aumento de k disminuye el porcentaje de error de PI comparado con un valor teórico de 3.141592")
print("\n")
print("El valor más cercano para PI obtenido con el método de Leibniz fue de: ",pilebb[-1],"con un porcentaje de error del ",pieleberr[-1],"%")
print("\n")
print("El valor más cercano para PI con el metodo de Euler fue de: ",pieul[-1],"con un porcentaje de error del",pieulerr[-1],"%")

