
def gray_to_binary(gray,bits=4):
    """converts a given gray code to its binary number"""
    mask = 1 << (bits - 1)
    binary = gray & mask
    for i in xrange(bits-1):
        bmask = 1 << (bits - i-1)
        gmask = bmask >> 1
        if (binary & bmask) ^ ((gray & gmask) << 1): 
            binary = binary | gmask
    return binary

def binary_to_gray(binary,bits=4):
    """converts a given binary number to is gray code"""
    mask = 1 << (bits - 1)
    gray = binary & mask  
    binary = (binary ^ binary << 1) >> 1
    gray = gray | binary  
    return gray


def ROR(x, n, bits = 32):
    n = n % bits 
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

def ROL(x, n, bits = 32):
    n = n % bits
    return ROR(x, bits - n, bits)


def bin_string(integer):
    return str(integer) if integer<=1 else bin_string(integer>>1) + str(integer&1)

def get_signed_number(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask

def get_unsigned_number(number, bitLength):
    mask = pow(2,bitLength) - 1
    return number & mask

