import data
import hashlib
import os
import pickle

class Neighbor:
    def __init__(self, ip, hash, port):
        self.ip = ip
        self.port = port
        self.hash = hash

def load_neighbors():
    return pickle.load(open("public/neighbors.p", "rb"))

def load_own_identity():
    return pickle.load(open("public/identity.p", "rb"))

def load_nodes():
    r = load_neighbors()
    r << load_own_identity()
    return r

def save_neighbors(neighbors):
    pickle.dump(neighbors, open( "public/neighbors.p", "wb" ))

def init_neighbors():
    save_neighbors([])

def init_identity(ip, port):
    r = hashlib.sha256(os.urandom(200)).hexdigest()
    a = Neighbor(ip, r, port)
    pickle.dump(a, open("public/identity.p", "wb"))
