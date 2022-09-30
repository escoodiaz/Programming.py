# -*- coding: utf-8 -*-
"""
@author: danie
"""


#Programa que analiza el tipo de fluido según el Reynolds con implementación de interfaz gráfica


from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import sys

ventana="reynols.ui"

class VentanaLogin(QDialog):
    def __init__(self):
        super(VentanaLogin,self).__init__()#Codigo pueda interactuar con cada uno de los widgets
        loadUi(ventana,self)#Función que carga el archivo
        self.setup()
        ##Función para cargar la interfaz grafica
        
    def setup(self):#widgets que van a tener algún evento
        # self.buttonBox.accepted.connect(self.opcion_aceptar)#Boton ok
        # self.buttonBox.rejected.connect(self.opcion_cancelar)
        self.calcular.clicked.connect(self.calculos)
        
    def calculos(self):
        v=float(self.velocidad.text())#Información entra a través del widget
        d=1.325 #Densidad del aire en kg/m3
        u=1.74e-5 #Viscosidad dinámica en kg/(ms)
        dia=0.5 #diametro de la tubería en m
        Re=d*v*dia/u
        self.reynols.setText(str(Re))#Evolución del print se muestra en el widget resultados
       
        if Re<=2300:
            self.tipo.setText("Nos encontramos con un flujo laminar")
        elif Re>2300 and Re<400:
            self.tipo.setText("Nos econntramos con un flujo de transición")
        else:
            self.tipo.setText("Nos encontramos con un flujo turbulento")
    def opcion_aceptar(self):
        pass
        def opcion_cancelar(self):
            pass
    

app=QApplication(sys.argv)
widget=VentanaLogin()
widget.show()
sys.exit(app.exec_())








    
