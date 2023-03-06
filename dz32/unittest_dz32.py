import unittest
import dz32

class Test_dz32(unittest.TestCase):

    def test_text_screen(self):
        text = 'text.txt'
        self.testfile = open(text, encoding='utf-8', mode = 'r')
        self.text = self.testfile.read()
        self.testfile.close()
        
    def test_two_num(self):
        self.assertNotEqual(dz32.two_num(24, 24), 'Неверный тип данных')

    def test_square(self):
        self.assertEqual(dz32.square(6, '*', False), None)
    
    def  test_min_num(self):
        self.assertNotEqual(dz32.min_num(2, -22, 6, 99, 0), 0)

    def test_mult(self):
        self.assertEqual(dz32.mult(2, 6), 720)

    def test_len_num(self):
        self.assertEqual(dz32.len_num(35648), 'Длина числа: 5')

    def test_Palindrome(self):
        self.assertEqual(dz32.Palindrome(121), 'Число палиндром')
 

if __name__ == '__main__':
    unittest.main()