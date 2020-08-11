from modules.translit.translit_library import translit_library


def translit_word(word: str):
    new_word = translit_library.get(word.lower(), word)
    return new_word if word.islower() else new_word.upper()
