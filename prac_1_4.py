n = int(input("Введите число n: "))

array = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        # Вычисляем расстояние от главной диагонали
        distance = abs(i - j)
        array[i][j] = distance

for row in array:
    print(" ".join(map(str, row)))
