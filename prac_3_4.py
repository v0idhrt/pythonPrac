def find_most_frequent_word(num_lines, lines):
    word_count = {}

    for line in lines:
        words = line.split()
        for word in words:
            word_lower = word.lower()
            if word_lower in word_count:
                word_count[word_lower] += 1
            else:
                word_count[word_lower] = 1

    most_frequent_word = None
    max_count = 0

    for word, count in word_count.items():
        if count > max_count or (count == max_count and (most_frequent_word is None or word < most_frequent_word)):
            most_frequent_word = word
            max_count = count

    return most_frequent_word

if __name__ == "__main__":
    num_lines = int(input("Введите количество строк: "))
    lines = []

    for _ in range(num_lines):
        line = input("Введите строку: ")
        lines.append(line)

    result = find_most_frequent_word(num_lines, lines)
    print("Самое частое слово:", result)
