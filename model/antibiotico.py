"""
Módulo que define la clase Antibiotico
"""
from model.producto import Producto

class Antibiotico(Producto):
    """Clase para productos antibióticos"""
    
    TIPOS_ANIMALES_VALIDOS = ['Bovinos', 'Caprinos', 'Porcinos']
    DOSIS_MIN = 400
    DOSIS_MAX = 600
    
    def __init__(self, nombre: str, precio: float, dosis: float, tipo_animal: str):
        super().__init__(nombre, precio)
        
        if not self.validar_dosis(dosis):
            raise ValueError(f"La dosis debe estar entre {self.DOSIS_MIN}Kg y {self.DOSIS_MAX}Kg")
        
        if tipo_animal not in self.TIPOS_ANIMALES_VALIDOS:
            raise ValueError(f"Tipo de animal debe ser uno de: {', '.join(self.TIPOS_ANIMALES_VALIDOS)}")
        
        self._dosis = dosis
        self._tipo_animal = tipo_animal
    
    @property
    def dosis(self):
        return self._dosis
    
    @property
    def tipo_animal(self):
        return self._tipo_animal
    
    @staticmethod
    def validar_dosis(dosis: float) -> bool:
        """Valida que la dosis esté en el rango permitido"""
        return Antibiotico.DOSIS_MIN <= dosis <= Antibiotico.DOSIS_MAX
    
    def __repr__(self):
        return (f"Antibiotico(nombre='{self._nombre}', precio={self._precio}, "
                f"dosis={self._dosis}, tipo_animal='{self._tipo_animal}')")
