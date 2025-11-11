"""
Módulo que define la clase Fertilizante
"""
from model.producto_control import ProductoControl

class Fertilizante(ProductoControl):
    """Clase para productos fertilizantes"""
    
    def __init__(self, nombre: str, precio: float, registro_ica: str, 
                 frecuencia_aplicacion: int, fecha_ultima_aplicacion: str):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        
        if not fecha_ultima_aplicacion or not isinstance(fecha_ultima_aplicacion, str):
            raise ValueError("La fecha de última aplicación es obligatoria")
        
        self._fecha_ultima_aplicacion = fecha_ultima_aplicacion
    
    @property
    def fecha_ultima_aplicacion(self):
        return self._fecha_ultima_aplicacion
    
    def __repr__(self):
        return (f"Fertilizante(nombre='{self._nombre}', precio={self._precio}, "
                f"registro_ica='{self._registro_ica}', frecuencia={self._frecuencia_aplicacion}, "
                f"fecha_ultima_aplicacion='{self._fecha_ultima_aplicacion}')")
