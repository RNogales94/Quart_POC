from functools import wraps
from quart import Quart, request, Response
from os import abort
import json


app = Quart(__name__)


def authorized(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'bearer' not in request.headers:
            print('No bearer')
            abort(401)
        else:
            print('Auth!')
            token = 'OK'
            return f(token, *args, **kwargs)

    return wrap


@app.route('/api/print1', methods=['POST'])
@authorized
async def print1(token):
    data = await request.get_data()
    data = json.loads(data)
    headers = request.headers

    print(data)
    print(headers)
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/api/print2', methods=['POST'])
@authorized
async def print2(token):
    data = await request.get_data()
    data = json.loads(data)
    headers = request.headers

    print(data)
    print(headers)
    return Response(json.dumps(data), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)