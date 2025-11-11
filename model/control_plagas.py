"""
Módulo que define la clase ControlPlagas
"""
from model.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    """Clase para productos de control de plagas"""
    
    def __init__(self, nombre: str, precio: float, registro_ica: str, 
                 frecuencia_aplicacion: int, periodo_carencia: int):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        
        if periodo_carencia < 0:
            raise ValueError("El periodo de carencia no puede ser negativo")
        
        self._periodo_carencia = periodo_carencia
    
    @property
    def periodo_carencia(self):
        return self._periodo_carencia
    
    def __repr__(self):
        return (f"ControlPlagas(nombre='{self._nombre}', precio={self._precio}, "
                f"registro_ica='{self._registro_ica}', frecuencia={self._frecuencia_aplicacion}, "
                f"periodo_carencia={self._periodo_carencia})")
