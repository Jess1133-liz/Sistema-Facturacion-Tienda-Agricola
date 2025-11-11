"""Módulo de modelos de datos"""
from .producto import Producto
from .producto_control import ProductoControl
from .control_plagas import ControlPlagas
from .fertilizante import Fertilizante
from .antibiotico import Antibiotico
from .factura import Factura
from .cliente import Cliente

__all__ = [
    'Producto',
    'ProductoControl', 
    'ControlPlagas',
    'Fertilizante',
    'Antibiotico',
    'Factura',
    'Cliente'
]