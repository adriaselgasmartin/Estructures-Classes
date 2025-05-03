"""Define a struct/class that holds the information of an airline company: it has a name,
a list of aircraft, and the information of the workers. For each aircraft the struct must
store the aircraft callsign, the aircraft type and the year it was build. For the
company workers the information to keep is the number of pilots, the number of
flight assistants and the number of ground workers. Then write the code to initialize
two variables, C1 and C2, with the data for two companies, entered by the user.
After that, create a new company CF as the result of the fusion the two previous.
Show the data of CF in the display"""







class Company:
    def __init__(self, name, aircrafts, workers):
        self.name = name
        self.aircrafts = aircrafts
        self.workers = workers

class Aircraft:
    def __init__(self, callsign, type, year):
        self.callsign = callsign
        self.type = type
        self.year = year
class Workers:
    def __init__(self, pilots, assistants, ground):
        self.pilots = pilots
        self.assistants = assistants
        self.ground = ground

name = input ("Escribe el nombre de la primera compañía: ")
print ('Introduce los datos de las aeronaves de esa compañia')
print ('Escribe todos los datos de cada aeronave en una linea, separados por un espacio')
print ('Escribe una linea vacía para acabar')

#2 variables, C1 i C2, les dues són companyies, les dades les introdueix l'usuari
#Aleshores es crea CF, que es la barreja entre les dues
aircrafts = []
fin = False
while not fin:
    line = input("Aeronave: ")
    if len(line) == 0:
        fin = True
    else:
        trozos = line.strip().split()
        aircrafts.append(Aircraft(trozos[0], trozos[1], int(trozos[2])))
print("Introduce ahora los datos de los trabajadores; numero de pilotos, asistentes y personal de tierra: ")
line = input("Introduce los datos separados por espacios: ")
trozos = line.strip().split()
trabajadores = []
trabajadores.append(Workers(int(trozos[0]),int(trozos[1]),trozos[2]))

C1 = Company(name, aircrafts, trabajadores)

#Ahora la segunda compañía


name = input ("Escribe el nombre de la segunda compañía: ")
print ('Introduce los datos de las aeronaves de esa compañia')
print ('Escribe todos los datos de cada aeronave en una linea, separados por un espacio')
print ('Escribe una linea vacía para acabar')

#2 variables, C1 i C2, les dues són companyies, les dades les introdueix l'usuari
#Aleshores es crea CF, que es la barreja entre les dues
aircrafts = []
fin = False
while not fin:
    line = input("Aeronave: ")
    if len(line) == 0:
        fin = True
    else:
        trozos = line.strip().split()
        aircrafts.append(Aircraft(trozos[0], trozos[1], int(trozos[2])))
print("Introduce ahora los datos de los trabajadores; numero de pilotos, asistentes y personal de tierra: ")
line = input("Introduce los datos separados por espacios: ")
trozos = line.strip().split()
trabajadores = []
trabajadores.append(Workers(int(trozos[0]),int(trozos[1]),trozos[2]))

C2 = Company(name, aircrafts, trabajadores)


name = "Fusion"
AircraftsFusioned = C1.aircrafts + C2.aircrafts
workers = Workers(C1.workers.pilots + C2.workers.pilots, C1.workers.assistants + C2.workers.assistants, C1.workers.ground + C2.workers.ground)
CF = Company ("fusion", AircraftsFusioned, workers)

print ('Datos de la nueva compañia')
print ('Nombre: ', CF.name)
print ('Aeronaves: ')
for aeronave in CF.aircrafts:
 print (aeronave.callsign)
print ('Trabajadores')
print ('Pilotos: ', CF.workers.pilots)
print ('Asistentes: ', CF.workers.assistants)
print ('Personal de tierra: ', CF.workers.ground)




