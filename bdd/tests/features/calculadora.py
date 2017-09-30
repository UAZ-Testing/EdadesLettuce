import math


class Calculadora(object):
    def __init__(self):
        self.resultado = 0

    def suma(self, num1, num2):
        self.resultado = num1 + num2

    def resta(self, num1, num2):
        self.resultado = num1 - num2

    def multiplica(self, num1, num2):
        self.resultado = num1 * num2

    def divide(self, num1, num2):
        self.resultado = num1 / float(num2)

    def raiz(self, num):
        self.resultado = math.sqrt(num)

    def potencia(self, base, potencia):
        self.resultado = base ** potencia

    def obtener_resultado(self):
        return self.resultado
