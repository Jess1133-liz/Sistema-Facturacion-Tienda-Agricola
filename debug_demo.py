"""
Script de demostración para debug - Composición y Herencia
"""

from model.cliente import Cliente
from model.factura import Factura
from model.control_plagas import ControlPlagas
from model.fertilizante import Fertilizante
from model.antibiotico import Antibiotico
from model.producto import Producto
from model.producto_control import ProductoControl

def separador(titulo):
    """Imprime un separador visual"""
    print("\n" + "="*70)
    print(f" {titulo}")
    print("="*70)

# ============================================================================
# COMPOSICIÓN: CLIENTE → FACTURAS
# ============================================================================
separador("COMPOSICIÓN: CLIENTE → FACTURAS")

cliente = Cliente("Juan Pérez", "1234567890")
factura1 = Factura("2024-11-01", cliente)
factura2 = Factura("2024-11-10", cliente)

cliente.agregar_factura(factura1)
cliente.agregar_factura(factura2)

print(f"Cliente creado: {cliente.nombre}")
print(f"Total de facturas asociadas: {len(cliente.obtener_facturas())}")

import pdb; pdb.set_trace()

# ============================================================================
# COMPOSICIÓN: FACTURA → PRODUCTOS
# ============================================================================
separador("COMPOSICIÓN: FACTURA → PRODUCTOS")

prod1 = ControlPlagas("Insecticida Potente", 50000, "ICA-12345", 15, 7)
prod2 = Fertilizante("Fertilizante Premium", 80000, "ICA-67890", 30, "2024-01-15")
prod3 = Antibiotico("Penicilina Bovina", 120000, 500, "Bovinos")

factura1.agregar_producto(prod1)
factura1.agregar_producto(prod2)
factura1.agregar_producto(prod3)

print(f"Productos agregados a factura: {len(factura1.obtener_productos())}")
print(f"Valor total de la factura: ${factura1.valor_total:,.2f}")

import pdb; pdb.set_trace()

# ============================================================================
# HERENCIA: CONTROL DE PLAGAS
# ============================================================================
separador("HERENCIA: CONTROL DE PLAGAS")

control = ControlPlagas("Herbicida Total", 65000, "ICA-99999", 12, 14)
print(f"Clase: {type(control).__name__}")
print(f"¿Es un Producto? {isinstance(control, Producto)}")
print(f"¿Es un ProductoControl? {isinstance(control, ProductoControl)}")
print(f"¿Es un ControlPlagas? {isinstance(control, ControlPlagas)}")

import pdb; pdb.set_trace()

# ============================================================================
# HERENCIA: FERTILIZANTE
# ============================================================================
separador("HERENCIA: FERTILIZANTE")

fertilizante = Fertilizante("Abono Orgánico", 45000, "ICA-88888", 20, "2024-10-01")
print(f"Clase: {type(fertilizante).__name__}")
print(f"¿Es un Producto? {isinstance(fertilizante, Producto)}")
print(f"¿Es un ProductoControl? {isinstance(fertilizante, ProductoControl)}")
print(f"¿Es un Fertilizante? {isinstance(fertilizante, Fertilizante)}")

import pdb; pdb.set_trace()

# ============================================================================
# HERENCIA: ANTIBIÓTICO
# ============================================================================
separador("HERENCIA: ANTIBIÓTICO")

antibiotico = Antibiotico("Amoxicilina", 95000, 450, "Porcinos")
print(f"Clase: {type(antibiotico).__name__}")
print(f"¿Es un Producto? {isinstance(antibiotico, Producto)}")
print(f"¿Es un Antibiotico? {isinstance(antibiotico, Antibiotico)}")

import pdb; pdb.set_trace()

# ============================================================================
# MÉTODOS HEREDADOS
# ============================================================================
separador("MÉTODOS HEREDADOS")

print(f"Control de Plagas - Precio: ${control.obtener_precio():,.2f}")
print(f"Fertilizante - Precio: ${fertilizante.obtener_precio():,.2f}")
print(f"Antibiótico - Precio: ${antibiotico.obtener_precio():,.2f}")

import pdb; pdb.set_trace()

# ============================================================================
# RESUMEN COMPLETO DEL SISTEMA
# ============================================================================
separador("RESUMEN DEL SISTEMA")

print(f"\nCliente: {cliente.nombre} (Cédula: {cliente.cedula})")
print(f"Total de facturas: {len(cliente.obtener_facturas())}")

for i, factura in enumerate(cliente.obtener_facturas(), 1):
    print(f"\nFactura #{i} - Fecha: {factura.fecha}")
    print(f"  Total: ${factura.valor_total:,.2f}")
    print(f"  Productos ({len(factura.obtener_productos())}):")
    
    for j, prod in enumerate(factura.obtener_productos(), 1):
        tipo = type(prod).__name__
        print(f"    {j}. [{tipo}] {prod.nombre} - ${prod.precio:,.2f}")

separador("FIN DEL DEMO")
print("\n✓ Demostración completada exitosamente\n")