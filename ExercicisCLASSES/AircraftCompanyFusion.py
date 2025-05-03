class Workers:
    def __init__(self, pilots, assistants, ground):
        self.pilots = pilots
        self.assistants = assistants
        self.ground = ground


class Aircraft:
    def __init__(self, callsign, type, year):
        self.callsign = callsign
        self.type = type
        self.year = year


class Company:
    def __init__(self, name, aircrafts, workers):
        self.name = name
        self.aircrafts = aircrafts
        self.workers = workers


# Lectura i creació de la primera companyia
name = input("Escribe el nombre de la primera compañía: ")
print('Introduce los datos de las aeronaves de esa compañía')
print('Escribe todos los datos de cada aeronave en una línea, separados por un espacio')
print('Escribe una línea vacía para acabar')
aircarfts = []
fin = False
while not fin:
    line = input('aeronave: ')
    if len(line) == 0:
        fin = True
    else:
        trozos = line.split(' ')
        if len(trozos) == 3:  # Comprovem que tenim exactament 3 elements
            aircarfts.append(Aircraft(trozos[0], trozos[1], trozos[2]))
        else:
            print("Introduce exactamente 3 datos: callsign, type, year.")

print('Introduce los datos de los trabajadores')
line = input('datos separados por espacio (pilotos asistentes tierra): ')
trozos = line.split(' ')
if len(trozos) == 3:
    workers = Workers(int(trozos[0]), int(trozos[1]), int(trozos[2]))
else:
    print("Se esperaban exactamente 3 datos para los trabajadores. Inténtalo nuevamente.")
    exit()  # Si l'entrada és incorrecta, sortim del programa

C1 = Company(name, aircarfts, workers)

# Lectura i creació de la segona companyia
name = input("Escribe el nombre de la segunda compañía: ")
print('Introduce los datos de las aeronaves de esa compañía')
print('Escribe todos los datos de cada aeronave en una línea, separados por un espacio')
print('Escribe una línea vacía para acabar')
aircarfts = []
fin = False
while not fin:
    line = input('aeronave: ')
    if len(line) == 0:
        fin = True
    else:
        trozos = line.split(' ')
        if len(trozos) == 3:  # Comprovem que tenim exactament 3 elements
            aircarfts.append(Aircraft(trozos[0], trozos[1], trozos[2]))
        else:
            print("Introduce exactamente 3 datos: callsign, type, year.")

print('Introduce los datos de los trabajadores')
line = input('datos separados por espacio (pilotos asistentes tierra): ')
trozos = line.split(' ')
if len(trozos) == 3:
    workers = Workers(int(trozos[0]), int(trozos[1]), int(trozos[2]))
else:
    print("Se esperaban exactamente 3 datos para los trabajadores. Inténtalo nuevamente.")
    exit()

C2 = Company(name, aircarfts, workers)

# Fusió de les dues companyies
aircrafts = C1.aircrafts + C2.aircrafts
workers = Workers(C1.workers.pilots + C2.workers.pilots,
                  C1.workers.assistants + C2.workers.assistants,
                  C1.workers.ground + C2.workers.ground)

CF = Company('Fusion', aircrafts, workers)

# Impressió de les dades de la nova companyia
print('Datos de la nueva compañía')
print('Nombre: ', CF.name)
print('Aeronaves: ')
for aeronave in CF.aircrafts:
    print(aeronave.callsign)
print('Trabajadores')
print('Pilotos: ', CF.workers.pilots)
print('Asistentes: ', CF.workers.assistants)
print('Personal de tierra: ', CF.workers.ground)