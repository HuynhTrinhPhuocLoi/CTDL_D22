def word_count(file_path):
    word_freq = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

file_path = "P1_data.txt" 
print(word_count(file_path))
