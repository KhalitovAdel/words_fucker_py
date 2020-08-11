from index import fucker
import unittest


class TestCorrectLang(unittest.TestCase):

    def test1(self):
        """should ВОВА by russian words get BOBA in english words"""
        self.assertTrue(fucker('ВОВА').correct_lang().value == 'BOBA')

    def test2(self):
        """should BOBA by english words get ВОВА in russian words"""
        self.assertTrue(fucker('BOBA').correct_lang('ru').value == 'ВОВА')

    def test3(self):
        """should BOВА - BO by eng words and BA by russian words get BOBA in english words"""
        self.assertTrue(fucker('BOВА').correct_lang().value == 'BOBA')

    def test4(self):
        """should BoВА - Bo by eng words and Bа by russian words get BoBa in english words and save register"""
        self.assertTrue(fucker('BoВа').correct_lang().value == 'BoBa')


if __name__ == '__main__':
    unittest.main()
