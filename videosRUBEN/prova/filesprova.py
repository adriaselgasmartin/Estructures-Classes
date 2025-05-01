F = open("hola.txt", "r")
linea = F.readline()
while linea != "":
    partes = linea.strip().split()
    linea = F.readline()
    print(partes[2])
F.close()