
#Se pide diseñar un programa que obtenga la curva 
#               v=ao+a1r+a2r2
#Sistema de ecuaciones lineales (Mí­nimos cuadrados de orden 2)
#Grafique los puntos experimentales en color azul 
#Grafique en color rojo la curva obtenida para r[0,10]
#Tí­tulo del gráfico: "Análisis de velocidad tubo Pitot 
#Eje x=r(cm)
#Eje y v(cm/s)
#Activar cuadrí­cula


import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as alg


from IPython import get_ipython
ipython=get_ipython()
ipython.magic("clear")

#Necesito una función de sumatoria

def sumatorias(r,v):
    n=len(r)
    sumar=0.0
    sumar2=0.0
    sumar3=0.0
    sumar4=0.0
    sumav=0.0
    sumavr=0.0
    sumavr2=0.0
    for i in range(0,n,1):
        sumar+=r[i]
        sumar2+=r[i]**2
        sumar3+=r[i]**3
        sumar4+=r[i]**4
        sumav+=v[i]
        sumavr+=v[i]*r[i]
        sumavr2+=v[i]*r[i]**2
        
    a=sumar
    b=sumar2
    c=sumar3
    d=sumar4
    e=sumav
    f=sumavr
    g=sumavr2
    
    return(a,b,c,d,e,f,g)

#Datos exp

v=np.array([600.0,550.0,450.0,312.0,240.0])
r=np.array([0,3,5,7,8])
n=5

#Cálculo de las sumatorias

a,b,c,d,e,f,g=sumatorias(r,v)

#Vector de sumatorias

vsum=np.array([a,b,c,d,e,f,g])

#Matriz de coeficientes

coeficientes=np.array([[n,vsum[0],vsum[1]],[vsum[0],vsum[1],vsum[2]],[vsum[1],vsum[2],vsum[3]]])

#Vector de términos independientes

terminos=np.array([[vsum[4]],[vsum[5]],[vsum[6]]])


#Matriz inversa de coeficientes

invcoeficientes=alg.inv(coeficientes)


#Producto punto y vector de incognitas encontradas


incognitas=np.dot(invcoeficientes,terminos)

xgraf=np.zeros(10)
ygraf=np.zeros(10)

for i in range (0,10):
    xgraf[i]=i
    ygraf[i]=incognitas[0]+incognitas[1]*i+incognitas[2]*i**2


plt.plot(xgraf,ygraf,"r",label="Función modelo")
plt.plot(r,v,"b",label="Datos experimentales")
plt.title("Análisis de velocidad tubo PITOT")
plt.xlabel("r(cm)")
plt.ylabel("v(cm/s)")
plt.legend()
plt.grid()

