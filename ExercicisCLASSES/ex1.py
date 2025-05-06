class pelicula:
    def __init__(self,titulo,director,duracion,ano):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.ano = ano
miLista = []
'''busque en la lista una película
que dure menos de dos horas y que sea anterior al año 2000 y escriba en consola
los datos de esa película'''

print("A continuación va a introducir los siguientes datos de 4 peliculas cualesquiera separados por una coma y espacio cuando se le pidan")
i = 0
while i != 2:
    linea = input("Título, Director, Duración, Año: ")
    partes = linea.rstrip().split(", ")
    P = pelicula(partes[0], partes[1], int(partes[2]), int(partes[3]))
    miLista.append(P)
    i += 1
encontrado = False
j = 0
while not encontrado and len(miLista) > j:
    if miLista[j].duracion < 120 and miLista[j].ano < 2000:
        encontrado = True
    else:
        j += 1
if encontrado:
    print("La pelicula que dura menos de 200 minutos y que es anterior al 2000 es: ", miLista[j].titulo)

"""
Cadena Perpetua, tim Robbins, 110, 1999
añlkjhda, aslkdjhaw dañljkd, 1234, 2004
"""