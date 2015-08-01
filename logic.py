import json
import neighbor
import requests
import time

def ping():
    neighbors = neighbor.load_nodes()
    for neigh in neighbors:
        ping_neighbor(neigh)

def ping_neighbor(neighbor):
    d = {}
    d['type'] = 'ping'
    d = json.dumps(d)
    url = str(neighbor.ip) + ":" + str(neighbor.port)
    return requests.post(url, data = d)

def handle_ping_response(response):
    c = response.content
    d = json.dumps(c)
    print d

def logic_cycle():
    print "Performing Logic"
    ping()
