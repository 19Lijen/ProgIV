class Factura:
    def __init__(self, fecha):
        self.fecha = fecha
        self.productos = []
        self.valor_total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)

        if hasattr(producto, 'valor'):
            self.valor_total += producto.valor
        else:
            self.valor_total += producto.precio