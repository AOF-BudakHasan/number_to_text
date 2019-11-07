import unittest
from number_to_text import NTT
from adapters import AdapterLangTr


class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        self.test_number = 2345.5265
        self.expected_text = "İKİBİNÜÇYÜZKIRKBEŞLİRAELLİÜÇKURUŞ"

    def tearDown(self):
        pass

    def test_lang_tr(self):
        new_ntt = NTT(adapter=AdapterLangTr, fraction_size=2)
        result_text = new_ntt.number_to_text(self.test_number)
        self.assertEqual(result_text, self.expected_text, 'Result should be as self.expected_text')


if __name__ == '__main__':
    unittest.main()
