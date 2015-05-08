import unittest
from similarities import MinHash

class TestMinHash(unittest.TestCase):

    def test_minhash(self):
        pass
        
if __name__ == '__main__':
    unittest.main()

'''
import similarities 
x = similarities.MinHash("this is a similar sentence",8)
x.hash
y = similarities.MinHash("this is another similar sentence",8)
y.hash

x.distance(y)
y = similarities.MinHash("a completely different sentence unlike the others")
x.distance(y)
'''