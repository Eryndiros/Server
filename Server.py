from flask import *        # to easily create an HTTP server
import ast
import time

AUTH = '121234'

arduino_data = {
    'LED1': 0,
    'LED2': 0,
    'FAN': 0
}

app = Flask(__name__)

log = open('Log.txt', 'w+')
log.close()


@app.route('/', methods=['POST', 'GET'])
def arduino():
    if 'Auth' in request.headers.keys() and request.headers['Auth'] == AUTH:
        if request.method == 'POST':
            if 'Data' in request.headers.keys():
                try:
                    data = ast.literal_eval(request.headers['Data'])
                    for key in data.keys():
                        if key in arduino_data.keys():
                            arduino_data[key] = data[key]
                            with open('Log.txt', 'a') as log:
                                log.write(time.strftime("%d%%%m%%%Y %H:%M").replace('%', '.') + ' ' +
                                          key + " " + str(data[key]) + "\n")
                    print arduino_data
                    return 'Thanks. '
                except:
                    abort(418)
            else:
                abort(400)
        else:
            print str(arduino_data).replace(' ', '').replace('\'', '')
            return str(arduino_data).replace(' ', '').replace('\'', '')
    else:
        abort(401)


@app.route('/log')
def log():
    with open('Log.txt', 'r') as log:
        data = log.read()
    return Response(data, mimetype='text/plain')
