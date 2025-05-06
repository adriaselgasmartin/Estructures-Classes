class asignatura:
    def __init__(self,nombre, creditos, porcentaje):
        self.nombre = nombre
        self.creditos = creditos
        self.porcentaje = porcentaje #int
miLista = []
print("Introduzca los datos de 4 asignaturas separados por espacios:")
i = 0
while i !=4:
    linea = input("Nombre, Creditos, Porcentaje: ")
    partes = linea.rstrip().split()
    a = asignatura(partes[0], int(partes[1]), int(partes[2]))
    miLista.append(a)
    i += 1

"""
obtener una nueva lista con las asignaturas
“María”, que son las asignaturas con un porcentaje de aprobados superior al 75% y
escribir en consola los nombres de esas asignaturas (un nombre por línea de
consola).
"""
#Hauré de construir un vector nou amb aquestes asignatures
marias = []
j = 0

while j < len(miLista):
    if miLista[j].porcentaje > 75:
        marias.append(miLista[j])
        j = j + 1
    else:
        j += 1
for i in range (len(marias)):
    print(marias[i].nombre)

    '''mates 6 78
    quimica 8 80
    fisica 6 45
    eg 3 10
    '''