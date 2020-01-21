import inflect


def num_to_word(number):
    p = inflect.engine()
    return p.number_to_words(number)
