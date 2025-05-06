import matplotlib.pyplot  as plt
import Punto

#Una estructura de un vector de puntos
class dibujo:
    def __init__(self):
        self.puntos =  []       #vector de puntos
#Cada elemento es un punto, tal como está definido en punto.py

"""
D = Dibujo
P = punto a añadir
"""
def AddPoint(D, P):
    for k in D.puntos:
        if k.x == P.x and k.y == P.y:
            return False
    D.puntos.append(P)
    return True
#Inserta un punto dentro del dibujo

def CreateFromFile(filename):
    #Crear un dibujo a partir del fichero Puntos.txt
    try:
        F = open(filename, "r")
    #Leer linea por linea el fichero e ir almacenando los puntos
    except:
       return None
    linea = F.readline()
    D = dibujo()
    while linea != "":
        partes = linea.strip().split()
        if len(partes) == 3:
            try:
                x = float(partes[0])
                y = float(partes[1])
                color = str(partes[2])
                P = Punto.punto(x,y,color)
                AddPoint(D,P)
            except:
                print("Error el la linea: ",linea)
                pass
        linea = F.readline()
    F.close()
    return D


def Plot(D):
    #recorrer todos los elementos del dibujo y hacer un plot
    for p in D.puntos:
        plt.plot(p.x, p.y, "o", color = p.color, markersize = 3)
    plt.show()

