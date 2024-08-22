mas = [5, 7, 4, 3, 8, 2]
n = len(mas)

for j in range(n-1):
    for i in range(n - 1 - j):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]


print(mas)
