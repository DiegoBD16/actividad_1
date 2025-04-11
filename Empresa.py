#comentario

class Productos:
    def __init__(self, nombre, fecha_caducidad, N_Lote, peso, medida):
        self.nombre = nombre
        self.caducidad = fecha_caducidad
        self.lote = N_Lote
        self.peso = peso
        self.medida = medida
    
    def precio(self):
        return self.peso *3

    def __str__(self):
        return f"El producto {self.nombre} caduca el {self.caducidad} y pertenece al lote {self.lote}, el peso del producto son {self.peso} Kg y sus medidas son {self.medida}, cuesta un total de {self.precio}"
    
class Frescos(Productos):
    def __init__(self, nombre, fecha_caducidad, N_Lote, peso, medida, fecha_envasado, pais_origen):
        super().__init__(nombre, fecha_caducidad, N_Lote, peso, medida)
        self.fecha = fecha_envasado
        self.pais = pais_origen
    
    def __str__(self):
        return super().__str__() + f", el producto viene de {self.pais} y fue envasado el {self.fecha}"

class Refrigerados(Productos):
    def __init__(self, nombre, fecha_caducidad, N_Lote, codigo_organismo):
        super().__init__(nombre, fecha_caducidad, N_Lote)
        self.codigo = codigo_organismo
    
    def precio(self):
        return super().precio() + 2
    
    def __str__(self):
        return super().__str__() + f", el codigo del producto es {self.codigo}"

class Congelados(Productos):
    def __init__(self, nombre, fecha_caducidad, N_Lote, temperatura_recomendada):
        super().__init__(nombre, fecha_caducidad, N_Lote)
        self.temperatura = temperatura_recomendada
    
    def precio(self):
        return super().precio() + 5
    
    def __str__(self):
        return super().__str__() + f", la temperatura recomendada del producto es de {self.temperatura}ºC"

def main():
    productos_frescos = []
    productos_refrigerados = []
    productos_congelados = []
    productos = []

    respuesta = ""
    
    while respuesta != "no":
        producto = int(input("¿Que producto quieres crear? 1 para Frescos, 2 para Refrigerados y 3 para congelados: "))
        nombre = str(input("Dime el  nombre del producto: "))
        caducidad = input("Dame la fecha de caducidad del producto: ")
        numero_lote = int(input("Cual es su numero de lote?: "))
        peso = int(input("Dime el peso del producto: "))
        medidas = input("Dame las medidas del producto: ")

        if producto == 1:
            envasado = input("Dime la fecha de envasado: ")
            pais = str(input("Dime de que pais llego: "))
            producto = Frescos(nombre, caducidad, numero_lote, peso, medidas, envasado, pais)
            productos_frescos.append(producto)

        elif producto == 2:
            codigo = input("Dime la fecha de envasado: ")
            producto = Refrigerados(nombre, caducidad, numero_lote, peso, medidas, codigo)
            productos_refrigerados.append(producto)

        elif producto == 3:
            temperatura = input("Dime la fecha de envasado: ")
            producto = Congelados(nombre, caducidad, numero_lote, peso, medidas, temperatura)
            productos_congelados.append(producto)
        respuesta = str(input("¿Quieres darme otro producto?: "))

    productos.append(producto)
    
    pregunta_coste_de_envio = str(input("¿Quieres calcular el precio de invio?: ")).lower()
    
    if pregunta_coste_de_envio == "si":
        print("Tenems estos productos: ")
        for indice, elemento in enumerate(productos):
            print(f"{indice}. {elemento}")    
        seleccion = int(input("¿De cual lo quieres calcular?: "))
        print (f"El coste es {productos(seleccion).precio}€")
         
    for indice, elemento in enumerate(productos_frescos):
            print("Productos frescos:")
            print(f"{indice + 1}. {elemento}")
    for indice, elemento in enumerate(productos_refrigerados):
            print("Productos refrigerados:")
            print(f"{indice + 1}. {elemento}")
    for indice, elemento in enumerate(productos_congelados):
            print("Productos congelados:")
            print(f"{indice + 1}. {elemento}")
main()