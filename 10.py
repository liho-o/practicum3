"""
Если на вход ввести не число, а латинские символы, например "helloworld"
- то программа выведет сообщение об ошибке.

Подумайте и исправьте программу таким образом, чтобы сообщение об ошибке не выводилось.
"""

raw = input('Enter number:')
try:
    num = int(raw)
    print(num)
except:
    print(raw)