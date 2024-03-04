"""
Квотербек рейтинг игрока (passer rating) в американском футболе рассчитывается по формуле,
предложенной Национальной футбольной лигой (NFL).
Для расчета используются пять параметров:  ATT, COMP, YDS, TD, INT.
Напишите программу, которая на вход получает эти параметры и вычисляет рейтинг игрока (passer rating).
"""

att = int(input("ATT:\n"))
comp = int(input("COMP:\n"))
yds = int(input("YDS:\n"))
td = int(input("TD:\n"))
inter = int(input("INT:\n"))

a = ((comp / att) - 0.3) * 5
b = ((yds / att) - 3) * 0.25
c = (td / att) * 20
d = 2.375 - ((inter / att) * 25)

a = min(max(a, 0), 2.375)
b = min(max(b, 0), 2.375)
c = min(max(c, 0), 2.375)
d = min(max(d, 0), 2.375)

passer_rating = ((a + b + c + d) / 6) * 100
print(passer_rating)
