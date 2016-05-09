from bottle import route, run, template, response, request
import json

@route('/')
@route('/hello/<name>')
@route('/hello')
def index(name='Man'):
    return template('<div>Hello, {{person}}!</div>', person=name)

@route('/<thing>/<id:int>')
def thing(thing, id):
    return template('Are you looking for {{object}} with identifier {{id}}', object=thing, id=id)

@route('/data/hello')
def data_hello():
    response.content_type = 'application/json; charset=UTF-8'
    resp_data = { 'noun': 'world', 'thing': 'Hello'}
    return json.dumps(resp_data)

@route('/data/2.5/forcast')
def get_forcast():
    lat = request.query.lat
    lon = request.query.lon
    return template('<div>Lat: {{lat}}, Lon: {{lon}} ', lat=lat, lon=lon)

run(host='localhost', port=8080)
