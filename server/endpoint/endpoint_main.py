from bottle import route, get, post, request
import create_init


@get('/init')
def init():
    body = request.json
    bingo_code = body['bingo_code']
    bingo_len = body['bingo_len']
    bingo_size = body['bingo_size']
    val = create_init.create_bingo(bingo_code, bingo_len, bingo_size)
    return val