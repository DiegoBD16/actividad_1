class Bicicleta:
    def __init__(self, kilometros_totales, color):
        self.kilometros_recorridos = 0
        self._kilometros_totales = kilometros_totales
        self.color = color

    def circular(self, kilometros):
        self.kilometros_recorridos = kilometros
        self._kilometros_totales += kilometros
        return(f"Has recorrido {self.kilometros_recorridos}")
    
    @property
    def kilometros_totales(self):
        return self._kilometros_totales
    
    def comprobar_ruedas(self):
        if self._kilometros_totales >= 1000:
            return("Es recomendable cambiar las ruedas")
        else:
            return("Las ruedas estan bien")
    
    def cambiar_ruedas(self):
        self._kilometros_totales = 0
        return("Las ruedas se han cambiado")

class Coche:
    def __init__(self, kilometros_totales, color):
        self.kilometros_recorridos = 0
        self._kilometros_totales = kilometros_totales
        self.color = color

    def circular(self, kilometros):
        self.kilometros_recorridos = kilometros
        self._kilometros_totales += kilometros
        return(f"Has recorrido {self.kilometros_recorridos}")
    
    @property
    def kilometros_totales(self):
        return self._kilometros_totales
    
    def comprobar_ruedas(self):
        if self._kilometros_totales >= 10000:
            return("Es recomendable cambiar las ruedas")
        else:
            return("Las ruedas estan bien")
    
    def cambiar_ruedas(self):
        self._kilometros_totales = 0
        return("Las ruedas se han cambiado")

def main():
    menu_crear = ["Coche", "bicicleta", "Ir al menú de vehículos", "Salir"]
    menu_accion = ["Andar con el coche", "Andar con la bicicleta", "Ver Km del coche", "Ver km de la bicicleta", "Recomendación del coche", "Recomendación de la bicicleta", "Cambiar ruedas del coche", "Cambiar ruedas de la bicicleta", "Salir"]
    coche_existente = False
    bicicleta_existente = False
    crear = int
    hacer = int

    while crear != 3:
        print("¿Que quieres crear?")
        for indice, elemento in enumerate(menu_crear):
            print(f"{indice}. {elemento}")
        crear = int(input("Elige una opcion 0-3: "))
        match crear:
            case 0:
                if coche_existente == False:
                    kilometros = int(input("¿Cuantos kilometros ha conducido el coche?: "))
                    color = str(input("¿De que color es el coche?: "))
                    coche = Coche(kilometros, color)
                    coche_existente = True
                else:
                    print("El coche ya existe")
            case 1:
                if bicicleta_existente == False:
                    kilometros = int(input("¿Cuantos kilometros ha conducido la bicicleta?: "))
                    color = str(input("¿De que color es la bicicleta?: "))
                    bicicleta = Bicicleta(kilometros, color)
                    bicicleta_existente = True
                else:
                    print("La bicicleta ya existe")
            case 2:
                hacer = 0
                while hacer != 8:
                    print("¿Que quieres hacer?")
                    for indice, elemento in enumerate(menu_accion):
                        print(f"{indice}. {elemento}")
                    hacer = int(input("Elige una opcion 0-8: "))
                    match hacer:
                        case 0:
                            if coche_existente == False:
                                print("No tenemos coche")
                            else:
                                kilometros = int(input("¿Cuantos kilometros vamos a circular?: "))
                                print(coche.circular(kilometros))
                        case 1:
                            if bicicleta_existente == False:
                                print("No tenemos bicicleta")
                            else:
                                kilometros = int(input("¿Cuantos kilometros vamos a circular?: "))
                                print(bicicleta.circular(kilometros))
                        case 2:
                            if coche_existente == False:
                                print("No tenemos coche")
                            else:
                                print(coche.kilometros_totales)
                        case 3:
                            if bicicleta_existente == False:
                                print("No tenemos bicicleta")
                            else:
                                print(bicicleta.kilometros_totales)
                        case 4:
                            if coche_existente == False:
                                print("No tenemos coche")
                            else:
                                print(coche.comprobar_ruedas())
                        case 5:
                            if bicicleta_existente == False:
                                print("No tenemos bicicleta")
                            else:
                                print(bicicleta.comprobar_ruedas())
                        case 6:
                            if coche_existente == False:
                                print("No tenemos coche")
                            else:
                                print(coche.cambiar_ruedas())
                        case 7:
                            if bicicleta_existente == False:
                                print("No tenemos bicicleta")
                            else:
                                print(coche.cambiar_ruedas())
                        case 8:
                            print("Volviendo al menu anterior")
            case 3:
                print("Adios")
main()