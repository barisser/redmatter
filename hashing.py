import json
import hashlib
import random
import requests
import time
import util

hash_hard_update_cycle = 200


def get_last_hash():
    return json.dumps(requests.get("https://blockchain.info/q/latesthash").content)


def hash_thread():
    hash_data = init_hash_data()
    while True:
        hash_data = hash_cycle(hash_data)


def hash_cycle(hash_data):
    b = time.time()
    if b - time.time() > hash_hard_update_cycle:
        hash_data['last_block_hash'] = get_last_hash()
    return hash(hash_data)


def hash(hash_data):
    input = str(random.random()) + str(hash_data['last_block_hash'])
    n = hashlib.sha256(input).hexdigest()
    if compare_hashes(n, hash_data['best_hash']):
        hash_data['best_hash'] = n
        print "hash found "+str(n)
        print util.hash_to_int(n)
        hash_data['hash_answer'] = input
    return hash_data


def init_hash_data():
    d = {}
    d['last_block_hash'] = get_last_hash()
    d['hash_answer'] = str(random.random()) + str(d['last_block_hash'])
    d['best_hash'] = hashlib.sha256().hexdigest()
    return d


def compare_hashes(new_hash, best_hash):
    return util.hash_to_int(new_hash) < util.hash_to_int(best_hash)
