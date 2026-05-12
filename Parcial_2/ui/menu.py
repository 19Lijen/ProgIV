from crud.gestion_tienda import GestionTienda
from modelo.cliente import Cliente
from modelo.factura import Factura
# Importamos todas las clases de productos para poder instanciarlas
from modelo.antibiotico import Antibiotico
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizante import ControlFertilizante

class Menu:
    def __init__(self):
        self.__gestion = GestionTienda()

    def mostrar_menu(self):
        while True:
            print("\n" + "="*30)
            print("      TIENDA AGRÍCOLA UTP")
            print("="*30)
            print("1. Registrar Cliente")
            print("2. Realizar Venta (Facturar)")
            print("3. Buscar Historial por Cédula")
            print("4. Salir")
            print("="*30)
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.__registrar_cliente()
            elif opcion == "2":
                self.__realizar_venta()
            elif opcion == "3":
                self.__buscar_historial()
            elif opcion == "4":
                print("Saliendo del sistema... ¡Éxitos en el parcial!")
                break
            else:
                print(">>> Opción no válida.")

    def __registrar_cliente(self):
        print("\n--- Registro de Cliente ---")
        nombre = input("Nombre completo: ")
        cedula = input("Cédula: ")
        nuevo_cliente = Cliente(nombre, cedula)
        self.__gestion.registrar_cliente(nuevo_cliente)
        print(f"OK: Cliente {nombre} registrado.")

    def __realizar_venta(self):
        print("\n--- Nueva Venta ---")
        cedula = input("Cédula del cliente: ")
        cliente = self.__gestion.buscar_por_cedula(cedula)
        
        if not cliente:
            print("ERROR: El cliente no existe. Regístrelo primero.")
            return

        fecha = input("Fecha de venta (AAAA-MM-DD): ")
        nueva_factura = Factura(fecha)
        
        while True:
            print("\n--- Carrito de Compras ---")
            print("1. Agregar Antibiótico")
            print("2. Agregar Control de Plagas")
            print("3. Agregar Control de Fertilizante")
            print("4. Finalizar y Guardar Factura")
            tipo = input("Seleccione producto: ")

            if tipo == "4":
                break
            
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio unitario: "))

            if tipo == "1":
                dosis = float(input("Dosis (400Kg - 600Kg): "))
                animal = input("Tipo de animal (Bovinos/Porcinos/Caprinos): ")
                producto = Antibiotico(nombre, dosis, animal, precio)
                nueva_factura.agregar_producto(producto)

            elif tipo == "2":
                registro = input("Registro ICA: ")
                frecuencia = input("Frecuencia de aplicación: ")
                carencia = int(input("Periodo de carencia (días): "))
                producto = ControlPlagas(registro, nombre, frecuencia, precio, carencia)
                nueva_factura.agregar_producto(producto)

            elif tipo == "3":
                registro = input("Registro ICA: ")
                frecuencia = input("Frecuencia de aplicación: ")
                fecha_ult = input("Fecha última aplicación: ")
                producto = ControlFertilizante(registro, nombre, frecuencia, precio, fecha_ult)
                nueva_factura.agregar_producto(producto)
            
            print(">>> Producto añadido a la factura.")

        # Guardamos la factura en el historial del cliente
        cliente.agregar_factura(nueva_factura)
        print(f"\nVENTA EXITOSA: Total factura ${nueva_factura.valor_total}")

    def __buscar_historial(self):
        print("\n--- Búsqueda de Historial ---")
        cedula = input("Ingrese cédula: ")
        cliente = self.__gestion.buscar_por_cedula(cedula)
        
        if cliente:
            print(f"\nCLIENTE: {cliente.nombre} | CC: {cliente.cedula}")
            if not cliente.facturas:
                print("No hay compras registradas.")
            else:
                for i, fac in enumerate(cliente.facturas, 1):
                    print(f"\nFactura #{i} - Fecha: {fac.fecha}")
                    print("-" * 20)
                    # Aquí mostramos los productos de cada factura
                    for prod in fac.productos:
                        print(f" * {prod.nombre}: ${prod.precio if hasattr(prod, 'precio') else prod.valor}")
                    print(f"TOTAL: ${fac.valor_total}")
        else:
            print("ERROR: Cliente no encontrado.")