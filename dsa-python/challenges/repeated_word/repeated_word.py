def words(sent):
    """
    Finds duplicate words in a sentence

    Args:
        sent (str): Sentence of words

    Returns:
        str: word that repeats
    """
    word_hold = []
    word_lst = sent.split()

    for w in range(len(word_lst)):
        print(word_lst)
        word_hold = word_lst[w]
        for j in range(w + 1, len(word_lst)):
            if word_hold == word_lst[j]:
                return word_hold
    return "does not have duplicate words"
