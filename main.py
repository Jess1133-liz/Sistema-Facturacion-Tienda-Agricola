"""
Punto de entrada principal del sistema
"""
from ui.interfaz_usuario import InterfazUsuario
import unittest

def ejecutar_pruebas():
    """Ejecuta todas las pruebas unitarias"""
    print("\n" + "="*60)
    print("EJECUTANDO PRUEBAS UNITARIAS")
    print("="*60 + "\n")
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    from test.test_clases import TestClases, TestAsociaciones, TestHerencia
    suite.addTests(loader.loadTestsFromTestCase(TestClases))
    suite.addTests(loader.loadTestsFromTestCase(TestAsociaciones))
    suite.addTests(loader.loadTestsFromTestCase(TestHerencia))
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    return resultado.wasSuccessful()

def main():
    """Función principal"""
    print("Bienvenido al Sistema de Facturación - Tienda Agrícola")
    print("\n¿Desea ejecutar las pruebas unitarias primero? (s/n): ", end="")
    
    # Para demo automática, ejecutar pruebas
    ejecutar_pruebas()
    
    print("\n\nIniciando sistema...")
    interfaz = InterfazUsuario()
    interfaz.ejecutar()

if __name__ == "__main__":
    main()