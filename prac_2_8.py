n = int(input("Введите максимальное число n: "))

possible_numbers = set(range(1, n + 1))

while True:
    line = input()  
    if line.strip() == "HELP":  
        break
    
    question = list(map(int, line.split())) 
    question_size = len(question)
    possible_count = len(possible_numbers)

    if question_size == possible_count // 2:
        print("NO")
    else:
        if any(num in possible_numbers for num in question):
            print("YES")
            possible_numbers.intersection_update(question) #оставляем элементы, которые также присутствуют в множестве question
        else:
            print("NO")
            possible_numbers.difference_update(question) #удаляет элементы, которые присутствуют в множестве question

result = sorted(possible_numbers)
print(" ".join(map(str, result)))
