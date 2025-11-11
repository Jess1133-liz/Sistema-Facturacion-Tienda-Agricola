"""
Módulo que maneja las operaciones CRUD del sistema
"""
from typing import Dict, List, Optional
from model.cliente import Cliente
from model.factura import Factura
from model.producto import Producto

class CRUDOperations:
    """Clase que maneja las operaciones de creación, lectura, actualización y eliminación"""
    
    def __init__(self):
        self._clientes: Dict[str, Cliente] = {}
    
    def crear_cliente(self, nombre: str, cedula: str) -> Cliente:
        """Crea y registra un nuevo cliente"""
        if cedula in self._clientes:
            raise ValueError(f"Ya existe un cliente con cédula {cedula}")
        
        cliente = Cliente(nombre, cedula)
        self._clientes[cedula] = cliente
        return cliente
    
    def obtener_cliente(self, cedula: str) -> Optional[Cliente]:
        """Obtiene un cliente por su cédula"""
        return self._clientes.get(cedula)
    
    def crear_factura(self, fecha: str, cedula_cliente: str) -> Factura:
        """Crea una nueva factura para un cliente"""
        cliente = self.obtener_cliente(cedula_cliente)
        if not cliente:
            raise ValueError(f"No existe cliente con cédula {cedula_cliente}")
        
        factura = Factura(fecha, cliente)
        cliente.agregar_factura(factura)
        return factura
    
    def agregar_producto_a_factura(self, factura: Factura, producto: Producto):
        """Agrega un producto a una factura"""
        factura.agregar_producto(producto)
    
    def buscar_por_cedula(self, cedula: str) -> Optional[Dict]:
        """Busca un cliente y retorna su información completa incluyendo facturas y productos"""
        cliente = self.obtener_cliente(cedula)
        if not cliente:
            return None
        
        facturas_info = []
        for factura in cliente.obtener_facturas():
            productos_info = [
                {
                    'tipo': type(p).__name__,
                    'nombre': p.nombre,
                    'precio': p.precio,
                    'detalles': str(p)
                }
                for p in factura.obtener_productos()
            ]
            
            facturas_info.append({
                'fecha': factura.fecha,
                'valor_total': factura.valor_total,
                'num_productos': len(factura.obtener_productos()),
                'productos': productos_info
            })
        
        return {
            'cliente': {
                'nombre': cliente.nombre,
                'cedula': cliente.cedula
            },
            'total_facturas': len(facturas_info),
            'facturas': facturas_info
        }
    
    def listar_clientes(self) -> List[Cliente]:
        """Retorna la lista de todos los clientes"""
        return list(self._clientes.values())