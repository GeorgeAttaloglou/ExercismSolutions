from string import ascii_lowercase

"return all(letter in sentence.lower() for letter in ascii_lowercase)"
def is_pangram(sentence):
    letters_of_sentence = []
    for letter in sentence.lower():
        if letter >= "a" and letter <= "z":
            letters_of_sentence.append(letter)
    return len(set(letters_of_sentence)) == 26