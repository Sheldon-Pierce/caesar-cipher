import nltk
from nltk.corpus import words, names


def encrypt(phrase, shift):
    encrypted = ""
    for char in phrase:
        if char.isalpha():
            code = ord(char)
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            code = (code - base + shift) % 26 + base
            char = chr(code)
        encrypted += char
    return encrypted


def decrypt(phrase, shift):
    return encrypt(phrase, -shift)


nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

word_list = words.words()
namelist = names.words()


def crack(encrypted_phrase):
    def score_phrase(phrase):
        # Count the number of valid English words in the phrase
        valid_words = [word for word in phrase.split() if word.lower() in word_list]
        print(valid_words)
        num_valid_words = len(valid_words)

        # Calculate the percentage of words in the phrase that are valid English words
        total_words = len(phrase.split())
        if total_words == 0:
            return 0
        else:
            return num_valid_words / total_words

    # Try all possible shift values and keep track of the one with the highest score
    best_shift = 0
    best_score = 0
    for shift in range(26):
        decrypted_phrase = decrypt(encrypted_phrase, shift)
        score = score_phrase(decrypted_phrase)
        if score > best_score:
            best_score = score
            best_shift = shift

    print(decrypt(encrypted_phrase, best_shift))
    # Return the decrypted phrase and the shift value used to encrypt it
    for word in decrypt(encrypted_phrase, best_shift):
        if word in word_list:
            print(word)
        count = 0
        if word not in word_list:
            return ''
        else:
            count += 1
            if count == 0 and word not in word_list:
                return ''
            return decrypt(encrypted_phrase, best_shift)

    return decrypt(encrypted_phrase, best_shift)
