class GestionTienda:
    def __init__(self):
        self.__clientes = {} # Diccionario para búsqueda rápida por cédula

    def registrar_cliente(self, cliente):
        if cliente.cedula not in self.__clientes:
            self.__clientes[cliente.cedula] = cliente

    def buscar_por_cedula(self, cedula):
        if cedula in self.__clientes:
            return self.__clientes[cedula]
        return None