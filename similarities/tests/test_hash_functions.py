import unittest
import similarities

class TestLSHHashes(unittest.TestCase):

    def setUp(self):
        self.s1 = "this is a similar sentence"
        self.s2 = "this is another similar sentence"
        self.s3 = "a completely different sentence unlike the others"
        self.dist_tolerence = 0.0001
        self.sim_tolerence = 0.9999

    def hash_function(self,HashFunction):
        x = HashFunction(self.s1)
        y = HashFunction(self.s2)
        z = HashFunction(self.s3)
        assert x.distance(x) < self.dist_tolerence
        assert y.distance(y) < self.dist_tolerence
        assert z.distance(z) < self.dist_tolerence

        assert x.similarity(x) > self.sim_tolerence
        assert y.similarity(y) > self.sim_tolerence
        assert z.similarity(z) > self.sim_tolerence
                
        assert x.distance(y) < x.distance(z)
        assert y.distance(x) < y.distance(z)
        assert x.similarity(y) > x.similarity(z)
        assert y.similarity(x) > y.similarity(z)
        
    def test_hashes(self):
        self.hash_function(similarities.CharikarHash)
        self.hash_function(similarities.MinHash)
        self.hash_function(similarities.FeatureHash)

if __name__ == '__main__':
    unittest.main()


#Scripts for readme use
'''
import similarities 
x = similarities.CharikarHash("this is a similar sentence")
x.string_hash()
y = similarities.CharikarHash("this is another similar sentence")
y.string_hash()

x.distance(y)
y = similarities.CharikarHash("a completely different sentence unlike the others")
x.distance(y)

x.vector
'''

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

'''
import similarities 
x = similarities.FeatureHash("this is a similar sentence",100000)
x.hash
y = similarities.FeatureHash("this is another similar sentence",100000)
y.hash

x.distance(y)
y = similarities.FeatureHash("a completely different sentence unlike the others",100000)
x.distance(y)
'''