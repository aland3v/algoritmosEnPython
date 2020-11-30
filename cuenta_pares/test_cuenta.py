import unittest
from cuenta import pares_rango

class CuentaTestCase(unittest.TestCase):
    """Test for cuenta module"""

    def test_cuenta_pares(self):
        """ contar los numeros en un intervalor funciona? """

        n_pares = pares_rango(6,11)
        self.assertEqual(n_pares, 3)

        n_pares = pares_rango(6,12)
        self.assertEqual(n_pares, 4)
        
unittest.main()