import matplotlib.pyplot as plt
import Punto

#Una estructura de un vector de puntos
class dibujo:
    def __init__(self):
        self.puntos =  []
#Cada elemento es un punto, tal como está definido en Punto.py

def AddPoint(D, P):
    D.puntos.append(P)
    return True
#Inserta un punto dentro del dibujo





def CreateFromFile(filename):
    F = open(filename, "r")
    #Leer linea por linea el fichero e ir almacenando los puntos
    linea = F.readline()
    D = dibujo()
    while linea != "":
        partes = linea.strip().split()
        linea = F.readline()
        if len(partes) == 3:
            x = float(partes[0])
            y = float(partes[1])
            color = str(partes[2])
            P = Punto.punto(x,y,color)
            AddPoint(D,P)
    F.close()
    return D



def Plot(D):
    #recorrer todos los elementos del dibujo y hacer un plot
    for p in D.puntos:
        plt.plot(p.x, p.y, "o", color = p.color, markersize = 3)
    plt.show()

