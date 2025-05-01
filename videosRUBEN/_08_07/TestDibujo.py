import Dibujo

D = Dibujo.CreateFromFile ("Puntos.txt")

if D == None:
    print("Error al abrir el fichero")
else:
    Dibujo.Plot(D)
#Queremos todo el conjunto de puntos de Puntos.txt visualizado en un plot