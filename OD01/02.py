# попробуем прописать алгоритм для нахождения факториала.
# Для начала пропишем, чем равен факториал 5:
# #5! = 1 * 2 * 3 * 4 * 5 = 120
# сравнение числа с 0. Если = 0, то 0! = 1
# создание переменной для хранения итогов

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(5))

