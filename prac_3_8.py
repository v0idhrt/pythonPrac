def build_english_latin_dictionary(entries):
    english_latin_dict = {}

    for entry in entries:
        english_word, latin_word = entry.split()
        english_latin_dict[english_word] = latin_word

    return english_latin_dict

def translate_words(dictionary, words_to_translate):
    results = []
    for word in words_to_translate:
        if word in dictionary:
            results.append(f"{word} -> {dictionary[word]}")
        else:
            results.append(f"{word} -> Not found")
    return results

if __name__ == "__main__":
    n = int(input("Введите количество записей в словаре: "))
    entries = []

    for _ in range(n):
        entries.append(input("Введите английское слово и его латинский перевод: "))

    m = int(input("Введите количество слов для перевода: "))
    words_to_translate = []

    for _ in range(m):
        words_to_translate.append(input("Введите слово для перевода: "))

    english_latin_dict = build_english_latin_dictionary(entries)

    results = translate_words(english_latin_dict, words_to_translate)

    print("\nРезультаты перевода:")
    for result in results:
        print(result)
