import unittest
import math
from calculadora import (
    sumar, restar, dividir, seno, coseno, tangente,
    arco_seno, arco_coseno, arco_tangente, potencia,
    logaritmo_base_10, logaritmo_natural, raiz_cuadrada,
    raiz_enesima, factorial, inverso, valor_pi,
    seno_hiperbolico, coseno_hiperbolico, tangente_hiperbolica,
    combinacion
)

class TestCalculadora(unittest.TestCase):

    '''
    def test_sumar(self):
        self.assertEqual(sumar(1, 4), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            dividir(5, 0)
    '''

    def test_seno(self):
        self.assertAlmostEqual(seno(math.pi / 2), 1)

    def test_coseno(self):
        self.assertAlmostEqual(coseno(0), 1)

    def test_tangente(self):
        self.assertAlmostEqual(tangente(0), 0)

    def test_arco_seno(self):
        self.assertAlmostEqual(arco_seno(1), math.pi / 2)
        with self.assertRaises(ValueError):
            arco_seno(2)

    def test_arco_coseno(self):
        self.assertAlmostEqual(arco_coseno(1), 0)
        with self.assertRaises(ValueError):
            arco_coseno(-2)

    def test_arco_tangente(self):
        self.assertAlmostEqual(arco_tangente(1), math.atan(1))

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_logaritmo_base_10(self):
        self.assertEqual(logaritmo_base_10(100), 2)
        with self.assertRaises(ValueError):
            logaritmo_base_10(0)

    def test_logaritmo_natural(self):
        self.assertEqual(logaritmo_natural(math.e), 1)
        with self.assertRaises(ValueError):
            logaritmo_natural(-1)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(9), 3)
        with self.assertRaises(ValueError):
            raiz_cuadrada(-4)

    def test_raiz_enesima(self):
        self.assertEqual(raiz_enesima(8, 3), 2)
        with self.assertRaises(ValueError):
            raiz_enesima(-8, 2)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_inverso(self):
        self.assertEqual(inverso(2), 0.5)
        with self.assertRaises(ValueError):
            inverso(0)

    def test_valor_pi(self):
        self.assertEqual(valor_pi(), math.pi)

    def test_seno_hiperbolico(self):
        self.assertAlmostEqual(seno_hiperbolico(0), 0)

    def test_coseno_hiperbolico(self):
        self.assertAlmostEqual(coseno_hiperbolico(0), 1)

    def test_tangente_hiperbolica(self):
        self.assertAlmostEqual(tangente_hiperbolica(0), 0)

    def test_combinacion(self):
        self.assertEqual(combinacion(5, 2), 10)
        with self.assertRaises(ValueError):
            combinacion(-1, 2)
        with self.assertRaises(ValueError):
            combinacion(3, 5)

if __name__ == '__main__':
    unittest.main()
