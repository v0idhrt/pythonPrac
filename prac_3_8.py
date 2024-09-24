def create_latin_english_dictionary(n, entries):
    latin_english_dict = {}

    for entry in entries:
        english_word, latin_translations = entry.split(' - ')
        latin_words = latin_translations.split(', ')

        for latin_word in latin_words:
            if latin_word not in latin_english_dict:
                latin_english_dict[latin_word] = []
            latin_english_dict[latin_word].append(english_word)

    return latin_english_dict

if __name__ == "__main__":
    n = int(input("Введите количество английских слов в словаре: "))
    entries = []

    for _ in range(n):
        entries.append(input("Введите английское слово и его латинские переводы: "))

    latin_english_dict = create_latin_english_dictionary(n, entries)

    sorted_latin_words = sorted(latin_english_dict.keys())

    print("\nЛатинско-английский словарь:")
    for latin_word in sorted_latin_words:
        english_words = sorted(latin_english_dict[latin_word])
        print(f"{latin_word} - {', '.join(english_words)}")
