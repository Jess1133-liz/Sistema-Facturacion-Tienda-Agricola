"""
Módulo que define la clase Cliente
"""
from typing import List

class Cliente:
    """Clase que representa un cliente de la tienda"""
    
    def __init__(self, nombre: str, cedula: str):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre es obligatorio y debe ser string")
        if not cedula or not isinstance(cedula, str):
            raise ValueError("La cédula es obligatoria y debe ser string")
        
        self._nombre = nombre
        self._cedula = cedula
        self._facturas: List = []
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def cedula(self):
        return self._cedula
    
    def agregar_factura(self, factura):
        """Agrega una factura al historial del cliente"""
        from model.factura import Factura
        if not isinstance(factura, Factura):
            raise ValueError("Debe proporcionar un objeto Factura válido")
        
        self._facturas.append(factura)
    
    def obtener_facturas(self) -> List:
        """Retorna la lista de facturas del cliente"""
        return self._facturas.copy()
    
    def __repr__(self):
        return f"Cliente(nombre='{self._nombre}', cedula='{self._cedula}', facturas={len(self._facturas)})"
