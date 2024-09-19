n = int(input("Введите число n: "))

array = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:  #Проверяем, находится ли элемент на диагонали
            array[i][j] = 1
        elif i + j < n - 1:  #Элементы выше диагонали
            array[i][j] = 0
        else:  #Элементы ниже диагонали
            array[i][j] = 2

for row in array:
    print(" ".join(map(str, row)))
