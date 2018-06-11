from flask import *        # to easily create an HTTP server
import ast

AUTH = '121234'

arduino_data = {
    'LED1': 0,
    'LED2': 0,
    'FAN': 0
}

app = Flask(__name__)


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
