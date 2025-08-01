"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    result = ' :: '.join([prefix] + prefixed_words)
    return result




def remove_suffix_ness(word):
    """
    Remove the suffix from the word while keeping spelling in mind.

    :param word: str - word to remove suffix from.
    :return: str - word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    suffix = "ness"
    
    # Check if the word ends with the suffix
    if word.endswith(suffix):
        # Remove the suffix
        word_without_suffix = word[:-len(suffix)]
        
        # Adjust spelling if needed
        if word_without_suffix.endswith("i"):
            # Change "i" to "y" if the previous letter is a vowel
            if word_without_suffix[-1] in "aeiou":
                return word_without_suffix[:-1] + "y"
        
    return word_without_suffix


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()
    adjective = words[index]
    if adjective.endswith('.'):
        verb = adjective[:-1] + 'en'
    else:
        verb = adjective + 'en'
    return verb
