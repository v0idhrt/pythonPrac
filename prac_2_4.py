numbers = list(map(int, input("Введите числа через пробел: ").split()))

seen = set()

for number in numbers:
    if number in seen:
        print("YES")
    else:
        print("NO")
        seen.add(number)
