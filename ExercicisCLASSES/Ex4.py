"""Define a struct/class Agenda as the list of appointments, where one appointment
contains the date, time, place and description of the appointment. The date is also
a struct Tdate which has year, month, day and weekday. The time is float in the
interval [0 – 23.5] giving hours or half hours. The other fields are strings. Then write
the code to ask the user for the information of an appointment and create an
agenda with the appointment entered. Show the result in the display. Finally write
the code that creates a copy of the appointment stored in the agenda, changes the
time slot with data entered by the user and stores the new appointment in the
agenda.
"""
import time
class Appointment:
    def __init__(self, date, time, place, description):
        self.date = date
        self.time = time #float between 0 and 23.5
        self.place = place
        self.description = description

class Tdate:
    def __init__(self, year, month, day, weekday):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

print("welcome to the Appointment agenda program!")
print("\n")
time.sleep(2)
try:
    agenda = [] #list of appointments
    print("Introduce todos los datos separados por espacio ")
    line = input("Escribe los datos de la fecha separados por espacios: ")
    trozos = line.rstrip().split()
    fecha = Tdate (int(trozos[0]),int(trozos[1]), int(trozos[2]),trozos[3])

    hora = eval(input("Hora: "))
    lugar = input("Lugar: ")
    descripcion = input("Pequeña descripción del evento: ")
    cita = Appointment(fecha, hora, lugar, descripcion)
    agenda.append(cita)

    for cita in agenda:
        print("Fecha de la cita: {0},{1},{2},{3}".format(cita.date.year, cita.date.month,
                                              cita.date.day, cita.date.weekday))

        print("Hora del evento: ",cita.time)
        print("Lugar: ",cita.place)
        print('Descripcion: ', cita.description)
    nuevaHora = eval(input(""))





except ValueError:
    print("Error: Por favor, introduce los datos en el formato correcto")