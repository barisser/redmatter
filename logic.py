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
    print "Trying to ping " + str(url)
    try:
        response = requests.post(url, data = d)
        print "heard response " + str(response.content)
    except:
        response = {}
        print "no response heard..."
    return response

def handle_ping_response(response):
    c = response.content
    d = json.dumps(c)
    print d


def logic_cycle():
    print "Performing Logic"
    ping()
