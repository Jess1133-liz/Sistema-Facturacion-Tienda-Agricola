"""
Interfaz de usuario para el sistema
"""
from crud.crud_operations import CRUDOperations
from model.control_plagas import ControlPlagas
from model.fertilizante import Fertilizante
from model.antibiotico import Antibiotico

class InterfazUsuario:
    """Clase que maneja la interfaz de usuario"""
    
    def __init__(self):
        self.crud = CRUDOperations()
    
    def mostrar_menu(self):
        """Muestra el menú principal"""
        print("\n" + "="*50)
        print("SISTEMA DE FACTURACIÓN - TIENDA AGRÍCOLA")
        print("="*50)
        print("1. Registrar nuevo cliente")
        print("2. Crear factura")
        print("3. Buscar cliente por cédula")
        print("4. Listar todos los clientes")
        print("5. Salir")
        print("="*50)
    
    def registrar_cliente(self):
        """Registra un nuevo cliente"""
        print("\n--- REGISTRAR NUEVO CLIENTE ---")
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        
        try:
            cliente = self.crud.crear_cliente(nombre, cedula)
            print(f"✓ Cliente registrado exitosamente: {cliente}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    def crear_factura(self):
        """Crea una nueva factura con productos"""
        print("\n--- CREAR FACTURA ---")
        cedula = input("Cédula del cliente: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        
        try:
            factura = self.crud.crear_factura(fecha, cedula)
            print(f"✓ Factura creada para cliente {factura.cliente.nombre}")
            
            while True:
                print("\nTipo de producto:")
                print("1. Control de Plagas")
                print("2. Fertilizante")
                print("3. Antibiótico")
                print("4. Finalizar factura")
                
                opcion = input("Seleccione opción: ")
                
                if opcion == "4":
                    break
                
                self._agregar_producto(factura, opcion)
            
            print(f"\n✓ Factura finalizada. Total: ${factura.valor_total:,.2f}")
            
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    def _agregar_producto(self, factura, tipo):
        """Agrega un producto a la factura según el tipo"""
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        
        try:
            if tipo == "1":
                registro_ica = input("Registro ICA: ")
                frecuencia = int(input("Frecuencia de aplicación (días): "))
                carencia = int(input("Periodo de carencia (días): "))
                producto = ControlPlagas(nombre, precio, registro_ica, frecuencia, carencia)
            
            elif tipo == "2":
                registro_ica = input("Registro ICA: ")
                frecuencia = int(input("Frecuencia de aplicación (días): "))
                fecha_aplicacion = input("Fecha última aplicación (YYYY-MM-DD): ")
                producto = Fertilizante(nombre, precio, registro_ica, frecuencia, fecha_aplicacion)
            
            elif tipo == "3":
                dosis = float(input("Dosis (Kg): "))
                print("Tipos de animal: Bovinos, Caprinos, Porcinos")
                tipo_animal = input("Tipo de animal: ")
                producto = Antibiotico(nombre, precio, dosis, tipo_animal)
            
            else:
                print("✗ Opción inválida")
                return
            
            self.crud.agregar_producto_a_factura(factura, producto)
            print(f"✓ Producto agregado: {producto}")
            
        except ValueError as e:
            print(f"✗ Error al agregar producto: {e}")
    
    def buscar_cliente(self):
        """Busca y muestra información de un cliente"""
        print("\n--- BUSCAR CLIENTE ---")
        cedula = input("Cédula: ")
        
        resultado = self.crud.buscar_por_cedula(cedula)
        
        if not resultado:
            print(f"✗ No se encontró cliente con cédula {cedula}")
            return
        
        print(f"\n{'='*60}")
        print(f"CLIENTE: {resultado['cliente']['nombre']}")
        print(f"CÉDULA: {resultado['cliente']['cedula']}")
        print(f"TOTAL FACTURAS: {resultado['total_facturas']}")
        print(f"{'='*60}")
        
        for i, factura in enumerate(resultado['facturas'], 1):
            print(f"\nFACTURA #{i}")
            print(f"  Fecha: {factura['fecha']}")
            print(f"  Total: ${factura['valor_total']:,.2f}")
            print(f"  Productos ({factura['num_productos']}):")
            
            for j, prod in enumerate(factura['productos'], 1):
                print(f"    {j}. [{prod['tipo']}] {prod['nombre']} - ${prod['precio']:,.2f}")
    
    def listar_clientes(self):
        """Lista todos los clientes registrados"""
        clientes = self.crud.listar_clientes()
        
        if not clientes:
            print("\n✗ No hay clientes registrados")
            return
        
        print(f"\n{'='*60}")
        print(f"TOTAL CLIENTES: {len(clientes)}")
        print(f"{'='*60}")
        
        for cliente in clientes:
            print(f"• {cliente.nombre} - Cédula: {cliente.cedula} - Facturas: {len(cliente.obtener_facturas())}")
    
    def ejecutar(self):
        """Ejecuta el sistema"""
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.crear_factura()
            elif opcion == "3":
                self.buscar_cliente()
            elif opcion == "4":
                self.listar_clientes()
            elif opcion == "5":
                print("\n¡Hasta luego!")
                break
            else:
                print("\n✗ Opción inválida")