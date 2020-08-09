#!/usr/bin/env python

from modules.correct_lang.correct_lang_services import transform_word


class _Fucker(object):
    def __init__(self, value: str):
        self._fuck_me: str = value

    def correct_lang(self, lang='eu'):
        self._fuck_me = ''.join([transform_word(x, lang) for x in list(self._fuck_me)])
        return self

    def print(self):
        print(self._fuck_me)
        return self
