import string

def longest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().translate(str.maketrans('', '', string.punctuation)).split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_words('max/text12lesson.txt'))
