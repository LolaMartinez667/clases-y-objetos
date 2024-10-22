class eevee:

    def __init__(self, nombre, tipo, nivel, peso, altura):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel 
        self.peso = peso
        self.altura = altura

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·tipo:", self.tipo)
        print("·nivel:", self.nivel)
        print("·peso:", self.peso)
        print("·altura:", self.altura)

pokemon = eevee("Eevee", "Normal", 12, "6 kg", "30 cm")
pokemon.atributos()


