def count_word_occurrences(text):
    words = text.split()
    
    word_count = {}
    
    result = []
    
    for word in words:
        word_lower = word.lower()
        
        if word_lower in word_count:
            result.append(word_count[word_lower])
            word_count[word_lower] += 1 
        else:
            result.append(0)  
            word_count[word_lower] = 1  
    
    return result

text = input("Введите текст: ")
occurrences = count_word_occurrences(text)
print("Количество вхождений слов:", occurrences)
