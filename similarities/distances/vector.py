def tanimoto_vector(x,y):
    a = 0
    b = 0
    ab = 0
    for i in xrange(len(x)):
        a = a + x[i] * x[i]
        b = b + y[i] * y[i]
        ab = ab + x[i] * y[i]
    if ab < 0.0:
        ab = ab * -1.0
    return 1.0 - ab / float(a + b - ab)

def cosine_vector(x,y):
    a = 0.0
    b = 0.0
    ab = 0.0
    for i in xrange(len(x)):
        a = a + x[i] * x[i]
        b = b + y[i] * y[i]
        ab = ab + x[i] * y[i]
    return 1.0 - (ab / (math.sqrt(a) * math.sqrt(b)) + 1.0) / 2.0