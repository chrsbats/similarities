========
Similarities
========

Utilities for creating similarity metrics and comparisons.


Examples
========

Url-Safe Base64 64-bit hashes (non-cryptographic)

    In [1]: import similarities

    In [2]: similarities.uuid_hash()
    Out[2]: 'C5ipbbEy5zJ'

    In [3]: similarities.string_hash("some string")
    Out[3]: 'Y7zSkq3mq5A'

    In [4]: x = {'some_dict':"with some values","with_another_key":"with_more_values"}

    In [5]: similarities.dict_hash(x)
    Out[5]: 'HHZ6x-owq7A'

Want bigger hashes? No problem.

    In [2]: similarities.string_hash("some string",22)
    Out[2]: 'XjhUAqjLxgMiUMmZxT2xoC'

Single key near duplicate hashing

    In [1]: import similarities

    In [2]: similarities.dupe_hash("this is a similar sentence")
    Out[2]: 'E7k0NTaRPkLB'

    In [3]: similarities.dupe_hash("this is also a similar sentence")
    Out[3]: 'E7k0NTaRPkLB'

    In [4]: similarities.dupe_hash("this is a very different sentence unlike the others")
    Out[4]: '3AReDsxSE7k0'


Locality Sensitive Hashing - Min Hash 

    In [1]: import similarities 

    In [2]: x = similarities.MinHash("this is a similar sentence",8)

Min Hash creates a number of buckets and uses Jaccard similarity to measure distance between two sets of buckets.

    In [3]: x.hash
    Out[3]: 
    ['MkiVvi1CbcE',
     'GIlKK7R3MeI',
     'J9eha5g1vDH',
     '1YeFzYkoMXH',
     'GNOqfA0pXUG',
     '-jFgKf4TfpP',
     '7Z_dtDBRhfJ',
     '-PEFXVP1ZOD']

    In [4]: y = similarities.MinHash("this is another similar sentence",8)

    In [5]: y.hash
    Out[5]: 
    ['6dqjGzE_dLH',
     '6UUqfI-w8TD',
     'J9eha5g1vDH',
     '1YeFzYkoMXH',
     '-l7dhyvQohF',
     '-jFgKf4TfpP',
     'IDyQGCxqVEP',
     '-PEFXVP1ZOD']

    
    In [6]: x.distance(y)
    Out[6]: 0.3333333333333333

    In [7]: y = similarities.MinHash("a completely different sentence unlike the others")

    In [8]: x.distance(y)
    Out[8]: 0.06666666666666667



Local Spatial hashing - Charikar Hash

    In [1]: import similarities 

    In [2]: x = similarities.CharikarHash("this is a similar sentence")

Charikar hashes create a bitfield (128 by default) and use hamming distance to measure similarity.

    In [3]: x.string_hash()
    Out[3]: 'T4h7RQMW_QPX7fxhRNSZkD'

    In [4]: y = similarities.CharikarHash("this is another similar sentence")

    In [5]: y.string_hash()
    Out[5]: 'R4hZQQJ42RPXr_5hYtTbmD'

    In [6]: x.distance(y)
    Out[6]: 0.171875

    In [7]: y = similarities.CharikarHash("a completely different sentence unlike the others")

    In [8]: x.distance(y)
    Out[8]: 0.390625


TODO:

    Vector hashes - Charikar for vectors and the "hashing trick"

    TF-IDF Vectors

    Hilbert curve compression

    Distance metrics



Authors
=======

Created by [Christopher Bates](https://github.com/chrsbats)

