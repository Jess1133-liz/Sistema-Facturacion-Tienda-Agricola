"""
Módulo que define la clase abstracta ProductoControl
"""
from model.producto import Producto

class ProductoControl(Producto):
    """Clase abstracta para productos de control (Fertilizantes y Control de Plagas)"""
    
    def __init__(self, nombre: str, precio: float, registro_ica: str, frecuencia_aplicacion: int):
        super().__init__(nombre, precio)
        
        if not registro_ica or not isinstance(registro_ica, str):
            raise ValueError("El registro ICA es obligatorio y debe ser string")
        if frecuencia_aplicacion <= 0:
            raise ValueError("La frecuencia de aplicación debe ser mayor a 0")
        
        self._registro_ica = registro_ica
        self._frecuencia_aplicacion = frecuencia_aplicacion
    
    @property
    def registro_ica(self):
        return self._registro_ica
    
    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion
    
    def __repr__(self):
        return (f"{self.__class__.__name__}(nombre='{self._nombre}', precio={self._precio}, "
                f"registro_ica='{self._registro_ica}', frecuencia={self._frecuencia_aplicacion})")
