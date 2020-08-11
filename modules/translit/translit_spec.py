from index import fucker
import unittest


class TestTranslit(unittest.TestCase):

    def test1(self):
        """shoult translit library work"""
        self.assertTrue(fucker('абвгдеёжзийклмнопрстуфхцчшщьъыэюя').translit().value == 'abvgdeyozhzijklmnoprsyufhtschshsch\'\"yeyuya')

    def test2(self):
        """should translit get correct case of word"""
        self.assertTrue(fucker('Аб').translit().value == 'Ab')

    def test3(self):
        """should translit work with symbols"""
        self.assertTrue(fucker('Аб -').translit().value == 'Ab -')


if __name__ == '__main__':
    unittest.main()
