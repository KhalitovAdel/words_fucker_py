from modules.correct_lang.correct_lang_library import correct_lang


def transform_word(word: str, lang='eu'):
    if lang == 'eu':
        new_word: str = correct_lang.get(word.lower(), word)
        return new_word if word.islower() else new_word.upper()
    else:
        if word.lower() in list(correct_lang.values()):
            new_word: str = list(correct_lang.keys())[list(correct_lang.values()).index(word.lower())]
            return new_word if word.islower() else new_word.upper()
        else:
            return word
