def count_and_sort_words(num_lines, lines):
    word_count = {}

    for line in lines:
        words = line.split()
        for word in words:
            word_lower = word.lower()
            if word_lower in word_count:
                word_count[word_lower] += 1
            else:
                word_count[word_lower] = 1

    sorted_words = [(count, word) for word, count in word_count.items()]

    sorted_words.sort(key=lambda x: (-x[0], x[1]))

    return sorted_words

if __name__ == "__main__":
    num_lines = int(input("Введите количество строк: "))
    lines = []

    for _ in range(num_lines):
        line = input("Введите строку: ")
        lines.append(line)

    sorted_word_list = count_and_sort_words(num_lines, lines)
    
    print("\nСлова по частоте встречаемости:")
    for count, word in sorted_word_list:
        print(word)
