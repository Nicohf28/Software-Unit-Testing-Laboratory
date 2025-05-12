import math

# Pruebas de Ejemplo.
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# Pruebas desarrolladas durante el Laboratorio.

def seno(x):
    return math.sin(x)

def coseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def arco_seno(x):
    if x < -1 or x > 1:
        raise ValueError("El valor debe estar entre -1 y 1")
    return math.asin(x)

def arco_coseno(x):
    if x < -1 or x > 1:
        raise ValueError("El valor debe estar entre -1 y 1")
    return math.acos(x)

def arco_tangente(x):
    return math.atan(x)

def potencia(base, exponente):
    return math.pow(base, exponente)

def logaritmo_base_10(x):
    if x <= 0:
        raise ValueError("El valor debe ser mayor que cero")
    return math.log10(x)

def logaritmo_natural(x):
    if x <= 0:
        raise ValueError("El valor debe ser mayor que cero")
    return math.log(x)

def raiz_cuadrada(x):
    if x < 0:
        raise ValueError("El valor no puede ser negativo")
    return math.sqrt(x)

def raiz_enesima(x, n):
    if n == 0:
        raise ValueError("La raíz enésima no puede tener exponente 0")
    if x < 0 and n % 2 == 0:
        raise ValueError("No se puede calcular la raíz par de un número negativo")
    return x ** (1 / n)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo")
    return math.factorial(n)

def inverso(x):
    if x == 0:
        raise ValueError("No se puede dividir entre cero")
    return 1 / x

def valor_pi():
    return math.pi

def seno_hiperbolico(x):
    return math.sinh(x)

def coseno_hiperbolico(x):
    return math.cosh(x)

def tangente_hiperbolica(x):
    return math.tanh(x)

def combinacion(n, r):
    if not all(isinstance(i, int) and i >= 0 for i in (n, r)):
        raise ValueError("n y r deben ser enteros no negativos")
    if r > n:
        raise ValueError("r no puede ser mayor que n")
    return math.comb(n, r)
