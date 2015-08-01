import data
import neighbor

def data_is_present(datahash):
    a = datahash in data.data_hashes
    return a

def handle_redmatter_request(data):
    print data
    if data["type"] == "ping":
        return construct_ping_response(data)
    elif data["type"] == "forward":
        forward(data)
        return construct_forward_response(data)

def forward(data):
    k=0

def construct_forward_response(data):
    r = {}
    r["type"] = "forward_response"
    r["status"] = "idk"
    return r

def construct_ping_response(data):
    n = neighbor.load_nodes()
    response = {}
    response['type'] = 'ping_response'
    response['neighbors'] = []
    for x in n:
        r = {}
        r['ip'] = x.ip
        r['port'] = x.port
        r['hash'] = x.hash
        response['neighbors'].append(r)
    print response
    return response

def handle_data_request(request):
    datahash = request['filehash']
    if data_is_present(datahash):
        response['data'] = data.open_file_contents(datahash)
        #response['neighbor'] =
        #response['state'] =
        #response['nexthash'] =
    else:
        response['neighbor'] = -1
        #response['state'] =



def handle_neighbor_request(data):
    k=0

def find_nearest_neighbor_for_filehash(filehash, myhash):
    myn = util.hash_to_int(myhash)
