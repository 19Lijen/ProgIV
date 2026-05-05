class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, precio):
        if not (400 <= dosis <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 Kg")
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio