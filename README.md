========
Similarities
========

Utilities for creating similarity metrics and comparisons.


Examples
========

Url-Safe Base64 64-bit hashes

    In [1]: import similarities

    In [2]: similarities.uuid_hash()
    Out[2]: 'C5ipbbEy5zJ'

    In [3]: similarities.string_hash("some string")
    Out[3]: 'Y7zSkq3mq5A'

    In [4]: x = {'some_dict':"with some values","with_another_key":"with_more_values"}

    In [5]: similarities.dict_hash(x)
    Out[5]: 'HHZ6x-owq7A'


Single key near duplicate hashing

    In [1]: import similarities

    In [2]: similarities.dupe_hash("this is a similar sentence")
    Out[2]: 'E7k0NTaRPkLB'

    In [3]: similarities.dupe_hash("this is also a similar sentence")
    Out[3]: 'E7k0NTaRPkLB'

    In [4]: similarities.dupe_hash("this is a very different sentence unlike the others")
    Out[4]: '3AReDsxSE7k0'


Local Spatial hashing - Min Hash 

    In [12]: similarities.min_hash("this is a similar sentence")
    Out[12]: 
    ['5bzX4Z1D5SA',
     'HPF9dv70SAK',
     'MV1WxKBY1xD',
     'GmrT_XYghRK',
     '8pr1qcIKpOG',
     'Fk2gqroFiRG',
     'FWzmAurH1yE',
     'L3ZOP_tzUbO']

    In [13]: similarities.min_hash("this is also sentence")
    Out[13]: 
    ['5bzX4Z1D5SA',
     'HPF9dv70SAK',
     '_4z6jVIPHdD',
     'GmrT_XYghRK',
     '8pr1qcIKpOG',
     'Fk2gqroFiRG',
     'FWzmAurH1yE',
     'L3ZOP_tzUbO']


Local Spatial hashing - Charikar Hash

    In [2]: x = similarities.CharikarHash("this is a similar sentence")

    In [3]: x.hex()
    Out[3]: '0xe46523518717fb5cebc0e128e117ab58L'

    In [4]: y = similarities.CharikarHash("this is another similar sentence")

    In [5]: y.hex()
    Out[5]: '0xe66d3b58879fab5ca3c2e122e735bb78L'

    In [6]: x.distance(y)
    Out[6]: 0.1640625

    In [7]: y = similarities.CharikarHash("a completely different sentence unlike the others")

    In [8]: x.distance(y)
    Out[8]: 0.40625


TODO:

    TF-IDF Vectors

    Hilbert curve compression

    Distance metrics



Authors
=======

Created by [Christopher Bates](https://github.com/chrsbats)

