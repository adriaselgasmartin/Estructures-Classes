#4 funcions
#Afegir punts
#crear-los des d'un fitxer
#representar-los graficament
import matplotlib.pyplot as plt
import punto
class dibujo:
    def __init__(self):
        self.puntos = []

def AddPoint(D, P):
    for k in D.puntos:
        if k.x == P.x and k.y == P.y:
            return False
    D.puntos.append(P)
    return True


def CreateFromFile(filename):
    F = open(filename, "r")
    linea = F.readline()
    D = dibujo()

    while linea != "":
        partes = linea.strip().split()
        if len(linea) == 3:
            x = float(partes[0])
            y = float(partes[1])
            color = partes[2]
            P = punto.punto(x,y,color)
            AddPoint(D,P)
        linea = F.readline()
    F.close()
    return D

def Plot(dibujo):
    for p in dibujo.puntos:
        plt.plot(p.x,p.y, "o", color = p.color, markersize = 4)
    plt.show()



