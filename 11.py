"""
Напишите программу, которая по заданным сторонам
треугольника a, b, c вычисляет значения углов треугольника в градусах.
"""
import math

a = float(input("a:\n"))
b = float(input("b:\n"))
c = float(input("c:\n"))

# Вычисляем угол A (между b c) по формуле косинуса
# Сначала находим косинус угла затем обратное значение, и в конце переводим значение из радиан в градусы
A = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
B = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
C = 180 - A - B

print(A, B, C)
