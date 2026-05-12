class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = []  # Aquí se cumple la asociación de 1 a muchos

    def agregar_factura(self, factura):
        self.__facturas.append(factura)

    @property
    def cedula(self):
        return self.__cedula

    @property
    def facturas(self):
        return self.__facturas

    @property
    def nombre(self):
        return self.__nombre