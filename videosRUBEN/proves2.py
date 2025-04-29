class Cliente ():
    def __init__(self):
        self.id = 0
        self.nombre =""
        self.edad = 0
#Queremos hacer un vector de clientes
vClientes = []
vClientes.append(Cliente())
vClientes[-1].id = 4
vClientes[-1].nombre = "Joan"
vClientes[-1].edad = 20

x = Cliente()
x.id = 1
x.nombre = "Adriana"
x.edad = 21
vClientes.append(x)

y = Cliente()
y.id = 2
y.nombre = "Pep"
y.edad = 22
vClientes.append(y)
print("Done")

i = 0
while i < len(vClientes):
    print(vClientes[i].__dict__)
    i += 1 
"""
for Cliente in vClientes:
    print(Cliente.__dict__)
    """