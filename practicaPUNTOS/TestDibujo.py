'''Llegir el fitxer de punts.

Comprovar si s’ha llegit correctament.

Mostrar el conjunt de punts en un gràfic.'''


import Dibujo
D = Dibujo.CreateFromFile("listapuntos.txt")
Dibujo.Plot(D)