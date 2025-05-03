class asignatura:
    def __init__(self, nom, credits):
        self.nom = nom
        self.credits = credits
a1 = asignatura("mates", 6)
print(a1.__dict__)