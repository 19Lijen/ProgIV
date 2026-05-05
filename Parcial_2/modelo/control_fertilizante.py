from .producto_control import ProductoControl

class ControlFertilizante(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre, frecuencia, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion