from sprinkler_control import *
from flask import Flask, request
import json

app = Flask(__name__)

@app.before_request
def auth():
    apikey = request.get_json('key')

    if  apikey['apikey'] != apikeyvalue:
        return 'Unauthorized'

def convert_to_integer(prgm):
    return {
            prgrma: 0,
            prgrmb: 1,
            prgrmc: 2,
            prgrmd: 3
    }.get(prgm, 18)

@app.route('/sprinkler/<prgm>')
def start(prgm):
    someint = convert_to_integer(prgm)
    if someint == 18:
        return 'Invalid program'
    controller.startProgram(convert_to_integer(prgm))
    #return str(convert_to_integer(prgm))
    return "Started program " + prgm


@app.route('/sprinkler/stop')
def stop():
    controller.stopIrrigation()
    return "Stopping irrigation"


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')
