"""
Программа получает на вход стоимость биткоина в рублях.
Какая цифра находится на третьей позиции справа?
"""

btc_rub_price = str(input('BTC/RUB price\n'))

print(btc_rub_price[-3:-2])
