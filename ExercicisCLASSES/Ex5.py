"""Define a struct/class TFlightPlan which contains: the code of the departure airport, the code
of the arrival airport, the flight level for the cruise, the departure time, the arrival time and
the 4D trajectory. To specify each waypoint of the 4D trajectory use a list of TwayPoint. A
TwayPoint is a struct containing the identification name, lat and lon of a navigation Fix, and
the estimated time over. Then write the code to initialize a variable F with a test TflightPlan.
Finally, show the user the departure and arrival times and ask him/her to enter some time
value when the aircraft is in flight. The program should show the waypoint name the aircraft
will be heading towards at the entered time"""

class TFlightPlan:
    def __init__(self, departure, arrival, level, departureTime, arrivalTime, trajectory):
        self.departure = departure
        self.arrival = arrival
        self.level = level
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.trajectory = trajectory

class TwayPoint:
    def __init__(self, id, lat, lon, time):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.time = time

#variable F test FlightPlan
try:
    linea = input("Escriu les dades del vol separades per espais: \n")
    trozos = linea.strip("\n").split()
    F = TFlightPlan(trozos[0], trozos[1], int(trozos[2]), float(trozos[3]), float(trozos[4]),None)
    print("Introdueix els Waypoints, cadascun en una linea amb les dades separades amb espais:\n")
    trayectoria = []
    fin = False
    while not fin:
        line = input("Waypoint: ")
        if len(linea) > 0:      #això vol dir que l'usuari ha omplert (minimament) el FlightPlan
            trozos = line.strip("\n").split()
            Wp = (trozos[0], float(trozos[1]), float(trozos[2]), float(trozos[3]))
            trayectoria.append(Wp)
        else:
            fin = True
    F.trajectory = trayectoria
    hora = eval(input("Introdueix una hora del dia: "))
    encontrado = False
    i = 0
    while i < len(trayectoria) and not encontrado:
        if F.trajectory[i].time == hora:
            encontrado = True

        if not encontrado:
            i=i+1
    if encontrado:
        print("Resultado: ",F.trajectory.name[i])
    if not encontrado:
        print("No hay waypoint sobrevolado a esa hora")
except ValueError:
    print("Error de formato")