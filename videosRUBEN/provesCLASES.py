class Cliente ():
    def __init__(self):
        self.id = 0
        self.nombre =""
        self.edad = 0
c = Cliente()
c.id = int(input("Dona un id: "))
c.nombre = input("El teu nom és: ")
c.edad = int(input("Edad: "))

print(c.__dict__)