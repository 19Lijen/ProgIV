class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []

    def añadir_factura(self, factura):
        self.facturas.append(factura)