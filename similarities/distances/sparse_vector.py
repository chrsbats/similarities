import math

def keys(x,y):
    return set(x.keys() + y.keys())

def tanimoto_sparse_vector(x,y):
    a = 0
    b = 0
    ab = 0
    for i in key(x,y):
        if i in x:
            a = a + x[i] * x[i]
            if i in y:
                ab = ab + x[i] * y[i]
        if i in y:
            b = b + y[i] * y[i]
        
    if ab < 0.0:
        ab = ab * -1.0
    return 1.0 - ab / float(a + b - ab)

def cosine_sparse_vector(x,y):
    a = 0.0
    b = 0.0
    ab = 0.0
    for i in keys(x,y):
        if i in x:
            a = a + x[i] * x[i]
            if i in y:
                ab = ab + x[i] * y[i]
        if i in y:
            b = b + y[i] * y[i]

    return 1.0 - (ab / (math.sqrt(a) * math.sqrt(b)) + 1.0) / 2.0