import data
import pickle

class Neighbor:
    def __init__(self, ip, hash):
        self.ip = ip
        self.hash = hash

def load_neighbors():
    return pickle.load(open("public/neighbors.p", "rb"))

def save_neighbors(neighbors):
    pickle.dump(neighbors, open( "public/neighbors.p", "wb" ))

def init_neighbors():
    save_neighbors([])
