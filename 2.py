"""
В сутках 86400 секунд (24*60*60). Напишите программу, которая по введенному целому числу
в диапазоне от 1 до 86400, выводит текущее время в часах, минутах и секундах.
"""

time_in_sec = int(input())

hour = time_in_sec // (60 * 60)

minute = (time_in_sec // (60)) - (hour * 60)

second = time_in_sec - (hour * 60 * 60 + (minute * 60))

print(hour, minute, second)
