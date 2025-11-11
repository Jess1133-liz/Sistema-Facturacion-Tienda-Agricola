"""
Módulo que define la clase base abstracta Producto
"""
from abc import ABC, abstractmethod

class Producto(ABC):
    """Clase abstracta base para todos los productos"""
    
    def __init__(self, nombre: str, precio: float):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre del producto es obligatorio y debe ser string")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        
        self._nombre = nombre
        self._precio = precio
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    def obtener_precio(self) -> float:
        """Retorna el precio del producto"""
        return self._precio
    
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre='{self._nombre}', precio={self._precio})"
