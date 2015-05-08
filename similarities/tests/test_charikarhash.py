import unittest
from similarities import CharikarHash

class TestCharikarHash(unittest.TestCase):

    def test_charikarhash(self):
        pass
        
if __name__ == '__main__':
    unittest.main()

'''
import similarities 
x = similarities.CharikarHash("this is a similar sentence")
x.string_hash()
y = similarities.CharikarHash("this is another similar sentence")
y.string_hash()

x.distance(y)
y = similarities.CharikarHash("a completely different sentence unlike the others")
x.distance(y)
'''