from pip._internal import cli


class Cliente():
    def __init__(self,cod,nom):
        self.codigo = cod
        self.nombre = nom



def Pedir(cli):
    cli.codigo = int(input("Dime el codigo: "))
    cli.nombre = input("Dime el nombre: ")

def Pintar(cli):
    print(cli.codigo, cli.nombre)

if __name__ == "__main__":
    print("Aquest es el programa de prova")
    print("fot el camp!")