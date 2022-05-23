# Реализовать класс для работы с обыкновенными дробями.
# Класс поддерживать все арифметические и логические операции.
import math


class Fract:
    numerator_1: int
    denominator_1: int

    def __init__(self, numerator, denominator):  # иницилизация
        self.numerator_1 = numerator
        self.denominator_1 = denominator

    def __str__(self):  # проверка и вывод дроби
        if self.denominator_1 == 0:
            return f'Неверное число'
        if self.numerator_1 == self.denominator_1:
            return '1'
        return f'{self.numerator_1}/{self.denominator_1}'

    def __add__(self, other):  # cложение
        numerator_2 = self.numerator_1 * other.denominator_1 + other.numerator_1 * self.denominator_1
        denominator_2 = self.denominator_1 * other.denominator_1
        gcd = math.gcd(numerator_2, denominator_2)  # НОД
        return Fract(numerator_2 // gcd, denominator_2 // gcd)

    def __sub__(self, other):  # вычитание
        numerator_2 = self.numerator_1 * other.denominator_1 - other.numerator_1 * self.denominator_1
        denominator_2 = self.denominator_1 * other.denominator_1
        gcd = math.gcd(numerator_2, denominator_2)
        return Fract(numerator_2 // gcd, denominator_2 // gcd)

    def __mul__(self, other):  # умножение
        numerator_2 = self.numerator_1 * other.numerator_1
        denominator_2 = self.denominator_1 * other.denominator_1
        gcd = math.gcd(numerator_2, denominator_2)
        return Fract(numerator_2 // gcd, denominator_2 // gcd)

    def __truediv__(self, other):  # деление
        numerator_2 = self.numerator_1 * other.denominator_1
        denominator_2 = self.denominator_1 * other.numerator_1
        gcd = math.gcd(numerator_2, denominator_2)
        return Fract(numerator_2 // gcd, denominator_2 // gcd)

    # сравнение
    def __lt__(self, other):
        return self.numerator_1 * other.denominator_1 < other.numerator_1 * self.denominator_1

    def __eq__(self, other):
        return self.numerator_1 * other.denominator_1 == other.numerator_1 * self.denominator_1

    def __le__(self, other):
        return self.numerator_1 * other.denominator_1 <= other.numerator_1 * self.denominator_1


f = Fract(3, 4)
b = Fract(1, 5)

print(f + b)
print(f - b)
print(f * b)
print(f / b)
print(f > b)
print(f == b)
print(f <= b)
