"""
Некоторое число K записали подряд без пробелов N раз.
Получившееся число умножили на R. Каков результат умножения?
Программа должна получать последовательность трех чисел К, N и R и выводит одно число - результат описанных выше действий.
Условный оператор и циклы не использовать.&nbsp;
"""

k, n, r = input().split(" ")
k, n, r = k, int(n), int(r)

answer = int(k * n) * r
print(answer)
