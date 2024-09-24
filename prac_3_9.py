def load_stress_dictionary(n, entries):
    stress_dict = {}

    for entry in entries:
        word = entry.lower()
        if word not in stress_dict:
            stress_dict[word] = []
        stress_dict[word].append(entry)  

    return stress_dict

def count_errors(stress_dict, text):
    errors = 0
    words = text.split()  

    for word in words:
        lower_word = word.lower()  
        stress_count = sum(1 for char in word if char.isupper())

        if lower_word in stress_dict:
            if stress_count == 0 or stress_count > 1:
                errors += 1  
            else:
                if word not in stress_dict[lower_word]:
                    errors += 1 
        else:
            if stress_count != 1:
                errors += 1

    return errors

if __name__ == "__main__":
    n = int(input("Введите количество слов в словаре: "))
    entries = []

    for _ in range(n):
        entries.append(input("Введите слово с ударением: "))

    text = input("Введите текст для проверки: ")

    stress_dict = load_stress_dictionary(n, entries)

    error_count = count_errors(stress_dict, text)

    print("\nКоличество ошибок:", error_count)
