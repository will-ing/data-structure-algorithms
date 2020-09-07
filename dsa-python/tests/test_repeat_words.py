from challenges.repeated_word.repeated_word import words


def test_repeat():
    sentence = "Once upon a time, there was a brave princess who..."
    assert words(sentence) == 'a'
