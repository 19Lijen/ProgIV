import unittest
from modelo.cliente import Cliente
from crud.gestion_tienda import GestionTienda
from modelo.control_plagas import ControlPlagas
from modelo.antibiotico import Antibiotico
from modelo.factura import Factura

class TestTiendaAgricola(unittest.TestCase):

    def test_calculo_total_factura(self):

        factura = Factura("2026-05-04")
        p1 = ControlPlagas("ICA-123", "Fungicida", "15 dias", 50000, 7)
        a1 = Antibiotico("Amoxicilina", 500, "Bovino", 30000)
        

        factura.agregar_producto(p1)
        factura.agregar_producto(a1)
        

        self.assertEqual(factura.valor_total, 80000)

    def test_dosis_antibiotico_invalida(self):

        with self.assertRaises(ValueError):
            Antibiotico("Penicilina", 300, "Porcino", 20000)

if __name__ == '__main__':
    unittest.main()
    