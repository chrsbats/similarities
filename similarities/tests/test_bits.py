import unittest
from similarities.bits import *

class TestGray(unittest.TestCase):

    def test_gray_to_binary(self):
        assert gray_to_binary(15,4) == 10
        assert gray_to_binary(8,4) == 15
        assert gray_to_binary(13,4) == 9


    def test_binary_to_gray(self):
        assert binary_to_gray(10,4) == 15
        assert binary_to_gray(15,4) == 8
        assert binary_to_gray(9,4) == 13

    def test_ROL(self):
        assert bin_string(ROL(1,1)) == '10'
        assert bin_string(ROL(1,4)) == '10000'
        assert bin_string(ROL(1,32)) == '1'
        assert bin_string(ROL(1,33)) == '10'
        assert bin_string(ROL(1,5,5)) == '1'
        assert bin_string(ROL(1,6,5)) == '10'

        
    def test_ROR(self):
        assert bin_string(ROR(1,1,5)) == '10000'
        assert bin_string(ROR(1,4,5)) == '10'
        assert bin_string(ROR(1,32)) == '1'
        assert bin_string(ROR(1,6,5)) == '10000'

if __name__ == '__main__':
    unittest.main()
