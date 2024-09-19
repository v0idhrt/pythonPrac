n, m = map(int, input("Введите два числа n и m: ").split())

array = [["." for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 1:  #Если сумма индексов - *
            array[i][j] = "*"

for row in array:
    print(" ".join(row))
