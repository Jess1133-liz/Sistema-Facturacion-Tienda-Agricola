"""
Pruebas unitarias para las clases del modelo
"""
import unittest
from model.cliente import Cliente
from model.factura import Factura
from model.control_plagas import ControlPlagas
from model.fertilizante import Fertilizante
from model.antibiotico import Antibiotico

class TestClases(unittest.TestCase):
    """Pruebas para validar la creación de clases"""
    
    def test_crear_cliente(self):
        """Verifica la creación de un cliente"""
        cliente = Cliente("Juan Pérez", "1234567890")
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.cedula, "1234567890")
        self.assertEqual(len(cliente.obtener_facturas()), 0)
    
    def test_crear_cliente_sin_nombre(self):
        """Verifica que no se pueda crear cliente sin nombre"""
        with self.assertRaises(ValueError):
            Cliente("", "1234567890")
    
    def test_crear_control_plagas(self):
        """Verifica la creación de un producto de control de plagas"""
        producto = ControlPlagas("Insecticida X", 50000, "ICA-12345", 15, 7)
        self.assertEqual(producto.nombre, "Insecticida X")
        self.assertEqual(producto.precio, 50000)
        self.assertEqual(producto.periodo_carencia, 7)
    
    def test_crear_fertilizante(self):
        """Verifica la creación de un fertilizante"""
        producto = Fertilizante("Fertilizante Y", 80000, "ICA-67890", 30, "2024-01-15")
        self.assertEqual(producto.nombre, "Fertilizante Y")
        self.assertEqual(producto.fecha_ultima_aplicacion, "2024-01-15")
    
    def test_crear_antibiotico(self):
        """Verifica la creación de un antibiótico"""
        producto = Antibiotico("Antibiótico Z", 120000, 500, "Bovinos")
        self.assertEqual(producto.nombre, "Antibiótico Z")
        self.assertEqual(producto.dosis, 500)
        self.assertEqual(producto.tipo_animal, "Bovinos")
    
    def test_antibiotico_dosis_invalida(self):
        """Verifica validación de dosis del antibiótico"""
        with self.assertRaises(ValueError):
            Antibiotico("Antibiótico Z", 120000, 700, "Bovinos")
    
    def test_antibiotico_tipo_animal_invalido(self):
        """Verifica validación del tipo de animal"""
        with self.assertRaises(ValueError):
            Antibiotico("Antibiótico Z", 120000, 500, "Perros")


class TestAsociaciones(unittest.TestCase):
    """Pruebas para validar las asociaciones entre clases"""
    
    def test_cliente_con_facturas(self):
        """Verifica la asociación Cliente-Factura (1 a muchos)"""
        cliente = Cliente("María González", "9876543210")
        factura1 = Factura("2024-11-01", cliente)
        factura2 = Factura("2024-11-10", cliente)
        
        cliente.agregar_factura(factura1)
        cliente.agregar_factura(factura2)
        
        self.assertEqual(len(cliente.obtener_facturas()), 2)
        self.assertEqual(factura1.cliente, cliente)
        self.assertEqual(factura2.cliente, cliente)
    
    def test_factura_con_productos(self):
        """Verifica la asociación Factura-Producto (1 a muchos)"""
        cliente = Cliente("Pedro López", "5555555555")
        factura = Factura("2024-11-10", cliente)
        
        prod1 = ControlPlagas("Insecticida A", 40000, "ICA-111", 15, 5)
        prod2 = Fertilizante("Fertilizante B", 60000, "ICA-222", 30, "2024-10-01")
        prod3 = Antibiotico("Antibiótico C", 100000, 450, "Porcinos")
        
        factura.agregar_producto(prod1)
        factura.agregar_producto(prod2)
        factura.agregar_producto(prod3)
        
        self.assertEqual(len(factura.obtener_productos()), 3)
        self.assertEqual(factura.valor_total, 200000)
    
    def test_composicion_cliente_factura(self):
        """Verifica la composición entre Cliente y Factura"""
        cliente = Cliente("Ana Rodríguez", "1111111111")
        factura = Factura("2024-11-05", cliente)
        cliente.agregar_factura(factura)
        
        # Verificar que la factura pertenece al cliente
        self.assertIn(factura, cliente.obtener_facturas())
        self.assertIs(factura.cliente, cliente)


class TestHerencia(unittest.TestCase):
    """Pruebas para validar la herencia entre clases"""
    
    def test_herencia_producto_control(self):
        """Verifica que ProductoControl hereda de Producto"""
        from model.producto import Producto
        from model.producto_control import ProductoControl
        
        fertilizante = Fertilizante("Fertilizante X", 70000, "ICA-333", 20, "2024-09-15")
        
        self.assertIsInstance(fertilizante, Producto)
        self.assertIsInstance(fertilizante, ProductoControl)
        self.assertIsInstance(fertilizante, Fertilizante)
    
    def test_herencia_control_plagas(self):
        """Verifica que ControlPlagas hereda de ProductoControl y Producto"""
        from model.producto import Producto
        from model.producto_control import ProductoControl
        
        control = ControlPlagas("Herbicida Y", 55000, "ICA-444", 10, 14)
        
        self.assertIsInstance(control, Producto)
        self.assertIsInstance(control, ProductoControl)
        self.assertIsInstance(control, ControlPlagas)
    
    def test_herencia_antibiotico(self):
        """Verifica que Antibiotico hereda de Producto"""
        from model.producto import Producto
        
        antibiotico = Antibiotico("Penicilina", 90000, 480, "Caprinos")
        
        self.assertIsInstance(antibiotico, Producto)
        self.assertIsInstance(antibiotico, Antibiotico)
    
    def test_metodos_heredados(self):
        """Verifica que los métodos se heredan correctamente"""
        control = ControlPlagas("Fungicida Z", 65000, "ICA-555", 12, 10)
        
        # Método heredado de Producto
        self.assertEqual(control.obtener_precio(), 65000)
        self.assertEqual(control.precio, 65000)
        self.assertEqual(control.nombre, "Fungicida Z")
