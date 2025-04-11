class Lampara:
    pass

class SistemaIluminacion:
    def __init__(self, brillo_inicial):
        self._brillo = brillo_inicial
    
    @property
    def brillo(self):
        return self._brillo
    
    @brillo.setter
    def brillo(self, valor):
        if valor > 100 or valor < 0:
            print("El valor introducido no es valido")
        else:
            self._brillo = valor

def main():

    lamparas = SistemaIluminacion(0)
    valor = int(input("¿Brillo? (0-100): "))
    lamparas.brillo = valor
    print(lamparas.brillo)

main()