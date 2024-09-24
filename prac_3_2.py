def find_synonym(synonym_pairs, target_word):
    synonym_dict = {}
    
    for word1, word2 in synonym_pairs:
        synonym_dict[word1] = word2
        synonym_dict[word2] = word1  
    
    return synonym_dict.get(target_word, "Синоним не найден")

if __name__ == "__main__":
    print("Введите пары синонимов (в формате 'слово1 слово2'):")
    synonym_pairs = []
    
    while True:
        line = input()
        if line.strip() == "":
            break
        pair = line.split()
        if len(pair) == 2:
            synonym_pairs.append(pair)
    
    target_word = input("Введите слово для поиска синонима: ")
    
    synonym = find_synonym(synonym_pairs, target_word)
    print("Синоним:", synonym)
