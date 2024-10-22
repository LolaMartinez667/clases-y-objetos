class Eevee:

    def __init__(self, nombre, tipo, nivel, peso, altura):
        self._nombre = nombre
        self._tipo = tipo
        self.nivel = nivel 
        self.peso = peso
        self.altura = altura

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·tipo:", self._tipo)
        print("·nivel:", self.nivel)
        print("·peso:", self.peso)
        print("·altura:", self.altura)

    def _aumentar_nivel(self):
        self.nivel += 1

class Umbreon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)
    
    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Sylveon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Jolteon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Vaporeon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Leafeon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Flareon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Glaceon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

class Espeon(Eevee):
    def __init__(self, nombre, tipo, nivel, peso, altura):
        super().__init__(nombre, tipo, nivel, peso, altura)

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Tipo:", self._tipo)
        print("·Nivel:", self.nivel)
        print("·Peso:", self.peso)
        print("·Altura:", self.altura)

pokemon = Eevee("Eevee", "Normal", 19, "6,5 kg", "30 cm")
pokemon.atributos()

umbreon = Umbreon("Umbreon", "Siniestro", 25, "27 kg", "100 cm")
umbreon.atributos()

sylveon = Sylveon("Sylveon", "Hada", 22, "23 kg", "120 cm")
sylveon.atributos()

jolteon = Jolteon("Jolteon", "Eléctrico", 30, "24 kg", "80 cm")
jolteon.atributos()

vaporeon = Vaporeon("Vaporeon", "Agua", 28, "29 kg", "100 cm")
vaporeon.atributos()

leafeon = Leafeon("Leafeon", "Hierba", 26, "25 kg", "90 cm")
leafeon.atributos()

flareon = Flareon("Flareon", "Fuego", 27, "25 kg", "85 cm")
flareon.atributos()

glaceon = Glaceon("Glaceon", "Hielo", 24, "23 kg", "105 cm")
glaceon.atributos()

espeon = Espeon("Espeon", "Psíquico", 28, "25 kg", "95 cm")
espeon.atributos()