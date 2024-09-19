n = int(input("Введите максимальное число n: "))

possible_numbers = set(range(1, n + 1))

while True:
        try:
            line = input() 
            if not line.strip():  
                break
            parts = line.split()  
            question = list(map(int, parts[:-1])) 
            answer = parts[-1]  
    
            if answer == "YES":
              
                possible_numbers.intersection_update(question)
            elif answer == "NO":
             
                possible_numbers.difference_update(question)
        except EOFError:
            break

result = sorted(possible_numbers)
print(" ".join(map(str, result)))
