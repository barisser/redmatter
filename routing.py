import math
import neighbor
import settings
import util

def closest_neighbor(neighbors, sought):
    a = []
    sought_int = util.hash_to_mod(sought, settings.network_scale)
    for x in neighbors:
        a << math.abs(sought_int - util.hash_to_mod(x.hash, settings.network_scale))
    return a

def closest(sought):
    n = neighbor.load_nodes()
    return closest_neighbor(n, sought)
