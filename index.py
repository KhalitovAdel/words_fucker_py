#!/usr/bin/env python

from modules.correct_lang.correct_lang_services import transform_word
from modules.translit.translit_services import translit_word


def fucker(value: str):
    return _Fucker(value)


class _Fucker(object):
    def __init__(self, value: str):
        self._fuck_me: str = value

    def correct_lang(self, lang='eu'):
        self._fuck_me = ''.join([transform_word(x, lang) for x in list(self._fuck_me)])
        return self

    def translit(self):
        self._fuck_me = ''.join([translit_word(x) for x in list(self._fuck_me)])
        return self

    @property
    def value(self):
        print(self._fuck_me)
        return self._fuck_me
