def load_stress_dictionary(n, entries):
    stress_dict = {}
    for entry in entries:
        word, stressed_word = entry.split()
        stress_dict[word] = stressed_word
    return stress_dict

def check_stress(text, stress_dict):
    results = []
    words = text.split()  

    for word in words:
        if word in stress_dict:
            if word == stress_dict[word]:
                results.append("Correct")
            else:
                results.append("Incorrect")
        else:
            if word.count('`') == 1: 
                results.append("Correct")
            else:
                results.append("Incorrect")

    return results

if __name__ == "__main__":
    n = int(input("Введите количество слов в словаре: "))
    entries = []

    for _ in range(n):
        entries.append(input("Введите слово и его правильное ударение: "))

    text = input("Введите текст для проверки: ")

    stress_dict = load_stress_dictionary(n, entries)

    results = check_stress(text, stress_dict)

    print("\nРезультаты проверки:")
    for result in results:
        print(result)
