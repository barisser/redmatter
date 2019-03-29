from flask import Flask
from flask import request
from flask import make_response
import data
import json
import neighbor
import serving_logic

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/')
def something():
    identity = data.fetch_identity()
    response=make_response("I'm made of Redmatter.  My name is " + str(identity), 200)
    response.headers['Access-Control-Allow-Origin']= '*'
    return response


@app.route('/', methods=['POST'])
def redmatter():
    jsoninput=json.loads(request.data)

    jsonresponse = serving_logic.handle_redmatter_request(jsoninput)

    jsonresponse=json.dumps(jsonresponse)
    response=make_response(str(jsonresponse), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin']= '*'
    return response


@app.route('/neighbors')
def neighbors():
    d = {}
    d['me'] = data.fetch_identity()
    d['neighbors'] = neighbor.load_neighbors()
    jsonresponse = json.dumps(d)
    response = make_response(str(jsonresponse), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin']= '*'
    return response


def serve():
    app.run(host='0.0.0.0', port=5000)
