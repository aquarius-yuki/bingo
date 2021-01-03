from bottle import route, get, post, request
import create_init


@route('/init', method='GET')
def init():
    bingo_code = request.query.get('code')
    val = {
        'endpoint': 'init',
        'code': bingo_code
    }
    return val