import hashlib
import math

def char_to_int(char):
    a = "01234567890abcdef"
    return a.index(char) + 1

def hash_to_int(hash):
    r = 1
    a = 1
    for x in hash:
        r += a * char_to_int(x)
        a = a * 16
    return r

def hash_to_mod(hash, mod):
    r = hash_to_int(hash)
    return r % mod

def string_to_mod(string, mod):
    return hash_to_mod(hashlib.sha256(string).hexdigest(), mod)
