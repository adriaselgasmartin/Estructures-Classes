import Cliente

lista = []


entrada = input("Introduzca su nombre y apellido, escriba tambien su código separado por una coma y un espacio: ")

'''partes = entrada.strip().split(", ")'''
"""C.nombre = partes[0]
C.codigo = partes[1]"""

#Si el codi introduit es divisible per 2, emmagatzemar el client en un vector i després mostrar-lo

while entrada != "":
    partes = entrada.strip().split(", ")
    C = Cliente.Cliente()
    C.nombre = partes[0]
    C.codigo = int(partes[1])

    if C.codigo % 2 == 0:
        lista.append(C)

    entrada = input("Introduzca su nombre y apellido, escriba tambien su código separado por una coma y un espacio: ")
for cliente in lista:
    print(f"Nombre: {cliente.nombre}")