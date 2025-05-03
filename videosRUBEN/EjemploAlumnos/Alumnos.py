#Meter la estructura de datos que necesitamos para los alumnos
class alumno:
    def __init__(self):
        self.Dni = ""
        self.Nombre = ""
        self.Apellidos = ""
        self.Telefono = ""
        self.Nacimiento = fecha()

class fecha:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

def LeerAlumnos(filename):
    Alumnos = []
    F = open("Alumnos.txt","r",encoding = "utf-8")
    linea = F.readline().rstrip() #leemos la primera linea
    while linea != "":          #Mientras que tengamos lineas
        trozos = linea.split("|")
        if len(trozos) == 4:    #Formato de lectura valido
            A = alumno()        #Empieza el ciclo de TRATAR la LINEA
            A.Dni = trozos[0]
            #Ahora quiero separar apellidos del nombre
            trozosN = trozos[1].split(",")
            A.Nombre = trozosN[1]
            A.Apellidos = trozosN[0]
            A.Telefono = trozos[2]
            trozosF = trozos[3].split("-")
            A.Nacimiento.dia = int(trozosF[0])
            A.Nacimiento.mes = int(trozosF[1])
            A.Nacimiento.ano = int(trozosF[2])
            Alumnos.append(A)
        linea = F.readline().rstrip()
    F.close()
    return Alumnos

def EscribirAlumnos(filename, Alumnos):
    F = open(filename, "w", encoding = "utf-8")
    for A in Alumnos:
        F.write(A.Dni)
        F.write("|")
        F.write(A.Apellidos)
        F.write(", ")
        F.write(A.Nombre)
        F.write("|")
        F.write(A.Telefono)
        F.write("|")
        F.write(str(A.Nacimiento.dia))
        F.write("-")
        F.write(str(A.Nacimiento.mes))
        F.write("-")
        F.write(str(A.Nacimiento.ano))
        F.write("\n")
    F.close()

def ListarAlumnos(Alumnos):
    print("Listado de alumnos")
    print("===================")
    for A in Alumnos:
        print("{0:<10} {1:<30} {2:<20} {3:02d}-{4:02d}-{5:04d}".format(A.Dni,A.Nombre + " " + A.Apellidos,A.Telefono,A.Nacimiento.dia,A.Nacimiento.mes,A.Nacimiento.ano))
    print()

def AnadirAlumno(Alumnos):
    A = alumno()
    A.Dni = input("Dime tu DNI: ")
    A.Nombre = input("nombre: ")
    A.Apellidos = input("Apellidos: ")
    A.Telefono = input("Teléfono: ")
    A.Nacimiento.dia = int(input("Nacimiento día: "))
    A.Nacimiento.mes = int(input("Nacimiento mes: "))
    A.Nacimiento.ano = int(input("Nacimiento ano: "))
    Alumnos.append(A)
#Programa principal

def menuPrincipal():
    op = -1
    while op < 0 or op > 3:
        print("1-Listar alumnos")
        print("2-Añadir alumnos")
        print("3-Guardar en fichero")
        print("0-Salir")
        op = int(input("dime una opcion: "))
    return op
fname = input ("Nombre del fichero: ")
X = LeerAlumnos("Alumnos.txt")

opcion = menuPrincipal()
while opcion != 0:
    if opcion == 1:
        ListarAlumnos(X)
    if opcion == 2:
        AnadirAlumno(X)
    if opcion == 3:
        EscribirAlumnos(fname, X)
    if opcion != 0:
        opcion = menuPrincipal()
print("Adeu siau!")
ListarAlumnos(X)
AnadirAlumno(X)
ListarAlumnos(X)
EscribirAlumnos("Alumnos.txt",X)
