"""
Módulo que define la clase Factura
"""
from typing import List
from model.producto import Producto

class Factura:
    """Clase que representa una factura o pedido"""
    
    def __init__(self, fecha: str, cliente):
        if not fecha or not isinstance(fecha, str):
            raise ValueError("La fecha es obligatoria y debe ser string")
        if cliente is None:
            raise ValueError("El cliente es obligatorio")
        
        self._fecha = fecha
        self._cliente = cliente
        self._productos: List[Producto] = []
        self._valor_total = 0.0
    
    @property
    def fecha(self):
        return self._fecha
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def valor_total(self):
        return self._valor_total
    
    def agregar_producto(self, producto: Producto):
        """Agrega un producto a la factura y recalcula el total"""
        if not isinstance(producto, Producto):
            raise ValueError("Debe proporcionar un objeto Producto válido")
        
        self._productos.append(producto)
        self.calcular_total()
    
    def calcular_total(self) -> float:
        """Calcula el valor total de la factura"""
        self._valor_total = sum(p.obtener_precio() for p in self._productos)
        return self._valor_total
    
    def obtener_productos(self) -> List[Producto]:
        """Retorna la lista de productos de la factura"""
        return self._productos.copy()
    
    def __repr__(self):
        return (f"Factura(fecha='{self._fecha}', cliente={self._cliente.nombre}, "
                f"productos={len(self._productos)}, valor_total={self._valor_total})")
